import pytest
from tests.test_base import TestBase
from test_data import test_data
from pages.register_page import RegisterPage
from pages.account_my_profile_page import AccountMyProfilePage
import time
from pages.account_page import AccountPage
import pdb

@pytest.mark.usefixtures("test_setup")
class TestRegisterWithRandomEmailWithAt(TestBase):

    def test_register_properly(self, test_setup):
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
        print(t2 - t1) # result of testing how long login proces takes

        assert account_page.get_hi_name_text() == f"Hi, {used_name} {used_last_name}"

        account_page.click_my_profile_button()
        my_profile = AccountMyProfilePage(self.driver)
        email_on_my_profile = my_profile.get_email_data()

        print(invalid_email + ' - email wpisany przez program')
        print(email_on_my_profile + ' - email ppbramy z my profile')

        # pdb.set_trace()

        assert email_on_my_profile == invalid_email