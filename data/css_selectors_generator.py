import shelve
import os

username="#username"
password="#password"
submit="#app__container > main > div > form > div.login__form_action_container > button"
user_contact_info="#ember98 > span"

if not os.path.exists('./css_selectors'):
    os.mkdir('./css_selectors')
with shelve.open('./css_selectors/css_selectors',writeback=True) as file:
    file['username']=username
    file['password']=password
    file['submit']=submit
    file['user_contact_info']=user_contact_info
    
