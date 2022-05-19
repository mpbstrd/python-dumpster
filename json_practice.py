import json

with open("data.json","rb") as file:
    data = json.load(file)
    jsonData = data["users"]

with open("data2.json","w") as file:
    data2 = 
    json.dump(data2,file)

    # for i in jsonData[0]["characters"]:
    #     print(i)
    
    # prints specific users' characters
    # print(jsonData[0]["characters"])

    # for x in jsonData:
    #     header = x.keys()
    #     print(header)
    #     values = x.values()
    #     print(values)