from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://github.com/login")
input("👉 Please log in to GitHub and press Enter here to continue...")

project_url = "https://github.com/orgs/Neophyte-ai/projects/28"
driver.get(project_url)

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='row']")))

# Scroll to load more tasks if necessary
for _ in range(7):  # Adjust number of scrolls if needed
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Scrape all task rows
tasks = driver.find_elements(By.CSS_SELECTOR, "div[role='row']")
print(f"\n🗂 Total Tasks Found: {len(tasks)}\n")

for task in tasks:
    try:
        columns = task.find_elements(By.CSS_SELECTOR, "div[role='gridcell']")
        if len(columns) >= 8:
            sl_no = columns[0].text
            title = columns[1].text
            assignees = columns[2].text
            status = columns[3].text
            parent = columns[4].text
            start_date = columns[5].text
            end_date = columns[6].text

            print(f"SL No: {sl_no}")
            print(f"Title: {title}")
            print(f"Assignees: {assignees}")
            print(f"Status: {status}")
            print(f"Parent Issue: {parent}")
            print(f"Start Date: {start_date}")
            print(f"End Date: {end_date}")
            print("-" * 80)
    except Exception as e:
        print("⚠️ Error parsing row:", e)

driver.quit()
