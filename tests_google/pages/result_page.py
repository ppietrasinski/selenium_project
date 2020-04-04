import re

class ResultPage:

    def __init__(self, driver):
        self.driver = driver
        self.amount_of_result_tiles = self.driver.find_elements_by_xpath("//div[@class='g']")
        self.amount_of_result_places = self.driver.find_elements_by_xpath("//div[@class='cXedhc']")
        self.images_result_section = self.driver.find_elements_by_xpath("//div[@class='LnbJhc']")
        self.results_quantity_displayer = self.driver.find_element_by_id('result-stats')

    def get_amount_of_searched_results(self):
        return self.results_quantity_displayer.text

    def get_amount_of_displayed_results_on_page(self):
        return len(self.amount_of_result_tiles)

    def get_amount_of_displayed_places_results_on_page(self):
        return len(self.amount_of_result_places)

    def is_images_result_section_displayed(self):
        if not self.images_result_section:
            return False
        else:
            return True

        #method is checking if element actually exist on page or if it's not

    def edit_result_string(self, string):
        edited_string_list = (re.sub("[(].*?[)]", "", string).split(' '))
        if edited_string_list[0] == 'About':
            return(int(''.join(edited_string_list[1].split(','))))
        elif edited_string_list[0] == 'Około':
            return(int(''.join(edited_string_list[1:4])))
        # method used to split string and make the result independent of the language in which the search engine
        # will be activated