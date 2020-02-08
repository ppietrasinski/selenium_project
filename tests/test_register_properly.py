import pytest
from tests.test_base import TestBase
from test_data import test_data
from pages.register_page import RegisterPage
import time
from pages.account_page import AccountPage
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("test_setup")
class TestRegisterProperly(TestBase):

    def test_register_properly(self, test_setup):
        register_page = RegisterPage(self.driver)
        used_name = test_data.name
        used_last_name = test_data.last_name
        register_page.type_in_first_name(used_name)
        register_page.type_in_last_name(used_last_name)
        register_page.type_in_mobile_number(test_data.phone_number)
        register_page.type_in_email(test_data.valid_email)
        register_page.type_in_password(test_data.password)
        register_page.type_in_confirm_password(test_data.password)

        t1 = time.time()

        register_page.click_submit_button()

        account_page = AccountPage(self.driver)
        assert account_page.get_hi_name_text() == f"Hi, {used_name} {used_last_name}"

        t2 = time.time()
        print(t2 - t1)
