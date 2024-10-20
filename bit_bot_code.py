from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

class BitBotCode:
    def __init__(self):       
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)

        service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=service, options=chrome_options)

    def login(self, email, password):
        self.browser.get("https://comunidade.onebitcode.com/users/sign_in?post_login_redirect=https%3A%2F%2Fcomunidade.onebitcode.com%2Ffeed#email")
        self.browser.find_element(By.ID, "user_email").send_keys(email)
        self.browser.find_element(By.ID, "user_password").send_keys(password)
        self.browser.find_element(By.NAME, "commit").click()
    
    def checkClass(self, init, end):
        self.browser.get(init)
        while self.browser.current_url != end:
            self.browser.find_element(By.CLASS_NAME, 'bg-circle-button').click()
            sleep(5)

if __name__ == "__main__":
    bot = BitBotCode()
    bot.login('ksilvasousa1@gmail.com', 'Kaique.1')
    bot.checkClass("https://comunidade.onebitcode.com/c/curso/sections/360098/lessons/1336828", "https://comunidade.onebitcode.com/c/curso/sections/360098/lessons/1336850")
