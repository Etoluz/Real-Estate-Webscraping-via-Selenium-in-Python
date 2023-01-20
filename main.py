import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#GOOGLE_FORM_LINK = "YOUR GOOGLE FORM LINK"

#Moe Doc
GOOGLE_FORM_LINK = "YOUR GOOGLE FORM LINK"

#URL YOU GET AFTER SPECIFYING RENT, CLOSEST STATION, ETC: ON HOMES.JP.CO
HOMES_URL = ["YOUR HOMES.JP.CO LINK"]
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

