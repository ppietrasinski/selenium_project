import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestBase:

    app_url = 'http://www.kurs-selenium.pl/demo/'
    login_app_url = app_url + '/login'
    register_app_url = app_url + 'register'

    @pytest.fixture()
    def test_setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(20)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1370, 1080)
        self.driver.get(self.register_app_url)
        yield
        self.driver.quit()

# nie działa, trzeba to poprawić!