import requests
from bs4 import BeautifulSoup
import datetime


site_link = "https://www.fontanka.ru/"
rss_link = "https://www.fontanka.ru/fontanka.rss"

response = requests.get(rss_link)
status = response.status_code  # получаем статус запроса. Если 200, то ОК
text = response.text  # получаем текст страницы
soup = BeautifulSoup(text, 'lxml')
item_list = soup.find_all("item")
for item in item_list:
    # print(item)
    title = item.find("title").text
    description = item.find("description").text
    uid = item.find("guid").text
    news_link = item.find("pdalink").text
    category = item.find("category").text
    pubDate = item.find('pubdate').text
    print(title)
    if description != '':
        print("\t" + description)
    if news_link != "":
        print(news_link)
    print("\tid = " + uid + ", категория: " + category)
    print("\t\tДата публикации: " + str(pubDate))
    print("==========================================")

# print(status)
# print(text)
