import csv


f = open('./resources/exam1.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
next(rdr, None)     # 컬럼 skip

for line in rdr:
    # print(type(line))
    print(line)
