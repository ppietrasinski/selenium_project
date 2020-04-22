from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

app_url = 'http://www.kurs-selenium.pl/demo'
login_app_url = '/login'
register_app_url = '/register'
homepage_url = '/'



driver = webdriver.Chrome(ChromeDriverManager().install())
# self.driver = webdriver.get()

driver.set_window_position(0, 0)
driver.set_window_size(1370, 1080)
driver.get(app_url)

search_textbox = driver.find_element_by_xpath("//span[text()='Search by Hotel or City Name']")
search_textbox.click()

search_textbox_input = driver.find_element_by_xpath('//div[@id="select2-drop"]/div/input')
search_textbox_input.send_keys('Madrid')

time.sleep(2)



#select2-drop > div > input