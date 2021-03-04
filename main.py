import requests
from bs4 import BeautifulSoup
import json
import re
import datetime

BASE_URL = 'https://www.fontanka.ru'

site_link = "https://www.fontanka.ru/"
rss_link = "https://www.fontanka.ru/fontanka.rss"

# response = requests.get(site_link)
# status = response.status_code  # получаем статус запроса. Если 200, то ОК
# src_text = response.text  # получаем текст страницы


#  TODO Пока комментирю что бы не обращаться к сайту постоянно
# with open('response.html', 'w', encoding='utf-8') as file:
#     file.write(src_text)

with open('response.html', encoding='utf-8') as file:
    html = file.read()

soup = BeautifulSoup(html, 'lxml')
news_cards = soup.find_all("div", class_="HTat EBsn")
all_news = {}  # Словарь для записи в jso и csv
line_number = 1
for news in news_cards:
    news_time = news.find("span", class_="HTabp").text  # Время публикации новости
    link = news.find('a')
    news_title = link.text  # Заголовок новости
    news_href = link.get("href")  # Ссылка на новость
    out = False  # Ссылка на внешний сайт
    res = re.search("(^[http|https]*)", news_href)  # Есть ли в адресе http|https
    if res.group(0) != '':  # Если есть, тогда внешняя ссылка
        news_url = news_href  # Оставляем ссылку на внешний сайт без изменений
        out = True
    else:
        news_url = BASE_URL + news_href  # дополняем внутреннюю ссылку до полной
    if not out:  # Если не внешняя, то получаем uid новости
        news_uid = re.findall("^.+\/([0-9]+)\/$", news_url)
    else:
        news_uid[0] = ''  # если внешняя ссылка, uid очищаем

    if out:  # Если ссылка внешняя, то новость без uid'а
        print(f"Время публикации: {news_time}")
    else:
        print(f"Время публикации: {news_time} - {news_uid[0]}")
    print(f"\t{news_title}")
    print(f"\t{news_url}")
    print('================================================')
    all_news[line_number] = {"time": news_time, 'title': news_title, 'uid': news_uid[0], 'href': news_url}
    line_number = line_number + 1

with open('all_news.json', 'w', encoding='utf-8') as file:
    # Параметр intent - это отступ в файле. Иначе все параметры будут в строку
    # ensure_ascii - не экранирует символы и помогает при работе с кириллицей
    json.dump(all_news, file, indent=4, ensure_ascii=False)