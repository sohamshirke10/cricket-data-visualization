from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import pandas as pd

url = "https://www.espncricinfo.com/records/season/team-match-results/2024-2024?trophy=89"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
all_rows = soup.find_all('tr')

links=['https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/united-states-of-america-vs-canada-1st-match-group-a-1415701/full-scorecard']
# for link in links:
# print(links)
for url in links:
    PlayerSumnmary = []
    team_names = []
    # print("=========================================================")
    page1 = urlopen(url)
    html1 = page1.read().decode("utf-8")
    soup1 = BeautifulSoup(html1, "html.parser")
    bowling_tables = soup1.find_all('table', class_='ds-w-full ds-table ds-table-md ds-table-auto')
    batting_tables = soup1.find_all('table', class_='ci-scorecard-table')

    
    for table in batting_tables:
        urlnew = "https://www.espncricinfo.com" + 
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
                    PlayerSumnmary.append({
                    "PlayerName": tds[0].text.strip(),
                    "team": tds[1].text.strip(),
                    "Image": tds[2].text.strip(),
                    "BattingStyle": tds[3].text.strip(),
                    "BowlingStyle": tds[4].text.strip(),
                    "PlayingRole": tds[5].text.strip(),
                    "Description": tds[6].text.strip(),
                    })
    
    for table in bowling_tables:
        urlnew = "https://www.espncricinfo.com" + 
        # inning_index +=1    
        rows = table.find_all('tr')
        index = 0  # Initialize index manually
        for row in rows:  # Skip the header row
            cols = row.find_all('td')
            # print(cols)
            col_data = [col.text.strip() for col in cols]
            if len(col_data) > 1:  # Ensure it's a valid row with player data
                tds = row.find_all('td')
                
                if len(tds)>=11:
                    PlayerSumnmary.append({
                    "PlayerName": tds[0].text.strip(),
                    "team": tds[1].text.strip(),
                    "Image": tds[2].text.strip(),
                    "BattingStyle": tds[3].text.strip(),
                    "BowlingStyle": tds[4].text.strip(),
                    "PlayingRole": tds[5].text.strip(),
                    "Description": tds[6].text.strip(),
                    })
     

df = pd.DataFrame(PlayerName)
df.to_excel('PlayerInfooo.xlsx', index=False)