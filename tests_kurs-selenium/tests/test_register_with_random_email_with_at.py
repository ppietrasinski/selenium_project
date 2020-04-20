import pytest
from tests.test_base import BaseTest
from test_data import test_data
from pages.register_page import RegisterPage
from pages.account_my_profile_page import AccountMyProfilePage
import time
from pages.account_page import AccountPage
import logging


@pytest.mark.usefixtures("setup")
class TestRegisterWithRandomEmailWithAt(BaseTest):

    def test_register_properly(self, setup):
        logger = logging.getLogger(__name__)

        register_page = RegisterPage(self.driver)
        used_name = test_data.name
        used_last_name = test_data.last_name

        register_page.type_in_first_name(used_name)
        register_page.type_in_last_name(used_last_name)
        register_page.type_in_mobile_number(test_data.phone_number)


        #zmień generowanie się invalid email tak aby były w nim tylko małe liczby
        invalid_email = test_data.generate_invalid_email_valid_format()
        register_page.type_in_email(invalid_email)

        register_page.type_in_password(test_data.password)
        register_page.type_in_confirm_password(test_data.password)

        t1 = time.time() # used to check how long logging in process takes

        register_page.click_submit_button()
        account_page = AccountPage(self.driver)

        t2 = time.time()
        test_data.login_time(t2, t1) # result of testing how long login proces takes

        assert account_page.get_hi_name_text() == f"Hi, {used_name} {used_last_name}"

        account_page.click_my_profile_button()
        my_profile = AccountMyProfilePage(self.driver)
        email_on_my_profile = my_profile.get_email_data()

        logger.info(invalid_email + ' - email used by program')
        logger.info(email_on_my_profile + ' - email get from profile page')

        assert email_on_my_profile == invalid_email
        logger.info('user can register new account with valid email address without any issues')