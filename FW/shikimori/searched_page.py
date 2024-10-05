from selenium.webdriver.common.by import By

from FW.any_page import AnyPage

class Locator:
    logo_anchor = (By.XPATH, "//div[@class='logo']")
    img_anchor = (By.XPATH, "//div[@class='c-screenshots']//img")
    img_nextbtn_anchor = (By.XPATH, "//button[contains(@class, 'mfp-arrow-right')]")
    img_closebtn_anchor = (By.XPATH, "//button[contains(@class, 'mfp-close')]")

class SearchedPage(AnyPage):
    def scroll_to_logo(self):
        return self.scroll_to_element(locator=Locator.logo_anchor)
    
    def click_on_logo(self):
        self.click_element(locator=Locator.logo_anchor)
        return self.manager.main_page
    
    def scroll_to_character(self, text, offset_x=0, offset_y=0):
        return self.scroll_to_element(
            locator=(By.XPATH, f"//div[@class='cc-characters']//span[@class='name-ru' and contains(text(), '{text}')]"), 
            offset_x=offset_x,
            offset_y=offset_y
        )

    def hover_on_character_by_name(self, text):
        return self.hover_element(locator=(By.XPATH, f"//div[@class='cc-characters']//span[@class='name-ru' and contains(text(), '{text}')]"))
    
    def open_image(self):
        return self.click_element(locator=Locator.img_anchor)
    
    def next_image(self):
        return self.click_element(locator=Locator.img_nextbtn_anchor)
    
    def close_image(self):
        return self.click_element(locator=Locator.img_closebtn_anchor)