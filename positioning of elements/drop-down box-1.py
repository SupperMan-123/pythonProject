import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://sahitest.com/demo/selectTest.htm")

# 选择下拉框方式一  需要引入 from selenium.webdriver.support.select import Select 这个包
# 用来定义web_element 是 select
select = Select(driver.find_element(By.ID, "s1"))
# by_index 根据select获取到下面的内容 index也可以理解为是下标 注意:0是第一个
select.select_by_index(1)
time.sleep(3)
# 选择下拉框方式二
select = Select(driver.find_element(By.ID, "s1"))
select.select_by_value("51")
time.sleep(3)
# 选择下拉框方式三 根据实际看到的内容选择
select = Select(driver.find_element(By.ID, "s1"))
select.select_by_visible_text("Mail")

time.sleep(3)
driver.close()
