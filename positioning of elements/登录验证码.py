# coding = utf-8
import time


import ddddocr

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select #鼠标选择
ocr = ddddocr.DdddOcr()



driver = webdriver.Firefox()#浏览器驱动
#打开浏览器
driver.get('https://www.51safety.com.cn/')

# 浏览器全屏显示
driver.maximize_window()
# 使用绝对路径找到 控件(地图) 并且点击
driver.find_element(By.XPATH,"/html/body/div/div/header/nav/ul[2]/li[1]/a/span").click()
screenshot_base64 = driver.get_screenshot_as_base64()
# 输入用户名和密码
driver.find_element(By.XPATH,"/html/body/div/div/div[6]/div[4]/div/div[1]/input").clear()
driver.find_element(By.XPATH,"/html/body/div/div/div[6]/div[4]/div/div[1]/input").send_keys('admin_zdxgyhlwaqsc')
driver.find_element(By.XPATH,"/html/body/div/div/div[6]/div[4]/div/div[2]/input").clear()
driver.find_element(By.XPATH,"/html/body/div/div/div[6]/div[4]/div/div[2]/input").send_keys('20220622')

#driver.find_element(By.XPATH,'//*[@id="mpanel1"]/div/div[1]/font[3]').screenshot('host.png')








# 等待时间 3秒
#time.sleep(3)
# 关闭网页
#driver.close()