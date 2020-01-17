import pandas as pd
import csv
import readline
import pymongo

# csv는 구분자 ',' '^t'
# delimiter= 속성은 구분자를 입력

#http://ihongss.com/csv/exam1.csv

df = pd.read_csv('./resources/exam1.csv', delimiter=",")
# print(df)

df = df.dropna()    # NaN 제거 : 결측치 제거
print(df)


list1 = df.values.tolist()  # DF -> list 변경

column = (list(df.columns)) # 컬렴명 읽기

## 몽고 접속
conn = pymongo.MongoClient('192.168.99.100', 32766)
db = conn.get_database("db1")
coll = db.get_collection("csv03") 

for line in list1:
    res = dict()
    for idx, val in enumerate(line):
        res[column[idx]] = val
    coll.insert_one(res)
conn.close()