import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com')

soup = BeautifulSoup(response.text, 'html.parser')

for p in soup.select('p'):
    print(p)
    
for link in soup.select('a'):
    print(link.get('href')) # a태그의 href를 전부 찾기