from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def test_menu_functionality(driver):
    """
    Tests the menu functionality: opening, closing, and clicking links.
    """
    # Open the menu
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    # Wait for the menu to be visible
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link")))

    # Click on "About" link
    about_link = driver.find_element(By.ID, "about_sidebar_link")
    about_link.click()

    #Verify that the page has changed
    assert "saucelabs.com" in driver.current_url

    driver.back()

    # Open the menu again
    menu_button = driver.find_element(By.ID, "react-burger-menu-btn")
    menu_button.click()

    # Wait for the menu to be visible again
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "inventory_sidebar_link")))
   
    # Close the menu
    close_button = driver.find_element(By.ID, "react-burger-cross-btn")
    close_button.click()

    # Wait for the menu to be closed
    wait.until(EC.invisibility_of_element_located((By.ID, "inventory_sidebar_link")))

def test_add_to_cart(driver):
    """
    Tests the "Add to cart" functionality of the first item.
    """
    # Find the add to cart button for the first item
    add_to_cart_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_to_cart_button.click()

    # Optional: Assert that the button text changes or the cart icon updates (if present)
    # Example:
    # assert driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").text == "Remove"
    
def test_sort_products(driver):
    """
    Tests the product sorting functionality.
    """
    # Find the product sort dropdown
    sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")

    # Select "Price (high to low)"
    select = Select(sort_dropdown)
    select.select_by_value("hilo")

    # Optional: Assert that the products are sorted correctly.
    # This will require fetching product prices and comparing them.
    
    # Select "Name (Z to A)"
    select = Select(sort_dropdown)
    select.select_by_value("za")
    
    # Optional: Assert that the products are sorted correctly.
    # This will require fetching product names and comparing them.

if __name__ == '__main__':
    # Set up the webdriver (replace with your desired browser)
    driver = webdriver.Chrome()

    # Navigate to the page
    driver.get("file:///path/to/your/html/file.html") #Replace with actual path

    # Run the tests
    test_menu_functionality(driver)
    test_add_to_cart(driver)
    test_sort_products(driver)

    # Close the browser
    driver.quit() 