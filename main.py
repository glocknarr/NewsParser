import requests

site_link = "https://www.fontanka.ru/"
rss_link = "https://www.fontanka.ru/fontanka.rss"

response = requests.get(rss_link)
status = response.status_code  # получаем статус запроса. Если 200, то ОК
text = response.text  # получаем текст страницы
print(status)
# print(text)
