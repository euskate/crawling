# Reference of Docker
도커에 관련된 개인 정리 레퍼런스입니다.

## 설치
docker툴박스 다운로드
https://github.com/docker/toolbox/releases

## Oracle 설치 관련
```
$ docker search oracle-12c
어떤 오라클 이미지가 있는지 검색해본다.

$ docker-machine stop
도커 머신을 종료한다.
```

- Oracle VM VirtualBox 실행
- 설정 > 시스템 > 기본메모리 변경
- 4096 or 8192 등... 사양에 맞게 메모리를 증가시킨다.

```
$ docker-machine start
도커 머신을 시작한다.

$ docker pull truevoly/oracle-12c
이미지(truevoly/oracle-12c)를 가져온다

$ docker images
 이미지 확인

$ docker run --name oracle12c -d -p 32765:8080 -p 32764:1521 truevoly/oracle-12c
 컨테이너 만들기 (최초 1 회만)

$ docker logs oracle12c
 설치 완료인지 확인

$ docker ps -a
 구동중인 컨테이너 확인

```

- 설치 이후 실행 및 삭제 
```
$ docker start oracle12c
 2번째 부터) 컨테이너 구동

$ docker stop oracle12c
 옵션) 컨데이너 실행 중지

$ docker rm oracle12c 
 옵션) 컨테이너 삭제
```

- 파이썬 오라클 모듈 설치

    `> pip install cx_oracle`


## MongoDB 설치 관련

```
$ docker search mongo
    MongoDB 이미지 검색
$ docker pull mongo
    MongoDB 이미지 가져오기

$ docker images
    MongoDB 이미지 확인 

$ docker run --name mongodb -d -p 32766:27017 mongo
    MongoDB 컨테이너 만들기

$ docker logs mongodb
    설치 완료 확인
```

- 파이썬 mongoDB 라이브러리 설치

    `> pip install pymongo`
