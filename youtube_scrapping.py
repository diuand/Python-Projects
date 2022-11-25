import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

import json
import pandas as pa
canal = input(r'scrie wurl-ul canalului: ')
driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver,10)
driver.get(canal)


buton_accept = wait.until(EC.element_to_be_clickable((By.XPATH, r'//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button')))
buton_accept.click()
time.sleep(5)
titlu = wait.until(EC.presence_of_element_located((By.CLASS_NAME,'style-scope.ytd-channel-name')))

subscribers =  wait.until(EC.presence_of_element_located((By.ID,'subscriber-count')))
videos = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsContent"]/tp-yt-paper-tab[2]')))
videos.click()
hight = driver.execute_script('return document.documentElement.scrollHeight')

while True:
    html = driver.find_element(By.TAG_NAME,'html')
    html.send_keys(Keys.END)
    time.sleep(2)
    new_hight = driver.execute_script('return document.documentElement.scrollHeight')
    if hight == new_hight:
        break
    hight = new_hight

print('Tutilul canalului :',titlu.text)
print('Nr de subscriberi :',subscribers.text)
title_videos = wait.until(EC.presence_of_all_elements_located((By.ID,'video-title-link')))
views = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME,'inline-metadata-item.style-scope.ytd-video-meta-block')))
real_views = [view.text for view in views if view.text.count('ago') == 0]
upload_time = [times.text for times in views if times.text.count('ago') == 1]
list_of_data = []
for ct in range(len(real_views)):
    dict_of_data = {
        'title': title_videos[ct].text,
        'views': real_views[ct],
        #'upload_time': upload_time[ct]
    }
    list_of_data.append(dict_of_data)
dict = pd.DataFrame(list_of_data)

while True:
    if os.path.exists(f'chanel_{titlu.text}.txt') == False:
        with open(f'chanel_{titlu.text}.txt' , 'w') as d:
            pass
        with open(f'chanel_{titlu.text}.txt', 'a') as canal:
            for data in list_of_data:
                canal.write(json.dumps(data))
        break
    else:
        print('removing')
        os.remove(os.getcwd()+ f'/chanel_{titlu.text}.txt')

print(dict)
#style-scope ytd-c4-tab bed-header-renderer class