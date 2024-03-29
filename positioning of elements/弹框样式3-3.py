import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://sahitest.com/demo/promptTest.htm")
# 弹窗 1 点击按钮 弹出弹窗
driver.find_element(By.XPATH,'//input[@value="Click For Prompt"]').click()
# 使用alert.text 函数获取弹窗的文字
print(driver.switch_to.alert.text)
time.sleep(3)
# 在弹窗中输入 "ok"
driver.switch_to.alert.send_keys("ok")
time.sleep(3)
# 点击弹窗中的 确定 按钮
driver.switch_to.alert.accept()

time.sleep(3)
driver.close()