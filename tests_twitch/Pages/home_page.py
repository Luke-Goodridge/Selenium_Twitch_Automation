from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TwitchHomePage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 2)
        self._driver.get("Https://twitch.tv")

    # Returns to the home page from wherever
    def goto_home(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-a-target='home-link']"))).click()
        if self._driver.current_url == "https://www.twitch.tv/":
            test_counter_print(f"Successfully Navigated to home page from home button.", True)
        else:
            test_counter_print(f"Navigation to home page, URL {self._driver.current_url} incorrect for home.", False)

    # If we need to accept cookies
    def accept_cookies(self):
        cookies_accept_button_path = "//*[@data-a-target='consent-banner-accept']"
        # Find and click the accept button
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@data-a-target='consent-banner-accept']"))).click()
        if self._driver.find_element(By.XPATH, cookies_accept_button_path):
            test_counter_print("Cookies Cleared", True)
        else:
            test_counter_print("Cookies not cleared", False)


global test_counter
test_counter = 0


# Function to simply format tests after being ran
def test_counter_print(text, passed):
    global test_counter
    test_counter += 1
    test_index = str(test_counter)
    if test_counter < 10:
        test_index = "0" + test_index
    if not passed:
        test_index = str("\033[91m FAIL - \033[0m") + test_index
    else:
        test_index = "\033[92m PASS - \033[0m" + test_index
    print(f"{str(test_index)} {text}")
    # If you wish to only see fails, simply comment out the else, and put the print in the IF above
