from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import traceback

try:
    page = webdriver.Safari()

    page.get('https://www.baseballmusings.com/cgi-bin/PSComparePitchers.py.com')

    start_box = page.find_element(By.NAME, 'StartDate')
    start_box.send_keys('03/27/2025')

    time.sleep(100)
except:
    traceback.print_exc()