from bs4 import BeautifulSoup
import requests
import time


query=str(input("What are you looking up for? \n :"))
query1=query.replace(' ','+')
i=int(input("Enter the page limit \n :"))

for j in range(1,i+1):
    g=0
    url=requests.get(f"https://www.xhamster20.desi/search/{query1}/?page={j}")



    soup = BeautifulSoup(url.text, 'lxml')
    thumb = soup.find_all('a', class_='root-9d8b4 video-thumb-info__name role-pop with-dropdown')
    artist = soup.find_all('a', class_='video-uploader__name')
    views=soup.find_all('div',class_='video-thumb-views')

    for a,b,c in zip(thumb,artist,views):
        link=a['href']

        swala=requests.get(link)
        soup2 = BeautifulSoup(swala.text,'lxml')
        likes=soup2.find('div',class_='rb-new__info')



        print(f"Title: {a.text} \nlink: {link}\nArtist: {b.text} \nViews: {c.text} \nLikes: {likes.text}")
        print()
        print()
        time.sleep(2)
