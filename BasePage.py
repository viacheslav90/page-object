from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver, url='https://photoblog.steelkiwi.com/'):
        self.base_url = url
        self.driver = driver
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 5)
        self.timeout = 30

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

