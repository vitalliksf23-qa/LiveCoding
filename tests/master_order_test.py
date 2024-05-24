import time
from pages.master_order_page import MasterOrderPage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import pytest


class TestComputer:
    def test1(self, driver):
        master_order_page = MasterOrderPage(driver, "https://qajava.skillbox.ru/module04/lesson3/os.html")
        master_order_page.open()
        master_order_page.call_the_wizard_with_valid_data(driver)
        # driver.save_screenshot("screen.png")
        # print(driver.get_cookies())
        # driver.add_cookie({
        #     "name": "POP",
        #     "value": "Kukushka"
        # })

