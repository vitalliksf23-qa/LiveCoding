import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='function')
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    driver.maximize_window()

    #  Все что до yield выполняется перед тестом
    yield driver  # - это ключевое слово указывающий на закрытие браузера при любом исходе
    driver.close()  # Нужно прописывать чтоб в  диспетчере задач не копились процессы Chromedriver
    driver.quit()