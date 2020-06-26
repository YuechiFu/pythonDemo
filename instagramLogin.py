import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome(r"D:\fuyeuchi.com\project\python\venv\Lib\site-packages\selenium\webdriver\remote\chromedriver.exe")
browser.get("https://www.instagram.com")
# 登录页面登录
WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
username = input("username")
password = input("password")
userNameInput = browser.find_element_by_xpath("//input[@name='username']").send_keys(username) # 账号
passwordInput = browser.find_element_by_xpath("//input[@name='password']").send_keys(password) # 密码
time.sleep(0.5)
submitButton = browser.find_element(By.XPATH,"//button[@type='submit']")
submitButton.click()

#登录成功后点击保存或者不保存







