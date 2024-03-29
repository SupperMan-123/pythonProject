from selenium import webdriver
from selenium.webdriver.common.by import By
import ddddocr
import time
# 解决浏览器自动关闭问题
opetion = webdriver.ChromeOptions()
opetion.add_experimental_option('detach',True)

driver = webdriver.Chrome(chrome_options=opetion)
driver.implicitly_wait(30)
# 打开浏览器
driver.get('https://www.51safety.com.cn/')
# 页面最大化
driver.maximize_window()
# 点击登录按钮弹出登录框
driver.find_element(By.XPATH,'//*[@id="login"]/span').click()
# 输入用户名
driver.find_element(By.XPATH,'//*[@id="userName"]').send_keys('admin_zdxgyhlwaqsc')
# 输入密码
driver.find_element(By.XPATH,'//*[@id="password"]').send_keys('20220622')
# 验证码输入框位置
code = driver.find_element(By.XPATH,'//*[@id="mpanel1"]/div/div[2]/div[1]/input')
# 验证码图片位置
imgCode = driver.find_element(By.XPATH,'//*[@id="mpanel1"]/div/div[1]')
# 将验证码截图,保存为code.png 并且保存路径为../file/code.png 上一层file文件夹下
imgCode.screenshot("../file/code.png")
# 等待时间
time.sleep(2)

ocr = ddddocr.DdddOcr()
with open("../file/code.png", "rb") as fp:
    image = fp.read()
catch = ocr.classification(image)
code.send_keys(catch)


#点击登录按钮
driver.find_element(By.XPATH,'//*[@id="loginBtn"]').click()
#等待3秒钟 待页面加载完毕
time.sleep(3)
# 点击应用中心按钮
driver.find_element(By.XPATH,'//*[@id="paas-app"]/div/header/nav/ul[2]/li[2]/a').click()
# 获取当前所有窗口句柄或者叫标签,并且给他一个变量 handles
handles = driver.window_handles
# 切换到新的窗口(标签或者句柄) 0是第一个1是第二个
driver.switch_to.window(handles[1])