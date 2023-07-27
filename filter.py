#method 2 by sarching

from bs4 import BeautifulSoup
import requests

query=str(input("What are you looking up for? \n :"))
query1=query.replace(' ','+')
i=int(input("Enter the page limit \n :"))

for j in range(1,i+1):
    url=requests.get(f"https://www.xhamster20.desi/search/{query1}/?page={j}")
    soup = BeautifulSoup(url.text, 'lxml')
    thumb = soup.find_all('a', class_='root-9d8b4 video-thumb-info__name role-pop with-dropdown')

    for a in thumb:
        link = a['href']
        artist=a.find_all('a',class_="video-uploader__name")
        print(f"Title: {a.text} \nlink: {link} ")
        print()
        print()
