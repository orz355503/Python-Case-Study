from selenium import webdriver
from time import sleep


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
opt.add_argument('--user-agent=%s' % user_agent)
driver = webdriver.Chrome('./chromedriver', options=opt)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
url = 'https://twitter.com'
driver.get(url)
sleep(2)
# 自動往下捲動 200px
driver.execute_script(f'window.scrollTo(0, 200)')
# 取得登入按鈕
loginButton = driver.find_element_by_css_selector('a[href="/login"]')
# 點擊登入按鈕
loginButton.click()
sleep(2)

# 取得帳號列並輸入
username = driver.find_element_by_css_selector(
    'input[autocomplete="username"]')
username.send_keys("userName")

# 取得按鈕並點擊
nextButton = driver.find_elements_by_css_selector('div[role="button"]')
for i in nextButton:
    if i.text == '下一步' or i.text == 'Next':
        i.click()
        break
sleep(1)

# 取得密碼列並輸入
password = driver.find_element_by_css_selector(
    'input[autocomplete="current-password"]')
password.send_keys("userPassword")

# 取得按鈕並點擊
buttons = driver.find_elements_by_css_selector('div[role="button"]')
for i in buttons:
    if i.text == '登入' or i.text == 'Log in':
        i.click()
        # print('點擊登入')
        break
