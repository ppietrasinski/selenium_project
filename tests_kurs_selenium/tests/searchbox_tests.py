import pytest
from tests_kurs_selenium.tests.test_base import BaseTest
from tests_kurs_selenium.pages.search_page import SearchPage
import time


@pytest.mark.usefixtures("setup")
class TestSearchbox(BaseTest):

    # @pytest.fixture()
    # def before_test(self, setup):
    #     self.driver.get(BaseTest.app_url + BaseTest.homepage_url)

    def test_search_properly(self, setup):
        self.logger.info("test")
        search_page = SearchPage(self.driver)
        search_page.fill_search_textbox_with_hotel_or_city_name('Madrid')
        time.sleep(2)

