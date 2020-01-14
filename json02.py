import requests
import json
import cx_Oracle as oci



conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

"""
{
    "ret":{"id":"a","name":"123","age":34},
    "ret1":{"id":"a","name":"123","age":36}
}
"""

url = "http://ihongss.com/json/exam2.json"
str1 = requests.get(url).text
data1 = json.loads(str1)

# print(type(str1))
# print(str1)

# print(type(data1))
# print(data1)


# print(type(ret))
# print(ret)

# 파일 읽기
for data in data1:
    ret = data1[data]
    print(data)
    # sql = """
    #     INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
    #     VALUES(:ID, '123', :NAME, :AGE, SYSDATE)
    #     """
    # cursor.execute(sql, ret)
    # conn.commit()
