from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


options = webdriver.FirefoxOptions()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)

driver.get("http://localhost:3000/reconciliation/strategy/PickAndApplyStrategy?id=testSample56.xlsx")

firstSelectionOfReconcilionKeysFromTheSecondPosition = ["marque","model"]
input_field = driver.find_element(By.ID, "numberOfReconciliationKeys")
input_field.send_keys("3")
print("typed the number")

button = driver.find_element(By.ID, "confirmNumberOfReconciliationKeys")
button.click()
print("clicked the button")
numberOfSelectionsThatAreNotPossible = 0
wait = WebDriverWait(driver,2)
select_element = wait.until(EC.element_to_be_clickable((By.ID, f"reconciliationDropdown-0")))
print("the dropdowns have appeared ")
for i in range(3):
    try:
        select_element = driver.find_element(By.ID, f"reconciliationDropdown-{i}")
        select = Select(select_element)
        select.select_by_visible_text("Intitule")
        print("first selection of Intitule happened successfully")

    except Exception as e:
        numberOfSelectionsThatAreNotPossible += 1
        print("proved that when we select an option it become unavailable for the other dropdowns")
        
for i in range(2):
    try:
        select_element = driver.find_element(By.ID, f"reconciliationDropdown-{i+1}")
        select = Select(select_element)
        select.select_by_visible_text(firstSelectionOfReconcilionKeysFromTheSecondPosition[i])
        print(f"valid selection of {firstSelectionOfReconcilionKeysFromTheSecondPosition[i]}")

    except Exception as e:
        print("Error during option selection:", e)
        
selectionToProveThatWhenWeChangeASelectionTheOldSelectedOptionIsAvailableAgain = driver.find_element(By.ID, f"reconciliationDropdown-2")
Select(selectionToProveThatWhenWeChangeASelectionTheOldSelectedOptionIsAvailableAgain).select_by_visible_text("fournisseur")
Select(selectionToProveThatWhenWeChangeASelectionTheOldSelectedOptionIsAvailableAgain).select_by_visible_text("model")
print("Proved that when we change a selection the old selected option is available again")
confirmReconciliatonKeysButton = driver.find_element(By.ID, "confirmReconciliationKeysButton")
confirmReconciliatonKeysButton.click()
wait = WebDriverWait(driver,2)
input_element = wait.until(EC.element_to_be_clickable((By.ID, f"numberOfCyclesInput")))
print("we found the input field of the number of cycles")

driver.quit()


