from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

# Dictionary with login credentials
linkedin_dictionary = {
    "email": "YOUROWNEMAIL",
    "linkedin_password": "YOUROWNPASSWORD",
}

# Function to get the current timestamp
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Constants
LINKEDIN_LOGIN_URL = "https://www.linkedin.com/login"
FILTER_SEARCH_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3813109947&f_AL=true&f_E=2%2C3&f_JT=F%2CC&f_SB2=4&f_WT=2&keywords=python&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy=R"

# Setup Chrome WebDriver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Function to log in to LinkedIn
def login_to_linkedin(driver, email, password):
    try:
        driver.get(LINKEDIN_LOGIN_URL)
        driver.find_element(By.ID, "username").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password + Keys.ENTER)
        print(f"{get_timestamp()}: Successfully logged in.")
    except Exception as e:
        print(f"{get_timestamp()}: Error during login: {e}")

# Main execution
try:
    login_to_linkedin(driver, linkedin_dictionary["email"], linkedin_dictionary["linkedin_password"])
    driver.get(FILTER_SEARCH_URL)

    # Attempt to click on the first pre-easy apply link
    pre_easy_apply_links = driver.find_elements(By.CSS_SELECTOR, "li.job-card-container__apply-method.job-card-container__footer-item.inline-flex.align-items-center")
    for index, link in enumerate(pre_easy_apply_links):
        try:
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            link.click()
            print(f"{get_timestamp()}: Clicked on the pre-easy apply link #{index+1}.")
            time.sleep(2)  # Time to wait for any dynamic content to load
        except Exception as e:
            print(f"{get_timestamp()}: Could not find or click on the pre-easy apply link #{index+1}: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Reminder to manually close the browser or add driver.quit() where appropriate.
