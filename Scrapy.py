import json
import re
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as makesoup

with open('obsstation.json') as f:
    obsstations = json.load(f)

fields = ['DT_AIR', 'DT_PRECIP', 'DT_WIND', 'DT_RH']
find_attr = ['_BACKUP1', '_BACKUP2', '_BACKUPAVG']

degre = re.compile('(\d+) deg (\d+) min[\W\w]*?(\d+) deg (\d+)')

#get data from a single webpage
def getdata(url):
    #obtain raw data
    req=Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
    page = urlopen(req).read()
    page_soup = makesoup(page.decode('iso-8859-1'), 'html.parser')
    return page_soup

def parsedata(soup):
    longlang = degre.findall(soup.find_all('td', {'style': 'white-space: nowrap'})[0].text)
    longlang = list(map(lambda x:int(x), longlang[0]))
    longlang = [longlang[0] + longlang[1] / 60,
                -(longlang[2] + longlang[3] / 60)]
    county = soup.find_all('td', {'colspan': '2'})[0].text[8:]
    fieldscontain = []
    for i in fields:
        if len(soup.find_all('input', {'name': i})) > 0:
            obj = {}
            obj[i] = 1
            
            for j in find_attr:
                attr = i[3:] + j
                obj[attr] = soup.find('input', {'name': attr})['value']
            fieldscontain.append(obj)
        else:
            fieldscontain.append(False)
    return {
        'STN': soup.find('input', {'name': 'STN'})['value'],
        'longlang': longlang,
        'county': county,
        'fields': fieldscontain
        }
out = []

##soup = getdata(obsstations[0])
##print(parsedata(soup))

for (j, i) in enumerate(obsstations):
    print('%2.0f' % (j/len(obsstations)*100))
    soup = getdata(i)
    out.append(parsedata(soup))
    
with open('stationwfields.json', 'w') as f:
    json.dump(out, f)

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

