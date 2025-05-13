This project is a **web scraper** that uses **Selenium** to extract task information from a **GitHub Project Board**  and stores it into a **MongoDB** database.


## Features

* Automates GitHub project scraping with **Selenium**.
* Requires **manual GitHub login** for authentication.
* Extracts all visible task rows from the Scrum board.
* Saves structured task data (e.g. title, status, dates) into MongoDB.

## Project Structure

```
📁 neo-hrms-scraper/
│
├── scrap.py          # Main scraper script
└── README.md         # Project documentation
```
---

##Prerequisites

1. Python 3.7 or above
Install from: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Google Chrome browser
Required by ChromeDriver (used by Selenium).

3. MongoDB
You can use:

* Local MongoDB: [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
* Or MongoDB Atlas (update the URI in `scrap.py` accordingly).

4. Python Packages
Install using pip:

```bash
pip install selenium pymongo webdriver-manager
```
---

##How to Run

Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/neo-hrms-scraper.git
cd neo-hrms-scraper
```
Step 2: Ensure MongoDB is Running
Ensure local MongoDB is running at:

```
mongodb://localhost:27017
```

Update the connection string in `scrap.py` if you're using MongoDB Atlas:

```python
client = MongoClient("your-atlas-connection-string")
```
Step 3: Execute the Scraper

```bash
python scrap.py
```
Step 4: Manual GitHub Login

* A Chrome browser window will open to GitHub login.
* Manually log in.
* Then return to your terminal and press Enter when prompted:

```
 Log in to GitHub manually, then press Enter to continue...
```
Step 5: Scraping and Storage
* Script scrolls through the GitHub Project Board.
* Task data is extracted and saved to MongoDB.
* You'll see messages like:

```
✅ Inserted: Implement login flow
✅ Inserted: Design user dashboard
```

---

##MongoDB Output Format
Each document in MongoDB looks like this:

```json
{
  "sl_no": "1",
  "title": "Design login screen",
  "assignees": "Jane Doe",
  "status": "In Progress",
  "parent_issue": "#42",
  "start_date": "2025-05-01",
  "end_date": "2025-05-07"
}
```
---

##Customization Options

* **Scroll Depth**:

  ```python
  for _ in range(7):
  ```

  Change `7` to load more or fewer items.

**Project URL**:

  ```python
  driver.get("https://github.com/orgs/Neophyte-ai/projects/28")
  ```

  Replace with the desired GitHub Project URL.

---

##Troubleshooting

* **GitHub login issue**: Ensure you can log in manually.
* **No data scraped**: Confirm project is public or you have access.
* **MongoDB errors**: Check that MongoDB is running and accessible.
---
