from selenium import webdriver
import pyperclip
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime

contacts = ['Aarzoo Mulani']
messages = ['Ayyyy it WORKSSS!!!', 'Best for a reason right ;)', 'GGEZ', 'zoooooozoooooooo']
name = 'Aarzoo Mulani'

#driver = webdriver.Firefox()
#driver.get('http://web.whatsapp.com')

def sendShit(hour, minute):
    for i in range(0, len(contacts)):
       # if contact_times[i][0] <= hour and contact_times[i][1] <= minute:
            try:
		    print "does this even run?"
                    pyperclip.copy(contacts[i])
                    #searchbar = driver.find_elements_by_xpath('//*[@id="side"]/div[1]/div/label/input')[0]
                    #searchbar = driver.find_elements_by_xpath('/html/body/div/div/div/div[3]/div/div[1]/div/label/div/div[2]')
		    searchbar = driver.find_elements_by_xpath('//*[@id="side"]/div[1]/div/label/div[2]')
		    print (searchbar)
		    searchbar.click() #Click on searchbar
                    print "does this even run3?"
		    searchbar.send_keys(Keys.CONTROL, 'v') #Search for contact for more speed
                    msg = random.choice(messages)
                    pyperclip.copy(msg) #Copies random message to clipboard
                    print msg

                    #new_chat = web_driver.find_element_by_id('input-chatlist-search')
                    #new_chat.send_keys(contacts[i], Keys.ENTER)
                    #print msg
            #-------------------------------------works till here----------------------------------------------
                    x_args = '//span[contains(@title,' + name + ')]'
                    x_arg = '//*span[contains(@title,' + contacts[i] + ')]'
                    #print x_args
                    #print x_arg
                    #x_arg = '//span[contains(@title=' + name + ')]'

                    #chat_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
                    z=driver.find_element_by_xpath("//span[contains(@title, 'Aarzoo Mulani')]")
                    print z #Prints value similar ot searchbar
                    #chat_title = wait.until(EC.presence_of_element_located(z))
                    z.click() #BUT THIS WONT FUCKING WORRRKKKK

                    #chat_title = wait.until(EC.presence_of_element_located((By.xpath(x_arg))))
                    print "wtff"
                    #chat_title.click()
                    print "wtf"
                    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
                    message.send_keys(Keys.CONTROL, 'v') #Sends message from clipboard
                    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
                    sendbutton.click() #Presses send button
                    searchbar.click() #Click on searchbar
                    searchbar.send_keys(Keys.CONTROL, 'a') #Select all
                    searchbar.send_keys(Keys.DELETE) #Delete searchbar content
                    print("Message successfully sent to :"+ contacts[i])
                    #christmas_contact_names_times[i][0] = 99
                    #christmas_contact_names_times[i][1] = 99

            except:
                    print("Error sending message to "+ contacts[i])
                    pass
            return

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://web.whatsapp.com')
#wait = WebDriverWait(driver, 6000)
#driver.maximize_window()
#contact_times = [[0]*2 for i in range(len(contacts))]

while True:
    sendShit(int(datetime.datetime.today().hour), int(datetime.datetime.today().minute))
    time.sleep(30)
