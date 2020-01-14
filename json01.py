# # 파일명 : json01.py
# import json

# # 파일 읽기
# file1 = open('./resources/exam1.json')

# # str to dict로 변경
# data1 = json.load(file1)

# print(type(file1))
# print(data1)
# print(type(data1))

import json
import cx_Oracle as oci

# 접속하기(아이디/암호@서버주소:포트번호/SID)
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

# 파일 읽기
file1 = open('./resources/exam2.json', encoding="utf-8")
# str to dict로 변경
data1 = json.load(file1)

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,EMAIL,TEL,IMG,JOINDATE)
    VALUES(:ID, :PW, :NAME, :EMAIL, :TEL, :IMG, SYSDATE)
    """
cursor.execute(sql, data1)
conn.commit()

# print(data1['ID'])
# print(type(data1))


