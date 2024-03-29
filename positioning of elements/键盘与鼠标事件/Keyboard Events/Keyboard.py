from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import ddddocr
import time
# 解决浏览器自动关闭问题
opetion = webdriver.ChromeOptions()
opetion.add_experimental_option('detach',True)

driver = webdriver.Chrome(chrome_options=opetion)
driver.implicitly_wait(30)
# 打开浏览器
driver.get('https://www.baidu.com/')
# 页面最大化
driver.maximize_window()
# 百度搜索框 输入键盘 SPACE 按键
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys(Keys.SPACE)
# 百度搜索框 输入键盘 NUMPAD3 按键
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys(Keys.NUMPAD3)
# 百度搜索框 回退键删除 数字3
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys(Keys.BACK_SPACE)
# F5
driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys(Keys.F5)




