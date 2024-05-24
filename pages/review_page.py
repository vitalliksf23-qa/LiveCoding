from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ReviewPage(BasePage):  # Это класс страницы теста, который наследуется от базовой страницы всех тестов
    # Это переменные которые мы присваеваем каждому элементу
    PAGE_URL = "https://qajava.skillbox.ru/module04/lesson3/os.html"
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input[class='data text']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[class='data field']")
    MESSAGE_INPUT = (By.CSS_SELECTOR, "textarea[class='field text']")
    BUTTON = (By.ID, "comment")

    def leave_a_review_with_valid_data(self, driver):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT)).send_keys("IVAN")
        self.element_is_visible(ReviewPage.EMAIL_INPUT).send_keys("IVAN@IVAN.RU")
        self.element_is_visible(ReviewPage.MESSAGE_INPUT).send_keys("Спасибо за ремонт")
        self.element_is_visible(ReviewPage.BUTTON).click()
