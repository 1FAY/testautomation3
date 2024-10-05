from selenium.webdriver.common.by import By

from FW.any_page import AnyPage


class SearchPage(AnyPage):
    def check_search_result_in_page(self, text):
        return self.check_element_in_page(locator=(By.XPATH, f"//div[@class='name']/span[@class='b-link' and text()='{text}']"))
    
    def open_search_result(self, text):
        self.click_element(locator=(By.XPATH, f"//div[@class='name']/span[@class='b-link' and text()='{text}']"))
        return self.manager.searched_page
