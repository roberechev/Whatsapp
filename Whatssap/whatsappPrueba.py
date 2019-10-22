'''
Created on 22 oct. 2019

@author: rober
'''

from selenium import webdriver
 
chromedriver = "C:/Users/rober/Desktop/UNI/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://web.whatsapp.com")
 
while (True):
    name = input('Nombre contacto: ')
    msg = input('Mensage: ')
    count = int(input('Veces a repetir: '))
    input('Toca algo: ')
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
    msg_box = driver.find_element_by_class_name('_3u328')
    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()

