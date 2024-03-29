import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://sahitest.com/demo/php/fileUpload.htm")

# 获取 input文件上传元素 注意:只能是input
upload = driver.find_element(By.XPATH,'//*[@id="file"]')
# 发送文件 绝对路劲
upload.send_keys(r"C:\Users\Administrator\PycharmProjects\pythonProject7\file\1.png")

# 点击提交附件按钮
driver.find_element(By.XPATH,'//input[@value="Submit Single"]').click()

time.sleep(3)
driver.close()