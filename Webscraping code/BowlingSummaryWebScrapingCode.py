from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import pandas as pd

url = "https://www.espncricinfo.com/records/season/team-match-results/2024-2024?trophy=89"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
all_rows = soup.find_all('tr')

links=['https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/afghanistan-vs-australia-48th-match-super-eights-group-1-1415748/full-scorecard']

# for link in links:
# print(links)
for url in links:
    ballingSummary = []
    team_names = []
    # print("=========================================================")
    page1 = urlopen(url)
    html1 = page1.read().decode("utf-8")
    soup1 = BeautifulSoup(html1, "html.parser")
    balling_tables = soup1.find_all('table', class_='ds-w-full ds-table ds-table-md ds-table-auto ')
    
    
    for table in balling_tables:
        # inning_index +=1    
        rows = table.find_all('tr')
        index = 0  # Initialize index manually
        for row in rows:  # Skip the header row
            cols = row.find_all('td')
            # print(cols)
            col_data = [col.text.strip() for col in cols]
            if len(col_data) > 1:  # Ensure it's a valid row with player data
                tds = row.find_all('td')
                
                if len(tds)>=7:
                    ballingSummary.append({
                    "ballerName": tds[0].text.strip(),
                    "overs": tds[1].text.strip(),
                    "runs": tds[2].text.strip(),
                    "balls": tds[3].text.strip(),
                    "maiden": tds[5].text.strip(),
                    "runs": tds[6].text.strip(),
                    "wickets": tds[7].text.strip(),
                    "economy": tds[6].text.strip(),
                    "Zeros": tds[6].text.strip(),
                    "Fours": tds[6].text.strip(),
                    "Sixes": tds[6].text.strip(),
                    "Wides": tds[6].text.strip(),
                    "NoBalls": tds[6].text.strip(),
                    "MatchId": 'T20I # 2632',
                    })
                index += 1 
ballingSummary               
# df = pd.DataFrame(ballingSummary)
# df.to_excel('balling.xlsx', index=False)