from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login_and_get_html(platform_url, username, password):
    # Initialize the Selenium WebDriver
    driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in your PATH
    driver.get(platform_url)

    # Find the username and password fields and log in
    driver.find_element(By.NAME, 'user-name').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password + Keys.RETURN)

    # Wait for the page to load and retrieve the HTML source
    html_source = driver.page_source

    # Close the driver
    driver.quit()

    return html_source
 