
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

chrome_options.add_argument('--headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

driver.get('https://letcode.in/edit')
driver.maximize_window()

driver.implicitly_wait(30)

driver.find_element(By.ID, "fullName").send_keys('Chunnu Madam')
driver.find_element(By.ID, "clearMe").clear()
value = driver.find_element(By.ID, "dontwrite").get_property("value")
print(f"Text box value is : {value}")

title = driver.title

print(f"Title of page is : {title}")

assert title == "Interact with Input fields"

driver.quit()

