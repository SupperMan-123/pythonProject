import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
def test_baidu():
    # 解决浏览器自动关闭问题
    opetion = webdriver.ChromeOptions()
    opetion.add_experimental_option('detach', True)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com')
    title = driver.title
    url = driver.current_url

    text = driver.find_element(By.XPATH,'//*[@id="s-top-left"]/a[1]').text

    button = driver.find_element(By.XPATH,'//*[@id="su"]').accessible_name
    assert title == "百度一下，你就知道"
    assert url == "https://www.baidu.com/"
    assert text == "新闻"
    assert button == "百度一下"