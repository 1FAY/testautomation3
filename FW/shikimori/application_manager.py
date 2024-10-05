from Data.settings import Settings
from FW.FW_Base import FWBase
from FW.driver_instance import DriverInstance
from FW.shikimori.main_page import MainPage
from FW.shikimori.search_page import SearchPage
from FW.shikimori.searched_page import SearchedPage


class ApplicationManager:

    def __init__(self):

        self.driver_instance = DriverInstance()
        self.fw_base = FWBase(self)
        self.settings = Settings()
        self.main_page = MainPage(self)
        self.search_page = SearchPage(self)
        self.searched_page = SearchedPage(self)
