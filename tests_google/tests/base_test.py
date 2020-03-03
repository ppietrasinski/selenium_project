import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BaseTest:

    app_url = 'https://www.google.com/'

    @pytest.fixture()
    def setup_test(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(self.app_url)
        yield
        self.driver.quit()

