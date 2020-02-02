import json
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as makesoup
import requests
import urllib
import os

with open('obsstation.json') as f:
    obsstations = json.load(f)
with open('stationwfields.json') as f:
    stationwfields = json.load(f)
fields = ['DT_AIR', 'DT_PRECIP', 'DT_WIND', 'DT_RH']

##new = stationwfields.copy()
##
##for idx, val in enumerate(stationwfields):
##    for index, field in enumerate(val['fields']):
##        if field:
##            a = field.copy()
##            a[fields[index]] = 1
##            new[idx]['fields'][index] = a
##
##with open('stationwfields.json', 'w') as f:
##    stationwfields = json.dump(new, f)
##
##exit(0)

degre = re.compile('(\d+) deg (\d+) min[\W\w]*?(\d+) deg (\d+)')

#get data from a single webpage
def getdata(data):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

    
##    conn = http.client.HTTPConnection('ipm.ucanr.edu/calludt.cgi/WXDATAREPORT', 80)
    resp = requests.post('http://ipm.ucanr.edu/calludt.cgi/WXDATAREPORT',
                         headers=headers, data=data)
##conn.request('POST',
##                 '/calludt.cgi/WXDATAREPORT',
##                 urllib.parse.urlencode(data),
##                 headers)
    #obtain raw data
##    req=Request(url, )
##    page = urlopen(req).read()
##    page_soup = makesoup(page.decode('iso-8859-1'), 'html.parser')
    return resp.content#.decode('iso-8859-1')

def parsedata(soup):
    longlang = degre.findall(soup.find_all('td', {'style': 'white-space: nowrap'})[0].text)
    longlang = list(map(lambda x:int(x), longlang[0]))
    longlang = [longlang[0] + longlang[1] / 60,
                -(longlang[2] + longlang[3] / 60)]
    county = soup.find_all('td', {'colspan': '2'})[0].text[8:]
    fieldscontain = []
    for i in fields:
        fieldscontain.append(len(soup.find_all('input', {'name': i})) > 0)
    return {
        'longlang': longlang,
        'county': county,
        'fields': fieldscontain
        }

##stationwfields = [stationwfields[0]]

for index, value in enumerate(stationwfields):


    print('%2.0f' % (index/len(stationwfields)*100))

    data = {
        'FROMMONTH': 1,
        'FROMDAY': 1,
        'FROMYEAR': 2013,
        'THRUMONTH': 12,
        'THRUDAY': 31,
        'THRUYEAR': 2019,
    ##        'DT_PRECIP': 1,
    ##        PRECIP_BACKUP1: ALTURAS.A,
    ##        PRECIP_BACKUP2: .,
    ##        PRECIP_BACKUPAVG: ALTURAS.C,
    ##        'DT_AIR': 1,
    ##        'DT_WIND': 1,
    ##        'DT_RH': 1,
    ##        AIR_BACKUP1: ALTURAS.A,
    ##        AIR_BACKUP2: .,
    ##        AIR_BACKUPAVG: ALTURAS.C,
    ##        AIROBS_BACKUP1: .,
    ##        AIROBS_BACKUP2: .,
    ##        AIROBS_BACKUPAVG: .,
    ##        WX_BACKUP1: .,
    ##        WX_BACKUP2: .,
    ##        WX_BACKUPAVG: .,
        'UNITS': 'M',
        'FFMT': 'T',
        'ACTION': 'RETRIEVE+DATA',
        }

    for i in value['fields']:
        if i:
            data.update(i)
    data['STN'] = value['STN']
##    print(data)

    filename = 'data/%s.txt' % data['STN'].replace('/', '-')
    if os.path.exists(filename):
        continue
    
    a = getdata(data)
##    print(123)
##    a = makesoup(a, 'html.parser').find('pre').text
##    a = re.sub('[\w\W]*" "\n', '', a)
    with open(filename, 'bw') as f:
        f.write(a)



##    rows0=page_soup.find_all('tr',{'class':'row0 right'})
##    rows1=page_soup.find_all('tr',{'class':'row1 right'})
##    rows=rows0+rows1
##    
##    name = []
##    alldata=[name]
##    for i in range(9):
##        alldata.append([])
##    
##    for row in rows:
##        data=row.find_all('td')
##        name.append(str(data[0]).replace('<td class="left nowrap"><span class="hidden-xs">','')\
##        .split('<')[1].split('>')[1])
##        for i in range(1,10):
##            alldata[i].append(re.search(r"[-+]?\d*\.?\d+|\d+", str(data[i])).group())
##

