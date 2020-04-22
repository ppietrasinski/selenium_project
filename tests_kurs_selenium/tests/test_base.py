import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging


class BaseTest:

    app_url = 'http://www.kurs-selenium.pl/demo'
    login_app_url = '/login'
    register_app_url = '/register'
    homepage_url = '/'

    @pytest.fixture()
    def setup(self):
        self.logger = logging.getLogger(__name__)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.get()
        self.driver.implicitly_wait(20)
        self.driver.set_window_position(0, 0)
        self.driver.set_window_size(1370, 1080)
        self.driver.get(self.app_url)
        yield
        self.driver.quit()

# nie działa, trzeba to poprawić!

