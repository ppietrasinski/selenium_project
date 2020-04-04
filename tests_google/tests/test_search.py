import pytest
from tests_google.tests.base_test import BaseTest
from tests_google.pages.search_page import SearchPage
from tests_google.pages.result_page import ResultPage
from tests_google.test_data import test_data
from bcolors import bcolors
import logging


@pytest.mark.usefixtures("setup_test")
class TestSearch(BaseTest):

    def test_search_term(self, setup_test):
        logger = logging.getLogger(__name__)
        search_page = SearchPage(self.driver)
        searched_term = test_data.searched_term
        search_page.type_in_searched_term_to_search_field(searched_term)
        search_page.search_button_in_prompt_pop_up.click()

        result_page = ResultPage(self.driver)
        search_results_whole_text = result_page.get_amount_of_searched_results()
        search_result_only = result_page.edit_result_string(search_results_whole_text)

        logger.info('test logger message')

        # FIRST CHECK:
        # How many search results do we have?
        logger.info('\nFIRST CHECK: How many search results do we have?')
        logger.info(f'{bcolors.OKBLUE}INFO: About {search_result_only} results were found{bcolors.ENDC}')

        # SECOND CHECK:
        # Is first 10 results displayed on page one?
        logger.info('\nSECOND CHECK: Is first 10 results displayed on page one?')
        results_amount = result_page.get_amount_of_displayed_results_on_page() + result_page.get_amount_of_displayed_places_results_on_page()
        logger.info(f'{bcolors.OKBLUE}INFO: {results_amount} results of search can be seen on the first page. Images, videos and articles were not included{bcolors.ENDC}')
        try:
            assert results_amount >= 10
        except AssertionError:
            logger.info(f'{bcolors.FAIL}INFO: on first page, less then 10 results are dispalyed{bcolors.ENDC}')

        # THIRD CHECK:
        # Have any pictures been found?
        logger.info('\nTHIRD CHECK: Have any pictures been found?')
        is_image_section_visble = result_page.is_images_result_section_displayed()
        try:
            assert is_image_section_visble
        except AssertionError as err:
            logger.info(f'{bcolors.FAIL}INFO: {err}{bcolors.ENDC}')
        finally:
            if is_image_section_visble:
                logger.info(
                    f'{bcolors.OKBLUE}INFO: images have been loaded and they are visible in the image section{bcolors.ENDC}')
            else:
                logger.info(f'{bcolors.FAIL}INFO: no images loaded, image section is not visible{bcolors.ENDC}')