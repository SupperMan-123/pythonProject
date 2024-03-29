from selenium import webdriver
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
# 定位到原对象元素
source = driver.find_element(By.XPATH,'xxx')
# 定位到目标对象元素
target = driver.find_element(By.XPATH,'xxx')
# 调用ActionChains()方法 将原对象拖拽到目标对象的操作
ActionChains(driver).drag_and_drop(source, target).perform()


