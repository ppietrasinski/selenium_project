from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
app_url = 'http://www.kurs-selenium.pl/demo/'
login_app_url = app_url + '/login'
register_app_url = app_url + '/register'


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.set_window_position(0, 0)
driver.set_window_size(1370, 1080)
driver.get(register_app_url)

first_name_textbox = driver.find_element_by_name('firstname')
first_name_textbox.send_keys('testing')
sleep(2)




self.driver.quit()