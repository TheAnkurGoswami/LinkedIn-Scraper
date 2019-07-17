from selenium import webdriver
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


links_file=shelve.open('./data/links/links')

    

#Logging into LinkedIn account
driver.get(links_file['login'])
print("login called")
driver=login(driver)

print("""
Scrape:
     1. Your Connections details
     2. Company details (followed by you)
     3. Company Employees data (followed by you)

""")
choice=int(input())

if choice==1:    
    page_users_links=get_page_users_links(driver,links_file['connections'])
    user_data=get_page_users_data(driver,page_users_links)
    pd.DataFrame(user_data).to_excel('./Connections Data.xlsx')
    
driver.quit()
