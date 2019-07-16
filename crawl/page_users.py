import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from crawl.user_info_grabber import individual_user_info

def get_page_users_links(driver,page_link):
    driver.get(page_link)
    page=BeautifulSoup(driver.page_source,'html.parser')
    
    total=[]
    temp=[]
    
    while 1:
        
        temp=[]
        for i in page.findAll('a',attrs={'data-control-name':'connection_profile'}):
            temp.append('https://www.linkedin.com'+i['href'])
        if set(total)==set(temp):
            break
        else:
            total=temp.copy()
            driver.find_element_by_css_selector('body').send_keys(Keys.END)
            driver.find_element_by_css_selector('body').send_keys(Keys.HOME)
            driver.find_element_by_css_selector('body').send_keys(Keys.END)
            time.sleep(5)
            page=BeautifulSoup(driver.page_source,'html.parser')
            
    return set(total)
    
    
def get_page_users_data(driver,users_links_list):
    user_details=[]
    length=len(users_links_list)
    for i in length:
        user_details.append(individual_user_info(driver,users_links_list[i]))
        print("{:0.2f}% Scraped!!".format((i/len(users_links_list))*100))
    print("Scraped {} users.".format(len(users_links_list)))
    return np.array(user_details)
