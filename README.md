# IPL-cricket-year-2022-Web-scrapping-
# 🏏 IPL 2022 Auction Data Scraping & Analysis

## 📌 Project Overview

This project focuses on **web scraping and data analysis of IPL 2022 auction data**. The aim is to extract structured data from the official IPL website and analyze player statistics, pricing trends, and team strategies during the auction.

---

## 🚀 Objectives

* Scrape IPL 2022 auction data from the official website
* Convert unstructured HTML data into a structured dataset
* Perform exploratory data analysis (EDA)
* Generate insights on player pricing and auction patterns

---

## 🛠️ Tech Stack

* **Python**
* **Requests** – Fetch webpage data
* **BeautifulSoup (bs4)** – Parse HTML
* **Pandas** – Data manipulation & analysis
* **Jupyter Notebook (optional)** – Analysis

---

## 📂 Project Structure

```
├── ipl2022.py                     # Web scraping script
├── ipl 2022 stat auction.csv      # Dataset (generated)
├── README.md                      # Project documentation
```

---

## 🔍 Web Scraping Process

* Fetched data from IPL official auction page
* Parsed HTML using BeautifulSoup
* Extracted table data including:

  * Player Name
  * Team
  * Role
  * Price
  * Other auction-related stats

📌 Example code snippet:

```
url = "https://www.iplt20.com/auction/2022"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
table = soup.find("table", class_="auction-tbl")
```

The script dynamically extracts table headers and rows to build a structured dataset.

📄 Reference: 

---

## 📊 Data Analysis (EDA)

Key analysis performed:

* Distribution of player prices
* Team-wise spending patterns
* Role-based analysis (batsman, bowler, all-rounder)
* Identification of most expensive players

---

## 📈 Key Insights

* Certain teams spent heavily on **all-rounders**, indicating their strategic importance
* A few players received significantly higher bids, showing demand-supply imbalance
* Teams followed different strategies: some focused on star players, while others built balanced squads
* Price variation highlights the importance of player performance and experience

---

## ⚠️ Limitations

* Data limited to IPL 2022 auction only
* Website structure dependency (scraper may break if HTML changes)
* No historical comparison included
* Missing deeper player performance metrics

---

## 🔮 Future Improvements

* Include multiple IPL seasons for trend analysis
* Build interactive dashboards (Power BI / Tableau)
* Add player performance data (runs, wickets, strike rate)
* Predict player prices using ML models

---

## 👨‍💻 Author

**Piyush Banchhor**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!


## ✅ Project Conclusion

This project successfully demonstrated the use of web scraping and data analysis techniques on IPL 2022 auction data. By extracting data from the official IPL website using Python libraries such as Requests and BeautifulSoup, unstructured HTML content was converted into a structured dataset suitable for analysis.

The exploratory data analysis revealed important insights into team strategies and player valuation. It was observed that teams invested heavily in all-rounders and experienced players, highlighting their importance in building a balanced squad. Additionally, there was a significant variation in player prices, indicating differences in demand, skill level, and past performance.

The analysis also showed that different teams followed different auction strategies. Some teams focused on acquiring star players with high budgets, while others aimed to create a well-balanced team by distributing their spending across multiple players.

Overall, this project provided hands-on experience in web scraping, data cleaning, and sports analytics. It also demonstrated how raw data can be transformed into meaningful insights that help understand real-world decision-making processes in auctions.

This project can be further enhanced by including data from multiple IPL seasons, integrating player performance statistics, and building predictive models or interactive dashboards for deeper analysis.
