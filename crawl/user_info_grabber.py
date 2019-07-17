import time
from bs4 import BeautifulSoup
import shelve

tags_file=shelve.open('./data/tags/tags')
css_selectors_file=shelve.open('./data/css_selectors/css_selectors')
def individual_user_info(driver,user_link):
    
    driver.get(user_link)
    
    user_profile_page=BeautifulSoup(driver.page_source,'html.parser')
    
    user_name=user_profile_page.find(list(tags_file['user_name'].keys())[0],list(tags_file['user_name'].values())[0]).text.strip()
    
    try:
        user_desigation=user_profile_page.find(list(tags_file['user_desigation'].keys()[0]),list(tags_file['user_desigation'].values())[0]).text.strip()
    except:
        user_desigation='NIL'
        
    try:    
        user_location=user_profile_page.find(list(tags_file['user_location'].keys()[0]),list(tags_file['user_location'].values())[0]).text.strip()
    except:
        user_location='NIL'
        
    try:
        user_description=user_profile_page.find(list(tags_file['user_description'].keys()[0]),list(tags_file['user_description'].values())[0]).text.strip()
    except:
        user_description='NIL'
    
    
    try:
        driver.find_element_by_css_selector(css_selectors_file['user_contact_info']).click()
        time.sleep(0.5)
        user_contact_page=BeautifulSoup(driver.page_source,'html.parser')
    except:
        user_contact_page=None
    
    if type(user_contact_page)!=None:
        
        try:
            user_phone_no=user_contact_page.find(list(tags_file['user_phone_no'].keys()[0]),list(tags_file['user_phone_no'].values())[0]).text.strip()
        except:
            user_phone_no='NIL'
            
        try:
            user_address=(user_contact_page.find(list(tags_file['user_address_1'].keys())[0],list(tags_file['user_address_1'].values())[0])).find(list(tags_file['user_address_2'].keys())[0],list(tags_file['user_address_2'].values())[0]).text.strip()
        except:
            user_address='NIL'
        
        try:
            user_email=(user_contact_page.find(list(tags_file['user_email_1'].keys()[0]),list(tags_file['user_email_1'].values())[0])).find(list(tags_file['user_email_2'].keys()[0]),list(tags_file['user_email_2'].values())[0]).text.strip()
        except:
            user_email='NIL'
            
    else:
        user_phone_no='NIL'
        user_address='NIL'
        user_email='NIL'
        
    return list((user_name,user_desigation,user_location,user_description,user_phone_no,user_email,user_address,user_link))
