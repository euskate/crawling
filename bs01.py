from bs4 import BeautifulSoup

with open('./resources/exam1.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

    # # div tag 전체 찾기
    all_divs = soup.find_all("div")
    # print(all_divs)

    # # div tag 첫번쨰 찾기
    first_divs = soup.find("div")
    # print(first_divs)

    for tmp in all_divs:
        # print(tmp)
        all_p = tmp.find_all("p")
        # print(all_p)
        for tmp1 in all_p:
            # print(tmp1)
            print(tmp1.text)


