import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/select")
# 非标准 select下拉框 就直接用点击的方式选择下拉选项
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/article/div/div/div[6]/div/div/div[1]/div/div/div[1]/div/span").click()
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/article/div/div/div[6]/div/div/div[1]/div/div/div[2]/ul[2]/li[6]").click()
time.sleep(3)
driver.close()
