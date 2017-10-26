from selenium.webdriver.common.by import By


class MainPageLocators(object):
    START_YOUR_BLOG_BUTTON = (By.XPATH, '//a/span[text()=\'Start Your Blog\']')
    LOG_IN_LINK = (By.XPATH, '//a/span[text()=\'Log In\']')
    LOGIN_FIELD = (By.ID, 'id_login')
    PASSWORD_FIELD = (By.ID, 'id_password')
    LOGIN_BUTTON = (By.XPATH, './/*[@id="login-modal"]//button')

class PopularPageLocators(object):
    POST_BUTTON = (By.XPATH, '//a/span[text()=\'Post\']')
    AVATAR_DROPDOWN = (By.ID, 'dropdownMenu2')
    MANAGE_POSTS_ITEM = (By.XPATH, './/li/a[text()=\'Manage Posts\']')

class CreateNewPostLocators(object):
    TITLE_FIELD = (By.ID, 'id_title')
    ADD_IMAGE_BUTTON = (By.XPATH, './/div[@class=\'pb-button pb-button-wrapped-input-file\']')
    INPUT_FILE = (By.XPATH, './/input[@type=\'file\']')
    PUBLISH_CLOSE_BUTTON = (By.XPATH, './/a[@class=\'link-with-icon btn btn-red post-publish-dropdown\']')
    ADD_TAGS_FIELD = (By.XPATH, './/input[@class=\'select2-search__field\']')
    PUBLISH_BUTTON = (By.ID, 'publish-btn')

class ManagePostsLocators(object):
    POSTS_ARRAY = (By.XPATH, './/*[@class="post-title"]//a')
    DELETE_BUTTON = (By.ID, 'delete-post-btn')
    CHECKBOXES_ARRAY = (By.XPATH, ".//label[@class='simple']")
    EDIT_BUTTONS_ARRAY = (By.XPATH, './/a[@class=\'btn btn-default red\']')
    YES_CONFIRMING_DELETING_BUTTON = (By.XPATH, './/a[@class=\'btn btn-dark post-delete-btn xs-btn\']')
