import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://sahitest.com/demo/iframesTest.htm")
# 清除文本框内容
driver.find_element(By.XPATH,'//input[@value="verify me"]').clear()
# 输入文本框字符
driver.find_element(By.XPATH,'//input[@value="verify me"]').send_keys(666)
time.sleep(2)
# 切换进入iframe 框架
driver.switch_to.frame(0)
# 点击切换框架的元素
driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td[3]/a[3]').click()
# 退出iframe 返回到上一级
#driver.switch_to.parent_frame()
# 切换到主界面
driver.switch_to.default_content()
# 清除文本框内容
driver.find_element(By.XPATH,'//input[@value="verify me"]').clear()
# 输入文本框字符
driver.find_element(By.XPATH,'//input[@value="verify me"]').send_keys(777)
time.sleep(3)

driver.close()