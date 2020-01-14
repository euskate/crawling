# pip install cx_oracle 모듈 설치
import cx_Oracle as oci

# 접속하기(아이디/암호@서버주소:포트번호/SID)
conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="cp949")
print(conn) # 확인

# 커서 생성
cursor = conn.cursor()

# SELECT
sql = "SELECT * FROM MEMBER"
cursor.execute(sql)
data = cursor.fetchall()        #[(  ),(  ),(  ), ... ]
print(data)

sql = """
    INSERT INTO MEMBER(ID,PW,NAME,EMAIL,TEL,IMG,JOINDATE)
    VALUES(:1, :2, :3, :4, :5, :6, SYSDATE)
"""
arr = ['a2','a2','이름','2@2','2-2','img']
cursor.execute(sql, arr)
conn.commit()