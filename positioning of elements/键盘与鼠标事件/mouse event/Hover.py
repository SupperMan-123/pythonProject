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
# 先找到你要的元素例如: 设置
element = driver.find_element(By.XPATH,'//*[@id="s-usersetting-top"]')
# 调用ActionChains()方法 移动光标到元素上
ActionChains(driver).move_to_element(element).perform()


