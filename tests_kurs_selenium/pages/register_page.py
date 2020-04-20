class RegisterPage:

    #PAGE OBJECT PATTERN

    def __init__(self, driver):
        self.driver = driver
        self.first_name_textbox = self.driver.find_element_by_name('firstname')
        self.last_name_textbox = self.driver.find_element_by_name('lastname')
        self.mobile_number_textbox = self.driver.find_element_by_name('phone')
        self.email_textbox = self.driver.find_element_by_name('email')
        self.password_textbox = self.driver.find_element_by_name('password')
        self.confirm_password_textbox = self.driver.find_element_by_name('confirmpassword')
        self.sign_up_button = self.driver.find_element_by_xpath("//div[@class='form-group']//button")

    def type_in_first_name(self, used_name=' '):
        self.first_name_textbox.send_keys(used_name)

    def type_in_last_name(self, used_last_name=' '):
        self.last_name_textbox.send_keys(used_last_name)

    def type_in_mobile_number(self, used_number=' '):
        self.mobile_number_textbox.send_keys(used_number)

    def type_in_email(self, used_email=' '):
        self.email_textbox.send_keys(used_email)

    def type_in_password(self, used_password=' '):
        self.password_textbox.send_keys(used_password)

    def type_in_confirm_password(self, used_confirmed_password=' '):
        self.confirm_password_textbox.send_keys(used_confirmed_password)

    def click_submit_button(self):
        self.sign_up_button.click()
