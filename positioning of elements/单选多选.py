import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/radio")
# 单选 点击
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/article/div/div/div[7]/div/div/div[1]/div/div/div[2]/div/label[3]").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/article/div/div/div[7]/div/div/div[1]/div/div/div[1]/div/label[3]/span[2]").click()
#
time.sleep(3)
driver.close()