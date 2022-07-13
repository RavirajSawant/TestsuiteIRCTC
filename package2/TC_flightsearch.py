import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Test_irctc(unittest.TestCase):
    '''flight search in IRCTC using unittest framework'''

    def test_opirctc(self):

        # -----------launch webdriver and irctc website----------------

        self.driver = webdriver.Chrome(executable_path="C:/Users/Dell/chromedriver_win32/chromedriver.exe")
        driver = self.driver
        driver.get("https://www.irctc.co.in/nget/train-search")

        title = driver.title
        self.assertEqual(title, "IRCTC Next Generation eTicketing System")
        window_before = driver.window_handles[0]
        driver.find_element(by=By.XPATH, value="//button[contains(text(),'OK')]").click()
        driver.find_element(by=By.XPATH, value="//app-header/div[1]/div[2]/a[1]/i[1]").click()
        driver.find_element(by=By.XPATH,
                            value="//app-header/div[@id='slide-menu']/p-sidebar[1]/div[1]/nav[1]/ul[1]/li[5]/a[1]/label[1]").click()
        time.sleep(3)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        global url
        url = driver.current_url
        time.sleep(3)

    def test_search_flight(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/Dell/chromedriver_win32/chromedriver.exe")
        driver = self.driver
        time.sleep(2)
        driver.get("https://www.air.irctc.co.in/")
        self.assertEqual(driver.title, "Air Ticket Booking | Book Flight Tickets | Cheap Air Fare - IRCTC Air")

        # -----selecting one way or round ticket-------

        driver.find_element(by=By.XPATH, value="//label[contains(text(),'One Way')]").click()

        # -----  Selecting origin and destination--------

        driver.find_element(by=By.XPATH, value="//input [@name= 'From']").click()
        # driver.find_element(by=By.XPATH, value="//input [@name= 'From']").send_keys("DEL")
        for down in range(2):
            driver.find_element(by=By.XPATH, value="//input [@name= 'From']").send_keys(Keys.DOWN)
        driver.find_element(by=By.XPATH, value="//input [@name= 'From']").send_keys(Keys.ENTER)

        driver.find_element(by=By.XPATH, value="//input[@id='stationTo']").click()
        # driver.find_element(by=By.XPATH, value="//input[@id='stationTo']").send_keys("MAA")
        for down1 in range(4):
            driver.find_element(by=By.XPATH, value="//input[@id='stationTo']").send_keys(Keys.DOWN)
        driver.find_element(by=By.XPATH, value="//input[@id='stationTo']").send_keys(Keys.ENTER)

        # -------  Selecting date-------

        driver.find_element(by=By.XPATH, value="//input[@id='originDate']").click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value="//tbody/tr[4]/td[6]/span[1]").click()

        # ---------------Selecting number of seats, class------------------

        driver.find_element(by=By.XPATH, value="//input[@id='noOfpaxEtc']").click()
        driver.find_element(by=By.XPATH, value="//div[@id='TravellerEconomydropdown']").click()
        time.sleep(2)
        type = Select(driver.find_element(by=By.XPATH, value="//select[@id='travelClass']"))
        type.select_by_index(1)
        time.sleep(2)

        # -----Click on search button

        driver.find_element(by=By.XPATH,
                            value="//body/app-root[1]/app-index[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[6]/button[1]").click()

        # ------ Taking screenshots---------

        time.sleep(15)

        #driver.save_screenshot("C:\\Users\\Umar\\Documents\\Flight_Search")
        driver.get_screenshot_as_file('flight1.png')
        driver.execute_script("window.scrollBy(0,750)", " ")
        time.sleep(3)
       ## driver.save_screenshot("C:\\Users\\Umar\\Documents\\Flight_Search")
        driver.get_screenshot_as_file('flight2.png')
        driver.execute_script("window.scrollBy(750,1500)", " ")
        time.sleep(3)
        #driver.save_screenshot("C:\\Users\\Umar\\Documents\\Flight_Search")
        driver.get_screenshot_as_file('flight3.png')
        driver.close()
        print("Flight searched successfully")









if __name__ == "__main__":
    unittest.main()