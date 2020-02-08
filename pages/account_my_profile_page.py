class AccountMyProfilePage:

    def __init__(self, driver):
        self.driver = driver
        self.email_field = self.driver.find_element_by_name("email")

    def get_email_data(self):
        return self.email_field.get_attribute('value')