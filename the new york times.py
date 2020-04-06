import requests
from bs4 import BeautifulSoup

url="https://timesofindia.indiatimes.com/"
r=requests.get(url)
r_html=r.text
soup=BeautifulSoup(r_html,'html.parser')
r_html=soup.prettify()
with open("toi.html","w",encoding='utf-8') as new:
    new.write(r_html)
soup.find_all(class_="top-story")
for story_heading in soup.find_all(class_="top-story"):
    if story_heading.a:
        print(story_heading.a.text)
else:
    print(story_heading.contents[0])