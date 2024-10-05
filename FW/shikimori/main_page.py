from selenium.webdriver.common.by import By

from FW.any_page import AnyPage


class Locator:
    input_search = (By.XPATH, "//div[@class='global-search']/label/input")
    

class MainPage(AnyPage):
    def search(self, text):
        self.send_keys(locator=Locator.input_search, text=text)
        return self.manager.search_page


