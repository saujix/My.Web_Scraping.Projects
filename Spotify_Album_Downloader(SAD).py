print(f'''                           
            ssssssssss           AAA           DDDD D
            sS                  AAA A          DDD    D
            sS                 AAA   A         DDD     D
            ssssssssss        AAA     A        DDD     D
                    Ss       AAA AAAAA A       DDD     D 
                    sS      AAA         A      DDD    D 
            ssssssssss     AAA           A     DDDD D

     .............Spotify Album Downloader(SAD)................
     ..............Developed by Akshat Pasbola.................
     ......................28/07/2023..........................


''')
kini=input("Enter The Spotify Album Link \n :")

from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver=webdriver.Chrome()

driver.get(kini)

content=driver.page_source

soup=BeautifulSoup(content,'lxml')

url=soup.find_all('a',class_='t_yrXoUO3qGsJS4Y6iXX')

for x in url:
    z=x.get('href')
    link=f"https://open.spotify.com{z}"

    url = 'https://spotifymate.com/'
    driver.get(url)

    # link_enter
    email_input_locator = (By.CLASS_NAME, "form-control")
    email_input_element = driver.find_element(*email_input_locator)
    email_input_element.send_keys(link)

    # next_click

    button_locator = (By.ID, "send")
    next_button_element = driver.find_element(*button_locator)
    next_button_element.click()

    time.sleep(5)

    x = driver.page_source

    soup = BeautifulSoup(x, 'lxml')
    name =soup.find('div',class_='hover-underline')
    link = soup.find('a', class_='abutton is-success is-fullwidth')



    if link is None:
        print("Please wait 1 minute!")
        time.sleep(60)
        driver.get(url)

        # link_enter
        email_input_locator = (By.CLASS_NAME, "form-control")
        email_input_element = driver.find_element(*email_input_locator)
        email_input_element.send_keys(link)

        # next_click

        button_locator = (By.ID, "send")
        next_button_element = driver.find_element(*button_locator)
        next_button_element.click()

        time.sleep(5)

        x = driver.page_source

        soup = BeautifulSoup(x, 'lxml')
        name = soup.find('div', class_='hover-underline')
        link = soup.find('a', class_='abutton is-success is-fullwidth')

        link1 = link.get('href')
        driver.get(link1)
        time.sleep(5)
        print(f"{name.text} is downloading!")
    else:
        link1 = link.get('href')
        driver.get(link1)
        print(f"{name.text} is downloading!")
        time.sleep(5)