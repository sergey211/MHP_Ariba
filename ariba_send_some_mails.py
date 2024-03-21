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
text_letters = [
    "расскажи про открытие закупочной процедуры в системе",
    # "расскажи про просмотр данных о событии",
    # "расскажи про участие и отказ от участия в событии, обязательные условия участника торгов",
    # "расскажи про просмотр содержимого в событии",
    "расскажи про выбор лотов для подачи предложения",
    "расскажи про регистрацию на сайте мхп",
    "расскажи про процесс закупок ",
    "подпиши на продукты питания",
    "расскажи на какие категории я подписан"


    # "расскажи про подачу предложения",
    # "расскажи про создание сообщения владельцу проекта",
    # "расскажи про создание альтернативного предложения",
    # "расскажи про подачу предложения с помощью импорта из Excel",
]


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
    for letter in text_letters:
        driver.find_element(By.XPATH, "//div[text()='Compose']").click()
        time.sleep(2)

        inputs = driver.find_elements(By.XPATH, "//input[@aria-haspopup='listbox']")
        inputs[-1].send_keys(config.mhp_mail)
        inputs[-1].send_keys(Keys.ENTER)
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@name='subjectbox']").send_keys(letter)  # тайтл письма
        driver.find_element(By.XPATH, '//div[@aria-label="Message Body"]').send_keys(letter)

        time.sleep(5)
        driver.find_element(By.XPATH, '//div[@data-tooltip="Send"]').click()
        print("отправили письмо")
        time.sleep(300)


send_mail()
