from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TwitchDirectoryPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 2)

    # Change view on the directories page, e.g recommended, by viewcount etc.
    def change_view_mode(self, mode):
        view_status_dropdown = self._driver.find_element(By.XPATH, "//button[@data-a-target='browse-sort-menu']")
        view_status_dropdown.click()
        view_modes = self._driver.find_elements(By.CLASS_NAME, 'dgcGVJ')
        if mode == 0:
            view_modes[0].click()
        else:
            view_modes[1].click()
