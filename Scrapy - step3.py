import json,re, os


with open('stationwfields.json') as f:
    stationwfields = json.load(f)

for i in stationwfields:
    name = i['STN'].replace('/', '-')
    filepath = 'data/%s.txt' % name

    if os.path.exists(filepath):
        with open(filepath, encoding='iso-8859-1') as f:
            preprocessed = f.read()
            
            a = preprocessed.split('</a>\n')[1].split('</pre>')[0]

        with open(filepath, 'w') as f:
            f.write(a)
