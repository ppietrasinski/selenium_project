import pytest
from ..tests.base_test import BaseTest
from ..pages.search_page import SearchPage
from ..pages.result_page import ResultPage
from ..test_data import test_data
from bcolors import bcolors
import logging

@pytest.mark.usefixtures("setup_test")
class TestSearch(BaseTest):
    logger = logging.getLogger(__name__)

    @pytest.fixture()
    def before_test(self, setup_test):
        search_page = SearchPage(self.driver)
        searched_term = test_data.searched_term
        search_page.type_in_searched_term_to_search_field(searched_term)
        search_page.search_button_in_prompt_pop_up.click()


        # FIRST CHECK:
        # How many search results do we have?
    def test_amount_of_search_results(self, before_test):
        result_page = ResultPage(self.driver)
        search_results_whole_text = result_page.get_amount_of_searched_results()
        search_result_only = result_page.edit_result_string(search_results_whole_text)
        self.logger.info('\nFIRST CHECK: How many search results do we have?')
        self.logger.info(f'{bcolors.OKBLUE}INFO: About {search_result_only} results were found{bcolors.ENDC}')


        # SECOND CHECK:
        # Are first 10 results displayed on page one?
    def test_first_10_results(self, before_test):
        self.logger.info('\nSECOND CHECK: Is first 10 results displayed on page one?')
        result_page = ResultPage(self.driver)
        results_amount = result_page.get_amount_of_displayed_results_on_page() + result_page.get_amount_of_displayed_places_results_on_page()
        self.logger.info(f'{bcolors.OKBLUE}INFO: {results_amount} results of search can be seen on the first page. Images, videos and articles were not included{bcolors.ENDC}')
        try:
            assert results_amount >= 10
        except AssertionError:
            self.logger.info(f'{bcolors.FAIL}INFO: on first page, less then 10 results are dispalyed{bcolors.ENDC}')


        # THIRD CHECK:
        # Have many pictures been found?
    def test_if_pictures_founded(self, before_test):
        self.logger.info('\nTHIRD CHECK: Have any pictures been found?')
        result_page = ResultPage(self.driver)
        is_image_section_visble = result_page.is_images_result_section_displayed()
        try:
            assert is_image_section_visble
        except AssertionError as err:
            self.logger.info(f'{bcolors.FAIL}INFO: {err}{bcolors.ENDC}')
        finally:
            if is_image_section_visble:
                self.logger.info(
                    f'{bcolors.OKBLUE}INFO: images have been loaded and they are visible in the image section{bcolors.ENDC}')
            else:
                self.logger.info(f'{bcolors.FAIL}INFO: no images loaded, image section is not visible{bcolors.ENDC}')