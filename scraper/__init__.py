import time
import re
import os
import urllib.request
import numpy as np
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from .getimage import get_image

def scrape(url, save_to):
    driver = webdriver.Chrome()
    driver.get(url)

    href_selectors = driver.find_elements(By.CSS_SELECTOR, "a")
    href_urls = [href.get_attribute('href') for href in href_selectors if href.get_attribute('href') is not None and href.get_attribute('href').endswith('/buy')]
    count = 0
    for href in href_urls :
        if count == 50:
            break
        folder_name = href.split("/")[-3]
        folder_path = os.path.join(save_to, folder_name)
        get_image(href,driver, folder_path)
        count = count + 1

    driver.quit()

