import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/time-picker")
# 单选时间 例 开始时间
driver.find_element(By.XPATH,'//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]').send_keys("2024-03-19")

# 多选时间 例 开始时间-结束时间 不一样的地方 elements 还加了下标
driver.find_elements(By.XPATH,'//input[@class="ivu-input ivu-input-default ivu-input-with-suffix"]')[1].send_keys("2024-03-19 - 2024-04-30")

time.sleep(3)
driver.close()
