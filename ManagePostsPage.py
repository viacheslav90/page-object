from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from BasePage import BasePage
from locators import ManagePostsLocators


class ManagePostsPage(BasePage):
    def select_post(self, post_name):
        posts_array = self.find_elements_array(*ManagePostsLocators.POSTS_ARRAY)
        counter = 1
        for post in posts_array:
            if post.text == post_name:
                checkboxes_array = self.find_elements_array(*ManagePostsLocators.CHECKBOXES_ARRAY)
                post_checkbox = checkboxes_array[counter]
                action_chains = ActionChains(self.driver)
                action_chains.move_to_element(post_checkbox).click().perform()
            counter += 1

    def edit_post(self, post_name):
        posts_array = self.find_elements_array(*ManagePostsLocators.POSTS_ARRAY)
        counter = 0
        for post in posts_array:
            if post.text == post_name:
                edit_buttons_array = self.find_elements_array(*ManagePostsLocators.EDIT_BUTTONS_ARRAY)
                edit_button = edit_buttons_array[counter]
                edit_button.click()
            counter += 1

    def click_delete_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(ManagePostsLocators.DELETE_BUTTON))
        delete_button = self.find_element(*ManagePostsLocators.DELETE_BUTTON)
        delete_button.click()

    def confirm_deleting_post(self):
        sleep(1)
        yes_button = self.find_element(*ManagePostsLocators.YES_CONFIRMING_DELETING_BUTTON)
        yes_button.click()
