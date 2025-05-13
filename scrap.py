from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient
import time

# MongoDB Setup
client = MongoClient("mongodb://localhost:27017/")  # Or use Atlas URL
db = client["github_projects"]
collection = db["tasks"]

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://github.com/login")
input("🔐 Log in to GitHub manually, then press Enter to continue...")

driver.get("https://github.com/orgs/Neophyte-ai/projects/28")  # Replace with your real URL

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='row']")))

for _ in range(7):  # Adjust number of scrolls if needed
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)


tasks = driver.find_elements(By.CSS_SELECTOR, "div[role='row']")

for task in tasks:
    try:
        columns = task.find_elements(By.CSS_SELECTOR, "div[role='gridcell']")
        if len(columns) >= 7:
            task_data = {
                "sl_no": columns[0].text,
                "title": columns[1].text,
                "assignees": columns[2].text,
                "status": columns[3].text,
                "parent_issue": columns[4].text,
                "start_date": columns[5].text,
                "end_date": columns[6].text
            }

            # Insert into MongoDB
            collection.insert_one(task_data)
            print("✅ Inserted:", task_data["title"])
    except Exception as e:
        print("⚠️ Skipped a row due to error:", e)

driver.quit()
