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
