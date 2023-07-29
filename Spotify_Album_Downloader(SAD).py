print(f'''                           
            ssssssssss           AAA           DDDD D
            sS                  AAA A          DDD    D
            sS                 AAA   A         DDD     D
            ssssssssss        AAA     A        DDD     D
                    Ss       AAA AAAAA A       DDD     D 
                    sS      AAA         A      DDD    D 
            ssssssssss     AAA           A     DDDD D

     .............Spotify Album Downloader(SAD)................
     .................Developed by Saujix......................
     ......................28/07/2023..........................

                             NOTE:
     .........If the script fails, while Downloading...........
rerun the script, the download progress is saved in save_file.json
     ..................so no need to worry.....................

     .....if you are the owner of https://spotifymate.com/.....
     ..............I LOVE YOU! MUWAAAAH! KISSES!...............
''')

import sys

bool=input("Do you want to Download Multiple Albums?(y,n)\n  :")

if bool.lower()=='y':
    num=int(input("How Many? \n    :"))
    def get_album_array(num):
        album_array = []
        if num==1:
            print("Lost some braincells?")
            sys.exit()
        else:
            for j in range(1,num):
                skini = input("Enter The Spotify Album Link \n :")
                album_array.append(skini)
            return album_array

    get_album_array(num)

    album_array=get_album_array(num)

    folder_path1 = input(r"Where to store Songs? Example:'C:\\Users\\chutk\\Music' :")

    for kini in album_array:

        from bs4 import BeautifulSoup
        import time
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import os
        import requests

        driver = webdriver.Chrome()

        driver.get(kini)

        content = driver.page_source

        w = 0

        with open('save_file.json', 'r+') as file:
            content1 = file.read().strip()
            run = int(content1) if content1 else 0

        soup = BeautifulSoup(content, 'lxml')

        url = soup.find_all('a', class_='t_yrXoUO3qGsJS4Y6iXX')

        for x in url:

            if w == run:
                w = w + 1

            else:
                w = w + 1
                z = x.get('href')
                link = f"https://open.spotify.com{z}"

                url = 'https://spotifymate.com/'
                driver.get(url)

                time.sleep(2)

                # link_enter
                email_input_locator = (By.CLASS_NAME, "form-control")
                email_input_element = driver.find_element(*email_input_locator)
                email_input_element.send_keys(link)

                # next_click

                time.sleep(2)

                button_locator = (By.ID, "send")
                next_button_element = driver.find_element(*button_locator)
                next_button_element.click()

                time.sleep(2)

                e = driver.page_source

                soup = BeautifulSoup(e, 'lxml')
                name = soup.find('div', class_='hover-underline')
                link = soup.find('a', class_='abutton is-success is-fullwidth')

                if link is None:
                    print(f"A little bit of issue in downloading")
                    print()
                    for time_wait in range(30, -1, 1):
                        print(f"...............Retrying in {time_wait} seconds!............... ")
                        time.sleep(1)

                    z = x.get('href')
                    link = f"https://open.spotify.com{z}"

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

                    time.sleep(2)

                    x = driver.page_source

                    soup = BeautifulSoup(x, 'lxml')
                    name = soup.find('div', class_='hover-underline')
                    link = soup.find('a', class_='abutton is-success is-fullwidth')

                    filename = f"{name.text}.mp3"
                    if filename in os.listdir(folder_path1):


                        print(f'''
                                               --------------------------------- 
                                               {name.text} is already Downloaded! 
                                                ----------skipping--------------
                                                     ''')
                        run = run + 1
                        pass
                    else:
                        link1 = link.get('href')

                        response = requests.get(link1)
                        folder_path = os.path.join(folder_path1, filename)
                        with open(folder_path, 'wb') as file:
                            file.write(response.content)
                        # driver.get(link1)

                        run = run + 1
                        with open('save_file.json', 'w') as file:
                            j = str(run)
                            file.write(j)

                        print(f"{name.text} is downloading!\n")
                        time.sleep(2)

                else:
                    filename = f"{name.text}.mp3"
                    if filename in os.listdir(folder_path1):


                        print(f'''
                                               --------------------------------- 
                                               {name.text} is already Downloaded! 
                                                ----------skipping--------------
                                                     ''')
                        run = run + 1
                        pass
                    else:
                        link1 = link.get('href')

                        response = requests.get(link1)
                        folder_path = os.path.join(folder_path1, filename)

                        with open(folder_path, 'wb') as file:
                            file.write(response.content)
                            run = run + 1
                            with open('save_file.json', 'w') as file:
                                j = str(run)
                                file.write(j)

                            print(f"{name.text} is downloading!\n")
                            time.sleep(2)




