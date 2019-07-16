from getpass import getpass
import shelve

file=shelve.open('./data/css_selectors')

def login(driver):
    #LinkedIn account details
    email=input('Enter Email: ')
    password=getpass(prompt='Enter Password: ')
    
    driver.find_element_by_css_selector(file['username']).send_keys(email)
    driver.find_element_by_css_selector(file['password']).send_keys(password)
    driver.find_element_by_css_selector(file['submit']).click()
    
    return driver
