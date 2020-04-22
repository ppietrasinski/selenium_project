import pdb

class SearchPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_textbox = self.driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']")
        self.search_textbox_input = '//div[@id="select2-drop"]/div/input' #need to find this element after clicking search_textbox


    def fill_search_textbox_with_hotel_or_city_name(self, searched_name):
        self.search_textbox.click()
        self.search_textbox_input_active = self.driver.find_element_by_xpath(self.search_textbox_input)
        self.search_textbox_input_active.send_keys(searched_name)

# search_textbox = driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']")
# search_textbox.click()
#
# search_textbox_input = driver.find_element_by_xpath('//div[@id="select2-drop"]/div/input')
# search_textbox_input.send_keys('Madrid')