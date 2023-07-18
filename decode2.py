import requests
from bs4 import BeautifulSoup

base_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

all_p_cn_text_body = soup.select("div.body__inner-container > p")

with open('lines.txt', 'w') as file:
    for elem in all_p_cn_text_body:
        file.write(elem.text + '\n')

