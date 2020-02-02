import json, csv, os

windDirections = ['0', 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

with open('stationwfields.json') as f:
    stationwfields = json.load(f)
 
def readTxt(loc, cols, rel_row=0, delim=",", performLookup=-1):
    f = open(loc, encoding='utf-8', errors='replace')
    data = list(csv.reader(f, delimiter=delim))

    out = []

    if performLookup > -1:
        cols = list(map(lambda x: data[performLookup].index(x), cols))

    for i in range(len(data) - rel_row - 1):
        temp = []
        for j in cols:
            
            temp.append(data[rel_row + i][j])
        out.append(temp)

    f.close()

    return out

transformations = {
    1: lambda x: '%s/%s/%s' % (str(int(x[4:6])), str(int(x[6:8])), x[2:4]),
    5: lambda x: windDirections.index(x)
    }

def parseOneLine(a):
    for i in transformations:
        if a[i]:
            a[i] = transformations[i](a[i])
    return ["N/A" if x == '' else x for x in a]

def parseClimateData(a):
    out = []
    for i in a:
        out.append(parseOneLine(i))
    return out

        
f = open('out.csv', 'w', newline='')
writer = csv.writer(f)

for i in stationwfields:
    name = i['STN'].replace('/', '-')
##    name = 'ALTURAS.A'
    filepath = 'data/%s.txt' % name

    if os.path.exists(filepath):
        a = readTxt(filepath, [0, 1, 3, 5, 6, 9, 10, 18, 19], 1)
        a = parseClimateData(a)
        print(a[1])
        writer.writerows(a)


        
f.close()
