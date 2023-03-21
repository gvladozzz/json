import json
f = open('InfrastructurePipeline.json')
data = json.load(f)
dict = {}
for i in range(len(data)):
    dict[data[i]['nazwa']] = 0
for i in range(len(data)):
    dict[data[i]['nazwa']] += data[i]['dlugosc']
print(dict)
f.close()