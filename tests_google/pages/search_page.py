
class SearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_field = self.driver.find_element_by_name('q')
        self.search_button = self.driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']/center/input[1]")
        self.search_button_in_prompt_pop_up = self.driver.find_element_by_xpath("//div[@class='tfB0Bf']/center/input[1]")
        self.google_hero_logo = self.driver.find_element_by_id('hplogo')

    def type_in_searched_term_to_search_field(self, searched_term):
        self.search_field.send_keys(searched_term)

    def click_search_button_in_prompt_pop_up(self):
        self.search_button_in_prompt_pop_up.click()

