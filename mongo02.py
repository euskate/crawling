import pymongo

conn = pymongo.MongoClient('192.168.99.100',32766)
db = conn.get_database("db2")
coll = db.get_collection("p20200115")

def check(a):
    print(a)
    print("-"*50)
    for i in a:
        print(i)
    print("-"*70)

dict1 = {"id":"a", "name":"abc", "age":25}
coll.insert_one(dict1)
dict1 = {"id":"b", "name":"aac", "age":15}
coll.insert_one(dict1)
dict1 = {"id":"c", "name":"abb", "age":27}
coll.insert_one(dict1)
dict1 = {"id":"a", "name":"bcc", "age":35}
coll.insert_one(dict1)
dict1 = {"id":"b", "name":"bbc", "age":18}
coll.insert_one(dict1)
dict1 = {"id":"c", "name":"acc", "age":40}
coll.insert_one(dict1)

# # SELECT * FROM p20200115
# data1 = coll.find()
# check(data1)

# # SELECT * FROM p20200115 WHERE ID='a'
# data2 = coll.find({'id':'a'})
# # check(data2)

# # SELECT ID, NAME FROM p20200115 WHERE ID='a'
# data3 = coll.find({'id':'a'},{'id':1, 'name':1})
# # check(data3)

# # SELECT * FROM p20200115 WHERE age > 10
# data4 = coll.find({'age':{"$gt":20}})
# # check(data4)

# # SELECT * FROM p20200115 ORDER BY name ASC
# data5 = coll.find().sort('name', 1)     # 1(ASC), -1(DESC)
# # check(data5)

# # SELECT * FROM p20200115 WHERE age>10 AND age<=30
# data6 = coll.find({"age":{"$gte":10, "$lte":30}})
# # check(data6)

# # SELECT COUNT(*) FROM TABLE
# data7 = coll.find().count()
# print(data7) # 반복문 X, 딕셔너리 아님

# # SELECT * FROM TABLE WHERE ID='a' OR NAME='b'
# data8  = coll.find({'$or':[{"id":'a'},{"name":'b'}]})
# # check(data8)

# #SELECT * FROM p202001015 id=a or name in (b)
# data9 = coll.find({'$or':[ {"id":'a'}, {'name':{'$regex':'bb'}} ] }) 
# check(data9)