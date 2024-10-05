from FW.mail.application_manager import ApplicationManager
from Test.test_base import TestBase

class TestMainPage(TestBase):
    APP = ApplicationManager()

    def setup_method(self):
        super().setup_method()
        self.APP.fw_base.go_to_page(self.APP.settings.page['MailRu'])

    def test_search(self):
        search_page = self.APP.main_page.search('НГИЭУ')
        assert search_page.check_site_in_page('Княгининский университет')
