from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from bs4 import BeautifulSoup
import requests
import os

print(f'''
########## YOU NEED TO LOGIN FOR THIS #########
# USES : https://saveinsta.app/en1 TO DOWNLOAD #
######### THANKS FOR DOWNLOADING ME :)##########

''')


username=input("Enter your username\n   :")

password=input("Enter Password\n   :")

loc=input(r"Enter the location To store  Example:C:\\Users\\chutk\\Documents\\ :")

handle=input("Enter the Target Instagram UserName \n   :").replace('@','')


print(f'''      ########### WORK BY SAUJIX #################
                open browser if you have small dik
                i mean it
                btw wait now 
                come back later to have all files:)
                ############################################

''')
time.sleep(2)


driver=webdriver.Chrome()
driver.minimize_window()

driver.get('https://www.instagram.com/')
time.sleep(2)


boom=driver.find_element('name','username')
boom.send_keys(username)


badam=driver.find_element('name','password')
badam.send_keys(password)
time.sleep(1)

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)

runs = 0
max_posts = 100
posts = set()


runs=0
posts=[]
driver.get(f'https://www.instagram.com/{handle}/')
time.sleep(5)
page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
print("getting links for download")
while runs < max_posts:
    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if '/p/' in href:
            linked = f'https://www.instagram.com{href}'
            if linked in posts:
                pass
            else:
                posts.append(linked)


    element = driver.find_element(By.TAG_NAME, 'body')
    element.send_keys(Keys.DOWN*10)
    runs += 1
print('done!')




#downloading portion
#_____________________________________________________________#

print("\n Downloading now!")
d=0
for x in posts:
    print(f'{d} th post is downloading!')
    driver.get('https://saveinsta.app/en1')




    type = driver.find_element('id', 's_input').send_keys(x)
    time.sleep(3)
    click = driver.find_element(By.CLASS_NAME, 'input-group-btn').click()
    time.sleep(2)

    try:
        click1 = driver.find_element(By.ID, 'closeModalBtn').click()
        time.sleep(2)
    except:
        pass

    time.sleep(2)
    x=0
    e = driver.page_source

    soup = BeautifulSoup(e, 'lxml')
    f = soup.find_all('a', rel="nofollow",class_='abutton//is-success//is-fullwidth//btn-premium//mt-3')
    for n in f:

        href = n.get('href')
        response = requests.get(href)
        content_type = response.headers['Content-Type']


        if 'audio' in content_type.lower():
            file_extension = '.mp3'
        elif 'image' in content_type.lower():
            file_extension = '.jpg'
        elif 'video' in content_type.lower():
            file_extension = '.mp4'
        else:
            file_extension='.dat'


        newpath = str(loc) + str(handle)


        if not os.path.exists(newpath):
            os.makedirs(newpath)
            file = str(newpath) + '\\' + str(d)+'.'+ str(x) + file_extension
            with open(file, 'wb') as f:
                f.write(response.content)
                x = x + 1
                time.sleep(1)

        else:
            file = str(newpath) + '\\'+str(d)+'.'+ str(x) + file_extension
            with open(file, 'wb') as f:
                f.write(response.content)
                x = x + 1
                time.sleep(1)


    print("done!")
    d = d + 1


#a note that dont run this more than 1 to 5 times a day or else your ip will be blocked like i got mine :(

#ends____________________________________________________________________________#
