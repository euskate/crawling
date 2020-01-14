import json
import requests
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1")
table = db.get_collection("exam21")

url1 = "http://ihongss.com/json/exam21.json"
str1 = requests.get(url1).text
data1 = json.loads(str1)

# print(data1)

sr = data1["boxOfficeResult"]["showRange"]
list1 = data1["boxOfficeResult"]["dailyBoxOfficeList"]

for i in range(0,len(list1)):
    dict1 = dict()
    
    dict1["showRange"] = sr
    dict1["rankOldAndNew"] = list1[i]["rankOldAndNew"]
    dict1["movieNm"] = list1[i]["movieNm"]
    dict1["salesShare"] = list1[i]["salesShare"]
    dict1["salesAcc"] = list1[i]["salesAcc"]
    dict1["scrnCnt"] = list1[i]["scrnCnt"]
    dict1["showCnt"] = list1[i]["showCnt"]
    table.insert_one(dict1)




# list1 = data1["boxOfficeResult"]["dailyBoxOfficeList"]
# num = int(input('정보를 확인할 영화 번호를 입력하세요'))

# print(list1[num-1])
