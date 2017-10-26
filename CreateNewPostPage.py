from time import sleep
from selenium.webdriver.support import expected_conditions
from BasePage import BasePage
from locators import CreateNewPostLocators


class CreateNewPostPage(BasePage):
    def enter_title(self, title):
        self.wait.until(expected_conditions.element_to_be_clickable(CreateNewPostLocators.TITLE_FIELD))
        title_field = self.find_element(*CreateNewPostLocators.TITLE_FIELD)
        title_field.send_keys(title)

    def click_publish_close_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(CreateNewPostLocators.PUBLISH_CLOSE_BUTTON))
        publish_close_button = self.find_element(*CreateNewPostLocators.PUBLISH_CLOSE_BUTTON)
        publish_close_button.click()

    def click_add_image_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(CreateNewPostLocators.ADD_IMAGE_BUTTON))
        add_image_button = self.find_element(*CreateNewPostLocators.ADD_IMAGE_BUTTON)
        add_image_button.click()

    def add_image(self, path_to_image):
        input_image_element = self.find_element(*CreateNewPostLocators.INPUT_FILE)
        input_image_element.send_keys(path_to_image)
        sleep(5)

    def enter_tags(self, tags):
        self.wait.until(expected_conditions.element_to_be_clickable(CreateNewPostLocators.ADD_TAGS_FIELD))
        add_tags_field = self.find_element(*CreateNewPostLocators.ADD_TAGS_FIELD)
        add_tags_field.send_keys(tags)
        add_tags_field.send_keys(',')

    def click_publish_button(self):
        self.wait.until(expected_conditions.element_to_be_clickable(CreateNewPostLocators.PUBLISH_BUTTON))
        publish_button = self.find_element(*CreateNewPostLocators.PUBLISH_BUTTON)
        publish_button.click()