from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 瀏覽器設定
userNameExpected = 'YourVerifyName'
# chrome.exe --remote-debugging-port=9220 --user-data-dir="C:\selenum\AutomationProfile"


# 瀏覽器設定
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=options)


# chrome_driver = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe"


url = 'https://www.imdb.com/'
driver.get(url)


set_userName_Expected = 'huang'

WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'ipc-button__text')))

# 取得登入按鈕並點擊
loginButton = driver.find_elements(By.CLASS_NAME, 'ipc-button__text')
for i in loginButton:
    if i.text == 'Sign In':
        i.click()
        break

WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'auth-provider-text')))

# 取得連結google登入按鈕並點擊
signInGoogleButton = driver.find_elements(By.CLASS_NAME, 'auth-provider-text')
for i in signInGoogleButton:
    if i.text == 'Sign in with Google':
        i.click()
        break


WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))

# 取得帳號列並輸入
accountTextField = driver.find_element(
    By.CSS_SELECTOR, 'input[autocomplete="username"]')

accountTextField.send_keys("YourAccount")


#  取得繼續按鈕並點擊
nextButton = driver.find_element(By.ID, 'identifierNext')
nextButton.click()


WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="current-password"]')))


#  取得密碼列並輸入
passwordTextField = driver.find_element(
    By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
passwordTextField.send_keys("YourPassword+")


WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.ID, 'passwordNext')))

#  取得按鈕並點擊
nextButton = driver.find_element(By.ID, 'passwordNext')
nextButton.click()


WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'ipc-button__text')))
sleep(2)
#  取得用戶名稱
userNameTextField = driver.find_elements(By.CLASS_NAME, 'ipc-button__text')
for i in userNameTextField:
    if i.text == set_userName_Expected:
        # print('true , username : '+userNameTextField.text)
        get_userName_Actual = userNameTextField.text
        driver.save_screenshot("screenshot.png")
        break
    else:
        # print('false , username : '+userNameTextField.text)
        continue


class TestInLoginName():
    assert get_userName_Actual == set_userName_Expected
