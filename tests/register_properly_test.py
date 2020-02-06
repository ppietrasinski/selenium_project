import pytest
from tests.test_base import TestBase
from test_data import test_data
from pages.register_page import RegisterPage

@pytest.mark.usefixtures("test_setup")
class RegisterProperlyTest(TestBase):

    def register_properly_test(self, test_setup):
        register_page = RegisterPage(self.driver)
        register_page.type_in_first_name(test_data.name)
        register_page.type_in_last_name(test_data.last_name)
        register_page.type_in_mobile_number(test_data.phone_number)
        register_page.type_in_email(test_data.valid_email)
        register_page.type_in_password(test_data.password)
        register_page.type_in_confirm_password(test_data.password)
