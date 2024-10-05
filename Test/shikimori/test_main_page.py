import time
from FW.shikimori.application_manager import ApplicationManager
from Test.test_base import TestBase

class TestMainPage(TestBase):
    APP = ApplicationManager()
    searchText = 'Наруто'

    def setup_method(self):
        super().setup_method()
        self.APP.fw_base.go_to_page(self.APP.settings.page['ShikimoriOne'])

    def test_search(self):
        search_page = self.APP.main_page.search(self.searchText)
        assert(search_page.check_search_result_in_page(self.searchText))
    
    def test_open_searched_page(self):
        search_page = self.APP.main_page.search(self.searchText)
        searched_page = search_page.open_search_result(self.searchText)
        searched_page.scroll_to_character(self.searchText, offset_y=10)
        searched_page.hover_on_character_by_name(self.searchText)
        time.sleep(3)
        searched_page.open_image()
        time.sleep(1)
        searched_page.next_image()
        time.sleep(1)
        searched_page.next_image()
        time.sleep(1)
        searched_page.next_image()
        time.sleep(1)
        searched_page.close_image()
        searched_page.scroll_to_logo()
        searched_page.click_on_logo()
        search_page = self.APP.main_page.search(self.searchText)
        assert(search_page.check_search_result_in_page(self.searchText))