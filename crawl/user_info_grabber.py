import time
from bs4 import BeautifulSoup
import shelve

def individual_user_info(driver,user_link):
    
    driver.get(user_link)
    
    user_profile_page=BeautifulSoup(driver.page_source,'html.parser')
    
    user_name=user_profile_page.find('li',{'class':'inline t-24 t-black t-normal break-words'}).text.strip()
    
    try:
        user_desigation=user_profile_page.find('h2',{'class':'mt1 t-18 t-black t-normal'}).text.strip()
    except:
        user_desigation='NIL'
        
    try:    
        user_location=user_profile_page.find('li',{'class':'t-16 t-black t-normal inline-block'}).text.strip()
    except:
        user_location='NIL'
        
    try:
        user_description=user_profile_page.find('span',{'class','lt-line-clamp__line lt-line-clamp__line--last'}).text.strip()
    except:
        user_description='NIL'
    
    
    try:
        driver.find_element_by_css_selector(user_contact_info).click()
        time.sleep(0.5)
        user_contact_page=BeautifulSoup(driver.page_source,'html.parser')
    except:
        user_contact_page=None
    
    if type(user_contact_page)!=None:
        
        try:
            user_phone_no=user_contact_page.find('span',{'class','t-14 t-black t-normal'}).text.strip()
        except:
            user_phone_no='NIL'
            
        try:
            user_address=(user_contact_page.find('section',{'class','pv-contact-info__contact-type ci-address'})).find('a',{'class','pv-contact-info__contact-link t-14 t-black t-normal'}).text.strip()
        except:
            user_address='NIL'
        
        try:
            user_email=(user_contact_page.find('section',{'class','pv-contact-info__contact-type ci-email'})).find('a',{'class':'pv-contact-info__contact-link t-14 t-black t-normal'}).text.strip()
        except:
            user_email='NIL'
            
    else:
        user_phone_no='NIL'
        user_address='NIL'
        user_email='NIL'
        
    return list((user_name,user_desigation,user_location,user_description,user_phone_no,user_email,user_address,user_link))
