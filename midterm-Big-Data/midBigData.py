# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import xlsxwriter


driver = webdriver.Firefox()
driver.get("https://nur.kz/")

workbook = xlsxwriter.Workbook('mid.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 'News ID')
worksheet.write(0, 1, 'Title')
worksheet.write(0, 2, 'Likes')
worksheet.write(0, 3, 'Dislikes')
worksheet.write(0, 4, 'Comment')

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
link_list = driver.find_elements_by_xpath('/html/body/section[2]/div[3]/div[1]/div/div[2]/div/a')

x = 1
k = 1
k2 = 1
k3 = 1
aut = 1
lik = 1
disl = 1
while x <= len(link_list):    
    try:
        driver.find_element_by_xpath("/html/body/section[2]/div[3]/div[1]/div/div[2]/div[" + str(x) + "]/a").click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            comments = driver.find_elements_by_xpath('/html/body/section[2]/div[2]/section/div[7]/div[2]/ul/li/div[2]/div[1]')
            likes = driver.find_elements_by_xpath('/html/body/section[2]/div[2]/section/div[7]/div[2]/ul/li/div[1]/span[3]/div[1]/span[1]')
            dislikes = driver.find_elements_by_xpath('/html/body/section[2]/div[2]/section/div[7]/div[2]/ul/li/div[1]/span[3]/div[2]/span[1]')
            title = driver.find_element_by_xpath('/html/body/section[2]/div[2]/section/div[2]/article/h1')            
            try:            
                worksheet.write_rich_string(k, 1, title.text)
            except Exception:
                pass
            for i in comments:
                try:
                    worksheet.write_rich_string(k, 4, i.text)
                except Exception:                
                    worksheet.write_rich_string(k, 4, 'Some failure')
                k = k + 1
            for i in likes:
                try:
                    worksheet.write_rich_string(k2, 2, i.text)
                except Exception:                
                    worksheet.write_rich_string(k2, 2, 'Some failure')
                k2 = k2 + 1
            for i in dislikes:
                try:
                    worksheet.write_rich_string(k3, 3, i.text)
                except Exception:                
                    worksheet.write_rich_string(k3, 3, 'Some failure')
                k3 = k3 + 1            
        except NoSuchElementException:
            pass
        #########
        driver.get("https://nur.kz/")
    except Exception:
        pass
    x = x + 1


workbook.close()