import requests
import json
import cx_Oracle as oci

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

url = "http://ihongss.com/json/exam4.json"
str1 = 
str1 = requests.get(url).text
data1 = json.loads(str1)


for data in data1:
    ret = data1[data]
    print(ret)
    for tmp in ret:
        sql = """
            INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
            VALUES(:ID, 'pwpw', :NAME, :AGE, SYSDATE)
            """
        cursor.execute(sql, tmp)
conn.commit()
