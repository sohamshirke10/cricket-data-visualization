# 🏏 Crafting the Ultimate Winning XI | ICC T20 World Cup 2024  
**Cricket Data Analytics & Visualization Project**

## 📌 Overview
This project showcases end-to-end cricket data analytics and visualization for the ICC Men's T20 World Cup 2024. It includes web scraping, data cleaning, transformation, modeling, and interactive dashboard creation using **Power BI**.  
The goal is to analyze and compare player performances to build the **Best XI** of the tournament using data-driven insights.

---

## 🧠 Problem Statement
Develop a dashboard that helps evaluate all players who participated in the ICC T20 World Cup 2024 and select the best-performing 11 players. This is done by analyzing match-wise and career-wise stats using performance metrics such as strike rate, average, economy rate, and wickets taken.

---

## 🔗 Data Source  
All data has been **web scraped** from the official [ESPN Cricinfo World Cup 2024 Series Page](https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166) using **Python** and **BeautifulSoup**.

📂 Web scraping code is available here:  
👉 [`Webscraping Code`](https://github.com/sohamshirke10/cricket-data-visualization/tree/main/Webscraping%20code)

---

## 📥 Data Collection
- Extracted match-wise and player-wise performance stats
- Gathered player career data for better comparison
- Used **Jupyter Notebook** and **BeautifulSoup** for scraping
- Converted JSON to Pandas DataFrames and then to CSVs for analysis

---

## 🧹 Data Cleaning & Transformation
- Cleaned player names, handled missing/null values, and linked match & player IDs
- Used **Pandas** for cleaning and **Power BI Power Query** for data shaping
- Ensured consistency and usability of datasets for dashboarding

---

## 🧩 Data Modeling
- Designed relationships using keys like `match_id`, `player_id`, and `team`
- Created **DAX measures**, **calculated columns**, and **parameters** to support analysis
- Optimized model for responsiveness and interactivity in Power BI

---

## 📊 Interactive Reports

### 🎯 Player Performance Analysis

| Section | Screenshot |
|--------|------------|
| **Front Page** | ![Front Page](https://raw.githubusercontent.com/sohamshirke10/cricket-data-visualization/main/Screenshots/front%20page.png) |
| **Middle Order** | ![Middle Order](https://raw.githubusercontent.com/sohamshirke10/cricket-data-visualization/main/Screenshots/Middle%20Order.png) |
| **Finishers** | ![Finishers](https://raw.githubusercontent.com/sohamshirke10/cricket-data-visualization/main/Screenshots/Finishers.png) |
| **All-Rounders** | ![Allrounders](https://raw.githubusercontent.com/sohamshirke10/cricket-data-visualization/main/Screenshots/Allrounders.png) |
| **Bowlers** | ![Bowlers](https://raw.githubusercontent.com/sohamshirke10/cricket-data-visualization/main/Screenshots/Bowlers.png) |
| **Player Summary** | ![Player Summary](https://raw.githubusercontent.com/sohamshirke10/cricket-data-visualization/main/Screenshots/Player%20Summary%20throughout%20worldcup.png) |
| **Final XI** | ![Final XI](https://raw.githubusercontent.com/sohamshirke10/cricket-data-visualization/main/Screenshots/Final%2011.png) |

---

## 🛠 Tools & Technologies
- **Python**
- **Jupyter Notebook**
- **BeautifulSoup (Web Scraping)**
- **Pandas**
- **Power BI**
- **Power Query Editor**
- **Excel**

---

## 📊 Power BI Dashboard (Live)
👉 [View Interactive Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNjEyNDAyMjYtMTc4Ni00NjRmLThiOGEtODFmNzUzZjg4YTgwIiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9&pageName=ReportSection3a8cb23b814911c94608)

---

## 🎓 References
- [Codebasics.io - Power BI Project](https://codebasics.io/courses)
