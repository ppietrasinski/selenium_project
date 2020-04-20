'''This is testing commentary'''

from selenium import webdriver

class AccountPage:

    def __init__(self, driver):
        self.driver = driver
        self.hi_name_text = self.driver.find_element_by_xpath("//h3[@class='RTL']")
        self.my_profile_button = self.driver.find_element_by_xpath("//span[@class='profile-icon']")

    def get_hi_name_text(self):
        return self.hi_name_text.text

    def click_my_profile_button(self):
        self.my_profile_button.click()