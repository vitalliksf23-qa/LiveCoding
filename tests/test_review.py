import time
from pages.review_page import ReviewPage
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
        review_page = ReviewPage(driver, "https://qajava.skillbox.ru/module04/lesson3/os.html")
        review_page.open()
        review_page.leave_a_review_with_valid_data(driver)
        time.sleep(1)