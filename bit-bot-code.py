from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

browser.get("https://comunidade.onebitcode.com/users/sign_in?post_login_redirect=https%3A%2F%2Fcomunidade.onebitcode.com%2Ffeed#email")

browser.find_element(By.ID, "user_email").send_keys('ksilvasousa1@gmail.com')
browser.find_element(By.ID, "user_password").send_keys('Kaique.1')
browser.find_element(By.NAME, "commit").click()

browser.get("https://comunidade.onebitcode.com/c/curso/sections/360103/lessons/1337005")
while browser.current_url != "https://comunidade.onebitcode.com/c/curso/sections/360105/lessons/1337070":
    browser.find_element(By.CLASS_NAME, 'bg-circle-button').click()
    sleep(5)
