import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://sahitest.com/demo/confirmTest.htm")
# 弹窗 1 点击按钮
driver.find_element(By.XPATH,'//input[@value="Click For Confirm"]').click()
# 使用alert.text 函数获取弹窗的文字
print(driver.switch_to.alert.text)
time.sleep(3)
# 点击弹窗中的 确认 按钮
driver.switch_to.alert.accept()
# 点击弹窗中的 取消 按钮
#driver.switch_to.alert.dismiss()

time.sleep(3)
driver.close()