from selenium.webdriver.support import expected_conditions
from BasePage import BasePage
from PopularPage import PopularPage
from locators import MainPageLocators


class MainPage(BasePage):

    def click_login_link(self):
        self.wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOG_IN_LINK))
        log_in_link = self.find_element(*MainPageLocators.LOG_IN_LINK)
        log_in_link.click()

    def enter_login(self, login):
        self.wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_FIELD))
        login_field = self.find_element(*MainPageLocators.LOGIN_FIELD)
        login_field.send_keys(login)

    def enter_password(self, password):
        self.wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.PASSWORD_FIELD))
        password_field = self.find_element(*MainPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_login_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON))
        login_button = self.find_element(*MainPageLocators.LOGIN_BUTTON)
        login_button.click()

    def login(self, login, password):
        self.click_login_link()
        self.enter_login(login)
        self.enter_password(password)
        self.click_login_button()
        return PopularPage(self.driver)
