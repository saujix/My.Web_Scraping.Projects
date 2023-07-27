
from bs4 import BeautifulSoup
import requests
import time

print()

g=0
query=str(input("What are you looking up for? \n :"))
query1=query.replace(' ','+')
i=int(input("Enter the page limit \n :"))
bool=str(input("Looking for a specific word(y,n)?\n :"))
filter = str(input("Enter the specific Keyword \n :"))


for j in range(1,i+1):
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


        if bool == "y":
            if filter.lower() in a.text.lower():
                print(f"Title: {a.text} \nlink: {link}\nArtist: {b.text} \nViews: {c.text} \nLikes: {likes.text}")
                print()
                print()
                g=g+1
            else:
                pass



        else:
            if "M" in c.text:
                print(f"Title: {a.text} \nlink: {link}\nArtist: {b.text} \nViews: {c.text} \nLikes: {likes.text}")
                print()
                print()


    if g==0:
        print("Result Not Found!")
        break
    else:
        print(f"{g} Results Found!")
        break


