import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import numpy as np
import pandas as pd
import shelve

from auth.login import login
from crawl.page_users import get_page_users_links
from crawl.page_users import get_page_users_data

choice=input('Keep Working Hidden? (y/n)\n').lower()
if choice=='y':
    opt=webdriver.ChromeOptions()
    opt.add_argument('headless')
elif choice=='n':
    opt=None
     
    
driver=webdriver.Chrome("./driver/chromedriver.exe",chrome_options=opt)

driver.get('https://www.linkedin.com/uas/login')

driver=login(driver)
page_link='https://www.linkedin.com/mynetwork/invite-connect/connections/'

page_users_links=get_page_users_links(driver,page_link)
user_data=get_page_users_data(driver,page_users_links)

pd.DataFrame(user_data).to_excel('./user data.xlsx')

driver.quit()
