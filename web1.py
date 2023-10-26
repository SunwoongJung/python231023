
from bs4 import BeautifulSoup

page = open("D:\\PythonWorkingDirectory\\test01.html", "rt", encoding = "utf-8").read()
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

# p tag 전체검색
# print(soup.find_all("p"))

# 첫번째 p만 검색
# print(soup.find("p"))

# outer-text class에서만 p 검색
# print(soup.find_all("p", class_="outer-text"))

# attrs 사용, key = class 내 이름이 outer-text인것에서 p 찾음
# print(soup.find_all("p", attrs = {"class":"outer-text"}))

# 특정 태그만 지정할 경우 id 속성
# print(soup.find_all(id = "first"))

# 태그 내 컨텐츠 가져오기
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)


