import time
import config
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
# chrome_options.add_argument('headless')
driver = webdriver.Chrome(options=chrome_options)

subject = ''
# text_letter =  "Могу ли я зарегистрироваться как поставщик?",
# text_letter = "Я регистрируюсь и появляется красная кнопка с надписью 'caravan', что делать?",
# text_letter = "Расскажи как проходит процедура закупок",
# text_letter = "Какие требования для пользователя для участия в закупках?",
text_letter = "Расскажи пожалуйста как зарегистрироваться в системе"


def send_mail():
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.TAB)
    driver.get('http://gmail.com')
    time.sleep(10)
    try:
        driver.find_element(By.XPATH, "//input[@type='email']").send_keys(config.gmail_login)
        driver.find_element(By.XPATH, "//span[text()='Далее']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@type='password']").send_keys(config.gmail_pass)
        driver.find_element(By.XPATH, "//span[text()='Далее']").click()
        time.sleep(10)
    except NoSuchElementException:
        print("")
    driver.find_element(By.XPATH, "//div[text()='Compose']").click()
    time.sleep(2)

    inputs = driver.find_elements(By.XPATH, "//input[@aria-haspopup='listbox']")
    inputs[-1].send_keys(config.mhp_mail)
    inputs[-1].send_keys(Keys.ENTER)
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@name='subjectbox']").send_keys(subject)
    driver.find_element(By.XPATH, '//div[@aria-label="Message Body"]').send_keys(text_letter)

    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@data-tooltip="Send"]').click()
    print("отправили письмо")


send_mail()
