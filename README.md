#### **How to run tests.**

pip packages that have to be imported:
webdriver-manager ( pip install webdriver-manager )
pytest ( pip install pytest )
selenium ( pip install selenium )


#### **Running tests:**

All tests are created to be able to run in one moment or separately, one by one. To run them all at once, move 
in terminal to /project directory and type py.test to run separately 

To run only test from kurs-selenium.pl/demo/ move to tests/ and use py.test command. It runs all the tests in this directory.

To run only google tests move to tests_google/tests/ directory and use py.test command. 

pytest.ini file is configured to show logs info logs level


#### **Test scenerios:**

**TESTS of kurs-selenium.pl/demo/**
1. register_properly_test.py - check if user can register account with valid data without any issues
2. test_register_with_random_email_with_at.py - checks if usercan register account with valid email address without any issues

**TESTS of google search engine:**
1. test_search_term.py - three tested scenerio there:
    1.1. Check how much search results do we have.
    1.2. Checks if first 10 results are displayed on page one. 
    1.3. Checks if any pictures have been found