# 주석
"""
[오라클 데이터 베이스 설치]
docker툴박스 다운로드 : https://github.com/docker/toolbox/releases

docker search oracle-12c  => 오라클 이미지 검색
docker-machine stop  => 도커 머신 종료, 메모리를 8G로 변경
docker-machine start => 도커 머신 시작

docker pull truevoly/oracle-12c   <= 이미지를 가져옴. 
docker images  => 이미지 확인

컨테이너 만들기 (최초 1 회만)
docker run --name oracle12c -d -p 32765:8080 -p 32764:1521 truevoly/oracle-12c

docker logs oracle12c =>설치 완료인지 확인
docker ps -a  => 구동중인 컨테이너 확인
docker start oracle12c => 2번째 부터) 컨테이너 구동
docker stop oracle12c => 옵션) 컨데이너 실행 중지
docker rm oracle12c => 옵션) 컨테이너 삭제

[데이터 베이스 접속 client 프로그램 설치]
http://ihongss.com/zip/java8.zip  => 설치
http://ihongss.com/zip/sqldeveloper.zip => 압축만 풀기
http://ihongss.com/zip/oracle_client.zip => 압축만 풀기

계정생성
CREATE user admin IDENTIFIED BY 1234;
grant connect, resource, dba to admin;

"""

from flask import Flask, render_template, request, redirect

import cx_Oracle as oci # conda install cx_oracle

conn = oci.connect('admin/1234@192.168.99.100:32764/xe', encoding="utf-8")
cursor = conn.cursor()

print(conn)

app = Flask(__name__)

@app.route("/")
def index():
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    data = cursor.fetchall()        # fetchall 모든 데이터를 가져와라 [(   ),(   ),(   )]
    
    '''
    print(type(data))
    print(data)
    
    # 나이의 합을 구하라 start
    sum = 0
    # for i in range(0, len(data)):
    #     sum += data[i][3]
    for tmp in data:print(tmp[3]);sum+=tmp[3]
    print(f'전체 회원의 나이 합계는 {sum}세입니다.')
    # 나이의 합을 구하라 end
    '''

    return render_template('list.html', list=data)

@app.route("/join", methods=['GET'])
def join():
    return render_template('join.html')

@app.route("/join", methods=['POST'])
def join_post():
    # DB에 값을 넣고
    a = request.form['id']
    b = request.form['pw']
    c = request.form['name']
    d = request.form['age']
    # print("{}:{}:{}:{}".format(a,b,c,d))
    
    # 오라클 DB접속
    # 추가하는 SQL문 작성   => INSERT, SELECT, UPDATE, DELETE
    sql = "INSERT INTO MEMBER VALUES(:id, :pw, :na, :ag, SYSDATE)"
    cursor.execute(sql, id=a, pw=b, na=c, ag=d)
    conn.commit()

    # SQL문 수행

    return redirect('/')
    # 127.0.0.1/ 크롬에서 입력한 것처럼 동작

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/login", methods=['POST'])
def login_post():
    # DB에 값을 넣고
    print("login-post")


    return redirect('/')
    # 127.0.0.1/ 크롬에서 입력한 것처럼 동작
if __name__ == '__main__':
    app.run(debug=True)