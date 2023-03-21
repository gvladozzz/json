import json
f = open('InfrastructurePipeline.json')
data = json.load(f)
old = []
for i in range(len(data)):
    if (data[i]['nazwa'] in old) == False:
        print(data[i]['nazwa'])
        old.append(data[i]['nazwa'])
print(old)
f.close()
