from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

url = "https://www.espncricinfo.com/records/season/team-match-results/2024-2024?trophy=89"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
all_rows = soup.find_all('tr')
# links = []
# all_rows[1]soup = BeautifulSoup(html, 'html.parser')
# link_tag = soup.find('a', {'title': 'T20I # 2729'})
# href = link_tag['href']
# href

# for row in all_rows[1:]:
#     tds = row.find_all('td')
#     if len(tds)>=7:
#         title = tds[6].text.strip()
#         divEle =soup.find('a', {'title': title})
#         rowURL = "https://www.espncricinfo.com" + divEle['href']
#         links.append(rowURL)
links=['https://www.espncricinfo.com/series/icc-men-s-t20-world-cup-2024-1411166/england-vs-namibia-34th-match-group-b-1415734/full-scorecard']
all_batting_summaries = []
# for link in links:
# print(links)
for url in links:
    battingSummary = []
    team_names = []
    # print("=========================================================")
    page1 = urlopen(url)
    html1 = page1.read().decode("utf-8")
    soup1 = BeautifulSoup(html1, "html.parser")
    batting_tables = soup1.find_all('table', class_='ci-scorecard-table')
    

    # Reset team names for each link
    team1_name = ""
    team2_name = ""
    team_headers = soup1.find_all('span', class_='ds-text-title-xs ds-font-bold ds-capitalize')
      # Reset team names for each link
    # print(team_headers[0].text.strip())
    # print(team_headers[1].text.strip())

    # match_info = soup1.find_all('h1', class_='ds-text-title-xs ds-font-bold ds-mb-2 ds-m-1')
    # print(match_info)
    if (len(team_headers)==2):
        matchInfo = team_headers[0].text.strip() +  ' Vs ' + team_headers[1].text.strip()
    else:
        matchInfo = team_headers[0].text.strip() +  ' Vs ' + "Team2"
    # print(matchInfo)
    # Iterate over the tables and extract data
    
    for table in batting_tables:
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
                    battingSummary.append({
                    "match": matchInfo,
                    # "teamInnings": team_headers[0].text.strip() if inning_index==0 else "Team2",
                    "battingPos": index + 1,
                    "batsmanName": tds[0].text.strip(),
                    "dismissal": tds[1].text.strip(),
                    "runs": tds[2].text.strip(),
                    "balls": tds[3].text.strip(),
                    "4s": tds[5].text.strip(),
                    "6s": tds[6].text.strip(),
                    "SR": tds[7].text.strip(),
                    "matchid": 'T20I # 2632'
                    })
                index += 1 

df = pd.DataFrame(battingSummary)
df.to_excel('batt.xlsx', index=False)