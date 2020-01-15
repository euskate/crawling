## csv01.py #################################
import csv
import readline
import pymongo

#http://ihongss.com/csv/exam1.csv

conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1")
coll = db.get_collection("exam1") 

f = open('./resources/exam1.csv', 'r', encoding="utf-8")
rdr = csv.reader(f)
column = next(rdr) #[컬러명 읽기]

for line in rdr:
    dict1 = dict()    
    for idx, val in enumerate(line):
        dict1[column[idx]] = val

    # print(dict1)
    coll.insert_one(dict1)
conn.close()