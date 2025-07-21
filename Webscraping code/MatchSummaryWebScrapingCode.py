
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
url = "https://www.espncricinfo.com/records/season/team-match-results/2024-2024?trophy=89"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
table = soup.find('table')
all_rows = soup.find_all('tr')
matchSummary = []

for row in all_rows:
    tds = row.find_all('td')
    if len(tds)>=7:
        matchSummary.append({
            'team1': tds[0].text.strip(),
            'team2': tds[1].text.strip(),
            'winner': tds[2].text.strip(),
            'margin': tds[3].text.strip(),
            'ground': tds[4].text.strip(),
            'matchDate': tds[5].text.strip(),
            'scorecard': tds[6].text.strip(),
        })
# print(matchSummary)
# Convert the list of dictionaries to JSON
json_data = json.dumps(matchSummary, indent=4)

# Save the JSON data to a file
with open('match_results.json', 'w') as json_file:
    json_file.write(json_data)