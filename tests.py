from time import sleep

from selenium import webdriver
from MainPage import MainPage

class TestCases():

    def test_successfull_create_a_new_post(self, title, path_to_image, tags):
        main_page = MainPage(webdriver.Chrome())
        main_page.open('')
        popular_page = main_page.login('slaviktest@gmail.com', 'qwerty123')
        create_new_post_page = popular_page.click_new_post_button()
        create_new_post_page.enter_title(title)
        create_new_post_page.add_image(path_to_image)
        create_new_post_page.click_publish_close_button()
        create_new_post_page.enter_tags(tags)
        create_new_post_page.click_publish_button()

    def test_delete_post(self, post_name):
        main_page = MainPage(webdriver.Chrome())
        main_page.open('')
        poular_page = main_page.login('slaviktest@gmail.com', 'qwerty123')
        manage_posts_page = poular_page.open_manage_posts_page()
        manage_posts_page.select_post(post_name)
        manage_posts_page.click_delete_button()
        manage_posts_page.confirm_deleting_post()

    def test_edit_post(self, post_name):
        main_page = MainPage(webdriver.Chrome())
        main_page.open('')
        poular_page = main_page.login('slaviktest@gmail.com', 'qwerty123')
        manage_posts_page = poular_page.open_manage_posts_page()
        manage_posts_page.edit_post(post_name)
        sleep(10)

test_cases = TestCases()
#test_cases.test_successfull_create_a_new_post('New post',
#                                              '/home/slavik/Downloads/2014-05-09_Vinnitsa_14_Swiss_Tram.jpg', 'tags')
#test_cases.test_delete_post('New post')
test_cases.test_edit_post('Post')
