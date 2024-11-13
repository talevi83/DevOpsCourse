from unittest import case

from selenium import webdriver
from time import sleep

d = webdriver.Chrome()

def tipTest(billamt, peopleamt):
    # d.get("https://www.google.com")

    d.get("file:///Users/tallevi/tip_calc/index.html")
    sleep(5)
    d.find_element(by="id", value="billamt").send_keys(billamt)
    d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
    d.find_element(by="xpath", value='//*[@id="musicQuality"]/option[4]').click()
    d.find_element(by="id", value="peopleamt").send_keys(peopleamt)
    d.find_element(by="id", value="calculate").click()

    tipText = d.find_element(by="id", value="tip").text

    sleep(3)
    return tipText

    # d.quit()

class TestTipCalculator_SimpleTip(case.TestCase):
    def test_simple_tip_five_people(self):
        self.assertEqual(tipTest(100, 5), "40.60", "The tip in incorrect")

    def test_simple_tip_400_1_people(self):
        self.assertEqual(tipTest(200, 1), "403.00", "The tip in incorrect")




