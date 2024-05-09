import random
import time
import config
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_experimental_option('detach', True) # do not close after test
# chrome_options.add_argument('headless') # silent mode
driver = webdriver.Chrome(options=chrome_options)
categ = ''


def find_tenders_mail():
    print("find tenders mail")
    driver.get(config.ariba_url+"/tendery")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn1-bord ')]").click()
    btns = driver.find_elements(By.XPATH, "//button[text()='75']")
    driver.execute_script("arguments[0].click();", btns[0])
    els = driver.find_elements(By.XPATH, "//div[contains(@class,'Tenders_tenderFlexWrapper')]")
    print("total = ", len(els))
    rand = random.randint(0, len(els) - 1)
    print(rand)
    # last_tend = els[-1].text
    last_tend = els[rand].text

    # for i in range(0, len(els)) :
    #     last_tend = els[i].text
    tems = last_tend.split("\n")

    # for tem in tems:
    # print(tem)
    global categ
    categ = tems[4]
    print(categ)
    time.sleep(5)


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

    subject = 'подписка ' + categ
    text_letter = 'подпиши меня на ' + categ

    driver.find_element(By.XPATH, "//input[@name='subjectbox']").send_keys(subject)
    driver.find_element(By.XPATH, '//div[@aria-label="Message Body"]').send_keys(text_letter)

    time.sleep(5)
    driver.find_element(By.XPATH, '//div[@data-tooltip="Send"]').click()
    print("отправили письмо")


find_tenders_mail()
send_mail()
