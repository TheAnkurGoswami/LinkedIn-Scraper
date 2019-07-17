import shelve
import os

if not os.path.exists('./tags'):
    os.mkdir('./tags')
with shelve.open('./tags/tags',writeback=True) as file:
    file['user_name']={'li':{'class':'inline t-24 t-black t-normal break-words'}}
    file['user_desigation']={'h2':{'class':'mt1 t-18 t-black t-normal'}}
    file['user_location']={'li':{'class':'t-16 t-black t-normal inline-block'}}
    file['user_description']={'span':{'class':'lt-line-clamp__line lt-line-clamp__line--last'}}
    file['user_phone_no']={'span':{'class':'t-14 t-black t-normal'}}
    file['user_address_1']={'section':{'class':'pv-contact-info__contact-type ci-address'}}
    file['user_address_2']={'a':{'class':'pv-contact-info__contact-link t-14 t-black t-normal'}}
    file['user_email_1']={'section':{'class':'pv-contact-info__contact-type ci-email'}}
    file['user_email_2']={'a':{'class':'pv-contact-info__contact-link t-14 t-black t-normal'}}
    
    file['company_name']={'h1':{'class':'org-top-card-summary__title t-24 t-black truncate'}}
    file['company_category']={'div':{'class':'org-top-card-summary__info-item org-top-card-summary__industry'}}
    file['company_hq_location']={'div':{'class':'org-top-card-summary__info-item org-top-card-summary__headquarter'}}
    file['company_followers']={'div':{'class':'org-top-card-summary__info-item org-top-card-summary__follower-count'}}
    file['company_website']={'a':{'data-control-name':'top_card_view_website_custom_cta_btn'}}
    
