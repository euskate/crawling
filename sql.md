# Reference of SQL

[SQL 기초(W3SCHOOL)](https://www.w3schools.com/sql)

Some of The Most Important SQL Commands

    SELECT - extracts data from a database
    UPDATE - updates data in a database
    DELETE - deletes data from a database
    INSERT INTO - inserts new data into a database
    CREATE DATABASE - creates a new database
    ALTER DATABASE - modifies a database
    CREATE TABLE - creates a new table
    ALTER TABLE - modifies a table
    DROP TABLE - deletes a table
    CREATE INDEX - creates an index (search key)
    DROP INDEX - deletes an index

계정생성
```
CREATE user admin IDENTIFIED BY 1234;
grant connect, resource, dba to admin;
```

admin / 1234

### SQL

	9. SQL 명령 종류.. 이것에 속한 것이 아닌 것은..
		DDL  => 테이터 정의어
			CREATE	생성
			ALTER	변경
			DROP	삭제
			RENAME	이름변경
			TRUNCATE	비우기
		
		DML  => 테이터조작어 (Data Manipulation Language)
			INSERT INTO TABLE(ID, NAME, AGE) VALUES('a', 'b', 34)
			UPDATE TABLE SET NAME='b1', AGE=44 WHERE ID='a'
			DELETE FROM MEMBER WHERE ID='a'
			SELECT * FROM MEMBER WHERE ID LIKE 'a%' ORDER BY NO DESC | ASC
			
			% = 와일드카드… 아무거나 와도 됨..
			
		 
		DCL  => 데이터 제어어
			GRANT	권한부여
			REVOKE	권한삭제
		
		TCL  => 트랜젝션 제어어
			COMMIT	적용
			ROLLBACK
SAVEPOINT

## Oracle SQL Developer

```
새 접속(+)
	• Name : 192.168.99.100_system
	• 사용자 이름 : system
	• 비밀번호 : oracle
	• 호스트이름 : 192.168.99.100
	• 포트 : 32764 (오라클 기본 포트는 1521이다.)
	• SID : xe
```
	[_system 워크시트]
```sql
	CREATE user admin IDENTIFIED BY 1234;
	grant connect, resource, dba to admin;
```
(시스템 계정은 최상위 관리자만 사용한다.)
시스템 계정으로 관리자 계정 생성 후 새 접속(+)

```
admin
	• Name : 192.168.99.100_admin
	• 사용자 이름 : admin
	• 비밀번호 : 1234
	• 호스트이름 : 192.168.99.100
	• 포트 : 32764 (오라클 기본 포트는 1521이다.)
	• SID : xe
```

기본키 시퀀스 만들기
```
CREATE SEQUENCE SEQ_ITEM1_NO
START WITH 1
INCREMENT BY 1
NOMAXVALUE
NOCACHE;
COMMIT;
```

기본키 기본 값에 시퀀스를 지정해주면 자동생성 `SEQ_ITEM1_NO.nextval`

### 외래키 설정하기
- 편집 >제약조건 > + > 새 외래키 제약조건



#### INNER JOIN 
> 두 개의 집합의 교집합

- INNER JOIN Syntax

> The INNER JOIN keyword selects records that have matching values in both tables.

```SQL
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

```SQL
SELECT * FROM MEMBER1 t1
INNER JOIN ORDER1 t2
ON t1.no = t2.mem_no;
```
```SQL
SELECT * FROM ITEM1 t4
INNER JOIN
	(SELECT * FROM MEMBER1 t1
	INNER JOIN ORDER1 t2
	ON t1.no = t2.mem_no) t3
ON t4.no = t3.itm_no;
```








## Modeler

데이터 구조 파악

파일> 임포트> 데이터 딕셔너리 `CTRL+SHIFT+B`

1. 데이터베이스 접속 (추가)
1. 스키마/데이터베이스 선택
1. 



