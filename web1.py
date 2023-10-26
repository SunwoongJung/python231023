
from bs4 import BeautifulSoup

page = open("D:\\PythonWorkingDirectory\\test01.html", "rt", encoding = "utf-8").read()
soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())