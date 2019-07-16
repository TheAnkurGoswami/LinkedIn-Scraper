import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd

import shelve
from auth.login import login

driver=webdriver.Chrome("./driver/chromedriver.exe")

driver.get('https://www.linkedin.com/uas/login')

driver=login(driver)

page_link='https://www.linkedin.com/mynetwork/invite-connect/connections/'
page_users_links=get_page_users_links(driver,page_link)

user_data=get_page_users_data(page_users_links)

print(user_data)
