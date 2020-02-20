import pytest
from tests.test_base import BaseTest
from test_data import test_data
from pages.register_page import RegisterPage
import time
from pages.account_page import AccountPage
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestRegisterProperly(BaseTest):

    def test_register_properly(self, setup):
        register_page = RegisterPage(self.driver)
        used_name = test_data.name
        used_last_name = test_data.last_name
        register_page.type_in_first_name(used_name)
        register_page.type_in_last_name(used_last_name)
        register_page.type_in_mobile_number(test_data.phone_number)
        register_page.type_in_email(test_data.generate_valid_email(used_name, used_last_name))
        register_page.type_in_password(test_data.password)
        register_page.type_in_confirm_password(test_data.password)

        t1 = time.time()  # used to check how long logging in process takes

        register_page.click_submit_button()

        account_page = AccountPage(self.driver)

        t2 = time.time()
        test_data.login_time(t2, t1)

        assert account_page.get_hi_name_text() == f"Hi, {used_name} {used_last_name}"