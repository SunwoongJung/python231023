import requests
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
f = open("D:\\PythonWorkingDirectory\\dangn.txt", "wt", encoding="utf-8")

posts = soup.find_all("div", attrs = {"class":"card-desc"})
for post in posts:
    title = post.find("h2", attrs = {"class" : "card-title" })
    price = post.find("div", attrs = {"class" : "card-price" })
    addr = post.find("div", attrs = {"class" : "card-region-name" })

    title = title.text.strip().replace("\n", "")
    price = price.text.strip().replace("\n", "")
    addr = addr.text.strip().replace("\n", "")
    print("{0}, {1}, {2}".format(title, price, addr))

    f.write(f"{title},{price},{addr}\n")

f.close()

    
