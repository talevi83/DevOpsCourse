import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

class TestTipCalculator(unittest.TestCase):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service('/usr/local/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    @classmethod
    def setUpClass(cls):
        # Initialize the Chrome WebDriver
        cls.driver = webdriver.Chrome()
        # cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # Quit the WebDriver
        cls.driver.quit()

    def tip_test(self, bill_amt, people_amt, expected_tip):
        # Construct the file URL
        file_path = os.path.abspath("/Users/tallevi/tip_calc/index.html")
        file_url = f"file://{file_path}"

        # Navigate to the local HTML file
        print(f"Navigating to {file_url}")
        self.driver.get(file_url)
        sleep(2)  # Wait for the page to load

        # Interact with the web elements
        self.driver.find_element(By.ID, "billamt").send_keys(str(bill_amt))
        self.driver.find_element(By.XPATH, '//*[@id="serviceQual"]/option[3]').click()
        self.driver.find_element(By.XPATH, '//*[@id="musicQuality"]/option[4]').click()
        self.driver.find_element(By.ID, "peopleamt").send_keys(str(people_amt))
        self.driver.find_element(By.ID, "calculate").click()

        sleep(1)  # Wait for calculation

        # Retrieve the tip text
        tip_text = self.driver.find_element(By.ID, "tip").text
        print(f"Calculated Tip: {tip_text}")

        # Assert the expected tip
        self.assertEqual(tip_text, expected_tip, f"Expected tip {expected_tip}, but got {tip_text}")

    def test_simple_tip_five_people(self):
        self.tip_test(100, 5, "40.60")

    def test_simple_tip_one_person(self):
        self.tip_test(200, 1, "403.00")

if __name__ == "__main__":
    unittest.main()
