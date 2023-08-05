from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import os
from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

print('''

       ###############################################
       ############ DEVELOPED BY SAUJIX ##############
       this program downloads every recommended video
       
       ::::LOGIN--------------------------REQUIRED::::
       
       ##############################################
       



''')




usrnm=input('Enter Your Google Account \n   :')
pas=input('Enter Password \n   :')
loc=input("Where to download \n   Example:'C:\\Users\\chutk\\OneDrive\\Desktop\\Today_YT \n     :")


driver=webdriver.Chrome()

driver.get('https://accounts.google.com/')

username=driver.find_element(By.CLASS_NAME,'whsOnd').send_keys(usrnm)
username_click=driver.find_element(By.ID,'identifierNext').click()
time.sleep(5)

password=driver.find_element(By.NAME,'Passwd').send_keys(pas)
pasword_next=driver.find_element(By.ID,'passwordNext').click()
time.sleep(5)

driver.minimize_window()


start=time.time()

def getting_yt_url():


    driver.get('https://www.youtube.com')

    start = time.time()
    while time.time() - start < 60:
        element = driver.find_element('tag name', 'body').send_keys(Keys.DOWN * 20)
        d = driver.page_source
        soup = BeautifulSoup(d, 'lxml')

        links = soup.find_all('a', id='thumbnail')
        dink = []

        for a in links:
            z = a.get('href')
            kink = f'https://www.youtube.com{z}'
            if kink in dink:
                pass
            else:
                dink.append(kink)
    return dink

pink=getting_yt_url()

driver.quit()

print("Starting Download!")
w=0
for links in pink:
    if w<1:
        w=w+1
    else:
        for video_url in pink:
            try:
                yt = YouTube(video_url)
                if yt.title in os.listdir(loc):
                    pass
                else:
                    yt = YouTube(video_url)
                    video_stream = yt.streams.get_highest_resolution()
                    channel_name = yt.author
                    # Download the video
                    video_stream.download(output_path=f'{loc}\\{channel_name}')

                    print(f"Downloaded: {yt.title}")

            except AgeRestrictedError:
                pass
            except Exception as e:
                pass

print("Done Downloading Everything!")

