from tests import base_test as test_base
from test_data import test_data as test_data
from pages import register_page as register_page

test_base.test_setup()
register_page.type_in_first_name(test_data.name)
register_page.type_in_last_name(test_data.last_name)
register_page.type_in_mobile_number(test_data.phone_number)
register_page.type_in_email(test_data.valid_email)
register_page.type_in_password(test_data.password)
register_page.type_in_confirm_password(test_data.password)

test_base.sleep_for(2)

# fn = driver.find_element_by_name('firstname')
# fn.send_keys(test_data.name)
#
# test_base.sleep_for(2)