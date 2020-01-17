# pip install pymongo
import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db1") # 없으면 db1 생성 (있으면 가져옴)
table = db.get_collection("table1") # 없으면 collection 생성 (있으면 가져옴)
dict1 = {"id":"a", "age":35}

table.insert_one(dict1)     # 추가하기

# data1 = table.find()
# for tmp in data1:
#     print(tmp)


conn.close()