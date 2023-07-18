# Use the BeautifulSoup and requests Python packages to print out a list
# of all the article titles on the New York Times homepage.
import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, 'html.parser')

class_names = ["indicate-hover css-vf1hbp", "indicate-hover css-1gb49m4", "indicate-hover css-66vf3i"]
element_list = soup.find_all('h3', class_=class_names)

for element in element_list:
    print(element.text)