else:
    kini = input("Enter The Spotify Album Link \n :")
    folder_path1 = input(r"Where to store Songs?  Example:'C:\\Users\\chutk\\Music' :")
    from bs4 import BeautifulSoup
    import time
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import os
    import requests

    driver = webdriver.Chrome()

    driver.get(kini)

    content = driver.page_source

    w = 0

    with open('save_file.json', 'r+') as file:
        content1 = file.read().strip()
        run = int(content1) if content1 else 0

    soup = BeautifulSoup(content, 'lxml')

    url = soup.find_all('a', class_='t_yrXoUO3qGsJS4Y6iXX')

    for x in url:

        if w == run:
            w = w + 1

        else:
            w = w + 1
            z = x.get('href')
            link = f"https://open.spotify.com{z}"

            url = 'https://spotifymate.com/'
            driver.get(url)

            time.sleep(2)

            # link_enter
            email_input_locator = (By.CLASS_NAME, "form-control")
            email_input_element = driver.find_element(*email_input_locator)
            email_input_element.send_keys(link)

            # next_click

            time.sleep(2)

            button_locator = (By.ID, "send")
            next_button_element = driver.find_element(*button_locator)
            next_button_element.click()

            time.sleep(2)

            e = driver.page_source

            soup = BeautifulSoup(e, 'lxml')
            name = soup.find('div', class_='hover-underline')
            link = soup.find('a', class_='abutton is-success is-fullwidth')

            if link is None:
                print(f"A little bit of issue in downloading")
                print()
                for time_wait in range(30, -1, 1):
                    print(f"...............Retrying in {time_wait} seconds!............... ")
                    time.sleep(1)

                z = x.get('href')
                link = f"https://open.spotify.com{z}"

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

                time.sleep(2)

                x = driver.page_source

                soup = BeautifulSoup(x, 'lxml')
                name = soup.find('div', class_='hover-underline')
                link = soup.find('a', class_='abutton is-success is-fullwidth')

                filename = f"{name.text}.mp3"
                if filename in os.listdir(folder_path1):


                    print(f'''
                           --------------------------------- 
                           {name.text} is already Downloaded! 
                            ----------skipping--------------
                                 ''')
                    run=run+1
                    pass
                else:
                    link1 = link.get('href')

                    response = requests.get(link1)
                    folder_path = os.path.join(folder_path1, filename)
                    with open(folder_path, 'wb') as file:
                        file.write(response.content)





                    # driver.get(link1)

                    run = run + 1
                    with open('save_file.json', 'w') as file:
                        j = str(run)
                        file.write(j)

                    print(f"{name.text} is downloading!\n")
                    time.sleep(2)



            else:
                filename = f"{name.text}.mp3"
                if filename in os.listdir(folder_path1):


                    print(f'''
                                           --------------------------------- 
                                           {name.text} is already Downloaded! 
                                            ----------skipping--------------
                                                 ''')
                    run = run + 1
                    pass
                else:
                    link1 = link.get('href')

                    response = requests.get(link1)
                    folder_path = os.path.join(folder_path1, filename)
                    with open(folder_path, 'wb') as file:
                        file.write(response.content)
                    # driver.get(link1)

                    run = run + 1
                    with open('save_file.json', 'w') as file:
                        j = str(run)
                        file.write(j)

                    print(f"{name.text} is downloading!\n")
                    time.sleep(2)

            with open('save_file.json', "w") as file:
                file.write("")

with open('save_file.json', "w") as file:
        file.write("")
