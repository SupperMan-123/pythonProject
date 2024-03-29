import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/cascader")
driver.find_element(By.XPATH,'//input[@class="ivu-input ivu-input-default"]').click()
driver.find_element(By.XPATH,'//li[@class="ivu-cascader-menu-item"]').click()
driver.find_element(By.XPATH,'//li[@class="ivu-cascader-menu-item"][2]').click()
time.sleep(3)
driver.close()


