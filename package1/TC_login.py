import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class loginTest(unittest.TestCase):
    def test_opirctca(self):
        # -----------launch webdriver and irctc website----------------

        self.driver = webdriver.Chrome(executable_path="C:/Users/Dell/chromedriver_win32/chromedriver.exe")
        driver = self.driver
        driver.get("https://www.irctc.co.in/nget/train-search")

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

        driver.find_element(by=By.XPATH,
                            value="/html/body/app-root/app-header/header/nav/div/div[3]/div/ul/li[2]/a").click()
        driver.find_element(by=By.NAME, value="userId").send_keys("shrinisen")
        driver.find_element(by=By.NAME, value="password").send_keys("Sr23ss23@")
        driver.find_element(by=By.XPATH, value="//button[contains(text(),'Login')]").click()
        title1 = driver.title
        assert "Air Ticket Booking | Book Flight Tickets | Cheap Air Fare - IRCTC Air" in title1
        driver.close()
        print("login done")


if __name__ == "__main__":
    unittest.main()

