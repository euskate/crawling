import pymongo
import requests
import json

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1")
table = db.get_collection("exam10")

url = "http://ihongss.com/json/exam10.json"
str1 = requests.get(url).text
data1 = json.loads(str1)        # str -> dict

# print(data1['data']) # [{},{},{}]

# id,이름,나이,수학,국어

for tmp in data1['data']:
    dict1 = dict()
    dict1['id'] = tmp['id']
    dict1['name'] = tmp['name']
    dict1['age'] = tmp['age']
    dict1['math'] = tmp['score']['math']
    dict1['kor'] = tmp['score']['kor']
    table.insert_one(dict1)

conn.close()