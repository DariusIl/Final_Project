import requests
from bs4 import BeautifulSoup

target = "https://www.dunkest.com/en/euroleague/stats/players/table/season/2022-2023?season_id=11&mode=nba&stats_type=tot&date_from=2022-10-06&date_to=2023-05-21&teams[]=31&teams[]=32&teams[]=33&teams[]=34&teams[]=35&teams[]=36&teams[]=37&teams[]=38&teams[]=39&teams[]=40&teams[]=41&teams[]=42&teams[]=43&teams[]=44&teams[]=45&teams[]=46&teams[]=47&teams[]=48&positions[]=1&positions[]=2&positions[]=3&player_search=&min_cr=4&max_cr=35&sort_by=pdk&sort_order=desc&iframe=yes&noadv=yes"
headers = {
    'statsTableHead'}
response = requests.get(target)

soup = BeautifulSoup(response.content, 'html.parser')
print(response.content)
data = []

table = soup.find('table', class_='table table--stats')
print(table)
if table:
    rows = table.find_all('tr')
    for row in rows[1:]:
        if 'Player' in row.text:
            continue
        columns = row.find_all('td')
        try:
            Player = columns[1].text.strip()
        except IndexError:
            Player = ""

        try:
            POS = columns[2].text.strip()
        except IndexError:
            POS = ""

        try:
            Team = columns[3].text.strip()
        except IndexError:
            Team = ""

        try:
            FPT = columns[4].text.strip()
        except IndexError:
            FPT = ""

        # try:
        #     close_price = columns[4].text.strip()
        # except IndexError:
        #     close_price = ""

        # try:
        #     adj_close_price = columns[5].text.strip()
        # except IndexError:
        #     adj_close_price = ""
        #
        # try:
        #     volume = columns[6].text.strip()
        # except IndexError:
        #     volume = ""

        data.append({
            'Player': Player,
            'POS': POS,
            'Team': Team,
            'FPT': FPT
            # 'Close': close_price,
            # 'Adj Close': adj_close_price,
            # 'Volume': volume
        })

# Print the scraped data
for entry in data:
    print(entry)