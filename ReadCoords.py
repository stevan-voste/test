import json

coords = []
JsonData = []

def createJson(data):
    for i,line in enumerate(data):
        newLine = line.split(",")
        newString = { "x": float(newLine[0]) , "y":  float(newLine[1]) }
        JsonData.append(newString)
    with open('anim_36.json', 'w') as fp:
        json.dump(JsonData, fp,sort_keys=True, indent=4)

with open("BallAnim//Ball_36.txt") as f:
    content = f.readlines()
    for x in content:
        temp = x.split()
        temp = temp[len(temp) - 1]
        splitNumber = len(temp) - 1
        temp = temp[:splitNumber]
        temp = temp[1:]
        coords.append(temp)

createJson(coords)    

