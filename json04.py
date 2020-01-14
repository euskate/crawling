import requests
import json


url1 = "http://ihongss.com/json/exam4.json"
str1 = requests.get(url1).text
data1 = json.loads(str1)

# 결과를 name, species, likes[0], dislikes[0]으로 딕셔너리에 담아서 출력

result = {}
# print(data1)
for data in data1:
    result['name'] = data['name']
    result['species'] = data['species']
    foods = data['foods']
    for tmp in foods:
        result['likes'] = foods['likes'][0]
        result['dislikes'] = foods['dislikes'][0]
    print(result)


# data1 => {ret:[{},{},{}], ret1:[{},{},{}]}

# print(data1)
# print(type(data1['ret']))

# for data in data1:
#     ret = data1[data]
#     print(ret)
#     for tmp in ret:
#         sql = """
#             INSERT INTO MEMBER(ID,PW,NAME,AGE,JOINDATE)
#             VALUES(:ID, 'pwpw', :NAME, :AGE, SYSDATE)
#             """
#         cursor.execute(sql, tmp)
# conn.commit()
