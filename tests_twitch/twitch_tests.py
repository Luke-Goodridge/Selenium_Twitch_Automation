from selenium import webdriver
from Pages.home_page import TwitchHomePage
from Pages.directory.directories_main import TwitchDirectoriesMain


# Chrome

CHROME_PATH = r"C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(executable_path=CHROME_PATH)
homePage = TwitchHomePage(driver)
browsePage = TwitchDirectoriesMain(driver)
browsePage.goto()

# ======== Tests =========

# Test recommended
browsePage.change_view_mode(0)
browsePage.test_print_viewcount_details()
# Test viewers high to low
browsePage.change_view_mode(1)
browsePage.test_print_viewcount_details()

# browsePage.test_all_directories()
print("CHROME TESTS COMPLETE.")

# Firefox

# options = Options()
# options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
# MOZILLA_PATH = r"C:/Program Files (x86)/geckodriver.exe"
# driver = webdriver.Firefox(executable_path=MOZILLA_PATH, options=options)
# homePage_F = TwitchHomePage(driver)
# browsePage_F = TwitchDirectoriesPage(driver)
# browsePage_F.goto_directories_hub()
# browsePage_F.test_all_directories()
# print("FIREFOX TESTS COMPLETE.")
