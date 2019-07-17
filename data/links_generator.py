import shelve
import os

if not os.path.exists('./links'):
    os.mkdir('./links')
with shelve.open('./links/links',writeback=True) as file:
    file['connections']='https://www.linkedin.com/mynetwork/invite-connect/connections/'
    file['login']='https://www.linkedin.com/uas/login'
