import requests
from bs4 import BeautifulSoup
from itertools import zip_longest
login_url="https://gvid.rest/2down/90469974"
home_url="http://styogyt.byethost31.com/add_video.php"
url_headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
r= requests.get(url=login_url)
src=r.content
soup = BeautifulSoup(src , "lxml")
titles=soup.find_all("li",{"class":"list-group-item d-flex align-items-center justify-content-between px-0"})
title=soup.find_all("a")
you =title[2]
link_720=you["href"]
print(link_720)
you1=title[1]
link_480=you1['href']
print(link_480)
