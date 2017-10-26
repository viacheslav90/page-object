from time import sleep

from selenium.webdriver.support import expected_conditions
from BasePage import BasePage
from CreateNewPostPage import CreateNewPostPage
from ManagePostsPage import ManagePostsPage
from locators import PopularPageLocators


class PopularPage(BasePage):
    def click_new_post_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(PopularPageLocators.POST_BUTTON))
        post_button = self.find_element(*PopularPageLocators.POST_BUTTON)
        post_button.click()
        return CreateNewPostPage(self.driver)

    def open_manage_posts_page(self):
        sleep(2)
        avatar_dropdown = self.find_element(*PopularPageLocators.AVATAR_DROPDOWN)
        avatar_dropdown.click()
        sleep(1)
        manage_posts_item = self.find_element(*PopularPageLocators.MANAGE_POSTS_ITEM)
        manage_posts_item.click()
        return ManagePostsPage(self.driver)