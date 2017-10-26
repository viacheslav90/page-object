from selenium.webdriver.support import expected_conditions
from BasePage import BasePage
from CreateNewPostPage import CreateNewPostPage
from locators import PopularPageLocators


class PopularPage(BasePage):
    def click_new_post_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(PopularPageLocators.POST_BUTTON))
        post_button = self.find_element(*PopularPageLocators.POST_BUTTON)
        post_button.click()
        return CreateNewPostPage(self.driver)