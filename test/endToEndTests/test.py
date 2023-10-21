from selenium import webdriver

driver = webdriver.Firefox()

# Open a website
driver.get("https://www.example.com")

# Perform some actions
search_box = driver.find_element_by_name("q")
search_box.send_keys("Selenium")
search_box.submit()

# Wait for a few seconds
import time
time.sleep(5)

# Close the browser
driver.quit()

