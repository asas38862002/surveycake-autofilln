from selenium import webdriver  #從library中引入webdriver
from selenium.webdriver.common.by import By

import time 

driver = webdriver.Chrome()    #開啟chrome browser
import time

driver.get("https://www.surveycake.com/s/4dzBB") # 更改網址以前往不同網頁
#browser.close() # 關閉瀏覽器視窗

time.sleep(5) # wait 10 sec. 


answers = driver.find_elements(By.XPATH,'//*[@class="css-jxh6ds"]')

textareas = driver.find_elements(By.CLASS_NAME,'css-i3v0av') # get textarea 

i = 1 
ar_i = 1 

# for i in range(10):
#     driver.execute_script("arguments[0].scrollIntoView();",answers[i])
#     Good = answers[i].find_elements(By.CLASS_NAME,'css-1qwxdea') # 非常滿意 class
#     ration = Good[0].find_element(By.CLASS_NAME,'css-1xsnle1')
#     ration.click()

for answer in answers:
    try:
        driver.execute_script("arguments[0].scrollIntoView();",answer)
        Good = answer.find_elements(By.CLASS_NAME,'css-1qwxdea') # 非常滿意 class
        if i == 10:
            ration = Good[5].find_element(By.CLASS_NAME,'css-1xsnle1') # 無
        elif i== 13 :
            ration = Good[3].find_element(By.CLASS_NAME,'css-1xsnle1') #Year
        elif i== 14 :
            ration = Good[1].find_element(By.CLASS_NAME,'css-1xsnle1') # agree
        else :  
            ration = Good[0].find_element(By.CLASS_NAME,'css-1xsnle1')
        ration.click() 

        if i == 15:
             ration = Good[1].find_element(By.CLASS_NAME,'css-1xsnle1')
             ration.click()  
            # have to muti-select 
        i=i+1


    except Exception as e :
        print(e)

for textarea in textareas:
    try:
        driver.execute_script("arguments[0].scrollIntoView();",textarea)
        
        if ar_i == 1 :
            textarea.send_keys('屏東縣')
        elif ar_i == 2 :
            textarea.send_keys('內埔鄉')
        else:
            textarea.send_keys('無')
        ar_i=ar_i+1


    except Exception as e :
        print(e)
    # for loop 
button = driver.find_element(By.CLASS_NAME,"css-s8higr")
driver.execute_script("arguments[0].scrollIntoView();",button)
button.click()
time.sleep(2)

confirm = driver.find_element(By.CLASS_NAME,"css-a57zav") # confirm button
driver.execute_script("arguments[0].scrollIntoView();",confirm) 
confirm.click()
time.sleep(4) #wait 

#driver.get("https://www.surveycake.com/s/4dzBB")


#input()

