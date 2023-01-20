import time
from selenium import webdriver
from selenium.webdriver.common.by import By



#譲れない条件、3か県
#GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScyqcd3aBJdoOe3Bs0zE1iANVEEJiPoLdB4fJbHAUFc7Wn87A/viewform?usp=sf_link"

#Moe Doc
GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSezcfV-pTzUoWWbrjMTawGwyyuSY_fjhUA5iGTeUtMtkSxXXQ/viewform?usp=sf_link"

#譲れない条件、3か県
# URL_HOMES = ["https://www.homes.co.jp/chintai/ibaraki/list/?cond%5Broseneki%5D%5B12901048%5D=12901048&cond%5Broseneki%5D%5B12100536%5D=12100536&cond%5Broseneki%5D%5B202107626%5D=202107626&cond%5Broseneki%5D%5B202109941%5D=202109941&cond%5Bmonthmoneyroomh%5D=7.0&cond%5Bhousearea%5D=0&cond%5Bhouseageh%5D=0&cond%5Bwalkminutesh%5D=15&bukken_attr%5Bcategory%5D=chintai&bukken_attr%5Bpref%5D=8",
#             "https://www.homes.co.jp/chintai/chiba/list/?cond%5Broseneki%5D%5B19401927%5D=19401927&cond%5Broseneki%5D%5B12901043%5D=12901043&cond%5Broseneki%5D%5B12901044%5D=12901044&cond%5Broseneki%5D%5B12900156%5D=12900156&cond%5Broseneki%5D%5B10300703%5D=10300703&cond%5Broseneki%5D%5B10300705%5D=10300705&cond%5Bmonthmoneyroomh%5D=7.0&cond%5Bhousearea%5D=0&cond%5Bhouseageh%5D=0&cond%5Bwalkminutesh%5D=15&bukken_attr%5Bcategory%5D=chintai&bukken_attr%5Bpref%5D=12",
#
# #HOMES_URL =         "https://www.homes.co.jp/chintai/saitama/list/?cond%5Broseneki%5D%5B10300670%5D=10300670&cond%5Broseneki%5D%5B10300689%5D=10300689&cond%5Broseneki%5D%5B10300690%5D=10300690&cond%5Broseneki%5D%5B10300691%5D=10300691&cond%5Broseneki%5D%5B10300692%5D=10300692&cond%5Broseneki%5D%5B10300693%5D=10300693&cond%5Broseneki%5D%5B10300694%5D=10300694&cond%5Broseneki%5D%5B10300695%5D=10300695&cond%5Broseneki%5D%5B10300696%5D=10300696&cond%5Broseneki%5D%5B10300638%5D=10300638&cond%5Broseneki%5D%5B10300596%5D=10300596&cond%5Broseneki%5D%5B10300697%5D=10300697&cond%5Broseneki%5D%5B10300698%5D=10300698&cond%5Broseneki%5D%5B10300699%5D=10300699&cond%5Broseneki%5D%5B10310039%5D=10310039&cond%5Broseneki%5D%5B10300700%5D=10300700&cond%5Broseneki%5D%5B10310100%5D=10310100&cond%5Broseneki%5D%5B10300701%5D=10300701&cond%5Broseneki%5D%5B10300702%5D=10300702&cond%5Broseneki%5D%5B10300703%5D=10300703&cond%5Broseneki%5D%5B10300704%5D=10300704&cond%5Broseneki%5D%5B10300705%5D=10300705&cond%5Broseneki%5D%5B10307743%5D=10307743&cond%5Broseneki%5D%5B10300706%5D=10300706&cond%5Broseneki%5D%5B10300707%5D=10300707&cond%5Broseneki%5D%5B10300708%5D=10300708&cond%5Broseneki%5D%5B10300709%5D=10300709&cond%5Broseneki%5D%5B10300710%5D=10300710&cond%5Broseneki%5D%5B84804763%5D=84804763&cond%5Broseneki%5D%5B84804766%5D=84804766&cond%5Broseneki%5D%5B84804767%5D=84804767&cond%5Bmonthmoneyroomh%5D=7.0&cond%5Bhousearea%5D=0&cond%5Bhouseageh%5D=0&cond%5Bwalkminutesh%5D=15&bukken_attr%5Bcategory%5D=chintai&bukken_attr%5Bpref%5D=11"]

#Moe URl
HOMES_URL = ["https://www.homes.co.jp/chintai/chiba/list/?cond%5Broseneki%5D%5B19401922%5D=19401922&cond%5Broseneki%5D%5B19401924%5D=19401924&cond%5Broseneki%5D%5B19401927%5D=19401927&cond%5Broseneki%5D%5B19900711%5D=19900711&cond%5Broseneki%5D%5B58006359%5D=58006359&cond%5Broseneki%5D%5B202109939%5D=202109939&cond%5Bmonthmoneyroomh%5D=7.0&cond%5Bhousearea%5D=0&cond%5Bhouseageh%5D=0&cond%5Bwalkminutesh%5D=15&bukken_attr%5Bcategory%5D=chintai&bukken_attr%5Bpref%5D=12"]
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

#homes selenium start
for _ in HOMES_URL:
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(_)
    driver.maximize_window()
    time.sleep(5)

    #link
    link_list = []
    find_href_top_2 = driver.find_elements(By.CLASS_NAME, 'prg-detailLink.detailLink')
    for my_href in find_href_top_2:
        actual_links = my_href.get_attribute('href')
        link_list.append(actual_links)

    find_href_rest = driver.find_elements(By.CSS_SELECTOR, 'div div.moduleHead h2 a')
    for my_href in find_href_rest:
        actual_links = my_href.get_attribute('href')
        link_list.append(actual_links)

    #address
    address_list = []
    find_address_top_2 = driver.find_elements(By.XPATH, '//*[@id="kksframelist"]/div/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td')
    for address in find_address_top_2:
        addresses = address.text
        address_list.append(addresses)

    find_address_rest = driver.find_elements(By.XPATH, '//*[@id="prg-mod-bukkenList"]/div[2]/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr[1]/td')
    for address in find_address_rest:
        addresses = address.text
        address_list.append(addresses)

    #rent
    rent_list = []
    rent_top_2 = driver.find_elements(By.XPATH, '//*[@id="kksframelist"]/div/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td')
    for rent in rent_top_2:
        rents = rent.text
        rent_list.append(rents)

    rent_rest = driver.find_elements(By.XPATH, '//*[@id="prg-mod-bukkenList"]/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[3]/span')
    for rent in rent_rest:
        rents = rent.text
        rent_list.append(rents)

    #google doc selenium start

    #google doc selenium_start
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(GOOGLE_FORM_LINK)
    driver.maximize_window()
    address_question = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_question.send_keys()



    for _ in range(len(address_list)):
        address_to_send = address_list[_]
        link_to_send = link_list[_].replace("'", "")
        price_to_send = rent_list[_]

        driver.get(GOOGLE_FORM_LINK)
        driver.maximize_window()

        address_input = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        url_input = driver.find_element(By.XPATH,
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        address_input.send_keys(address_to_send)
        price_input.send_keys(price_to_send)
        url_input.send_keys(link_to_send)

        submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
        submit.click()

        time.sleep(2)

