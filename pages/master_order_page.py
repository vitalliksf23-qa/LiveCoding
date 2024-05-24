from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MasterOrderPage(BasePage):  # Это класс страницы теста, который наследуется от базовой страницы всех тестов
    # Это переменные которые мы присваеваем каждому элементу
    PAGE_URL = "https://qajava.skillbox.ru/module04/lesson3/os.html"
    BUTTON_COMMENT = (By.LINK_TEXT, 'Вызвать мастера')
    FULL_NAME = (By.XPATH, '//input[@class="form-input fio"]')
    STREET_NAME = (By.CSS_SELECTOR, 'input[class="data form-input street"]')
    HOUSE_NUMBER = (By.CSS_SELECTOR, 'input[class="form-input house"]')
    APARTMENT = (By.CSS_SELECTOR, 'input[class="form-input flat"]')
    DAY_OF_VISIT = (By.CSS_SELECTOR, 'input[class="form-input date"]')
    BUTTON_MASTER = (By.CSS_SELECTOR, 'button[class="form-submit"]')
    RESULT_MESSAGE_MASTER = (By.CSS_SELECTOR, 'div[class="form-result result"]')

    def call_the_wizard_with_valid_data(self, driver):
        self.element_is_visible(MasterOrderPage.BUTTON_COMMENT).click()
        self.element_is_visible(MasterOrderPage.FULL_NAME).send_keys("Вальдемар Ибрагимович Плюшкин")
        self.element_is_visible(MasterOrderPage.STREET_NAME).send_keys("Кл-Цеткин")
        self.element_is_visible(MasterOrderPage.HOUSE_NUMBER).send_keys("3Г")
        self.element_is_visible(MasterOrderPage.APARTMENT).send_keys("/1")
        self.element_is_visible(MasterOrderPage.DAY_OF_VISIT).send_keys("Понедельник")
        self.element_is_visible(MasterOrderPage.BUTTON_MASTER).click()
        self.element_is_visible(MasterOrderPage.RESULT_MESSAGE_MASTER)  # Проверяем что элемент с определенным селектором присутствует


