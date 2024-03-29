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
# 先找到你要的元素例如: 换一换
element = driver.find_element(By.XPATH,'//*[@id="hotsearch-refresh-btn"]/span')
# 调用ActionChains()方法 双击 换一换 这个元素
ActionChains(driver).double_click(element).perform()


