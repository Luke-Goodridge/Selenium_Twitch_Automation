from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .home_page import test_counter_print


class TwitchDirectoriesPage:
    def __init__(self, driver):
        self._driver = driver
        self.wait = WebDriverWait(self._driver, 2)

    # Return to the directories' page via the "browse_button"
    def goto_directories_hub(self):
        current_page = self._driver.current_url
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-a-target='browse-link']"))).click()
        # Verify that we are at the browse page
        if self._driver.current_url == "https://www.twitch.tv/directory":
            test_counter_print(f"Successfully Navigated to directories page from {current_page}.", True)
        else:
            test_counter_print(f"Navigation to directories page.", False)

    # Ensures all directories can be navigated to
    def test_all_directories(self):
        # Lookup how many directories there should be on the page
        directory_search_web_elements = self._driver.find_elements_by_class_name(
            'vertical-selector__title--big--creative')
        directories_lookup = []
        for link in directory_search_web_elements:
            directories_lookup.append(f"{link.text}")
        test_directories = ["gaming", "irl", "esports", "creative", "TEST_FAILURE_1", "Musich"]
        # Compare the 2 lists, making sure we have the same amount to test
        if len(directories_lookup) != len(test_directories):
            # Output the 2 lists if they are different lengths, something in script needs updating
            test_counter_print(f"Scripted directories don't match the amount on the directories page. "
                               f"\n{str(len(directories_lookup))} directories on page. {str(directories_lookup)}"
                               f"\n{str(len(test_directories))} scripted to test {str(test_directories)}", False)
        for directory in test_directories:
            # Find the link to each directory
            try:
                self.wait.until(EC.presence_of_element_located(
                    (By.XPATH, f'//a[contains(@href,"/directory/{directory}")]'))).click()
            # If there is no link, the data must be wrong, normally this would stack trace etc, but for this purpose 
            # its fine to fail the test 
            except TimeoutException as ex:
                test_counter_print(f"Navigation button to {directory} directory page could not be found", False)
            # Check to make sure the button sent us to the right page
            if self._driver.current_url == f"https://www.twitch.tv/directory/{directory}":
                test_counter_print(f"Successfully Navigated to {directory} directory page.", True)
            else:
                test_counter_print(f"Could not navigate to {directory} directory page from the {directory} button",
                                   False)
            # Return to the directories home page
            self.goto_directories_hub()
        self._driver.quit()
