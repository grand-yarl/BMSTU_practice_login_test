from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def enter_site(url):
    options = webdriver.ChromeOptions()
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,800")
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver

def element_send_keys(driver, locator, key):
    element = driver.find_element(By.ID, locator)
    element.clear()
    element.send_keys(key)

def element_click(driver, locator):
    element = driver.find_element(By.ID, locator)
    element.click()

def login(driver, login, password):
    element_send_keys(driver, 'user-name', login)
    element_send_keys(driver, 'password', password)
    element_click(driver, 'login-button')

def check_passing_login(driver):
    assert driver.current_url != URL

# Заходим на сайт
chrome_driver = enter_site(url=URL)
# Вводим данные и нажимаем кнопку
login(driver=chrome_driver, login=LOGIN, password=PASSWORD)
# Проверяем переход на другую страницу
check_passing_login(driver=chrome_driver)

chrome_driver.quit()
