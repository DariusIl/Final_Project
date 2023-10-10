# import
import pandas as pd
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import psycopg2
import numpy as np
import matplotlib.pyplot as plt

target = "https://www.euroleaguebasketball.net/euroleague/stats/expanded/?size=25&viewType=traditional&statisticMode=perGame&seasonMode=All&sortDirection=descending&statistic=score"
# headers = {
#     'User-Agent': 'complex-stat-table_row__Jiu1w'}
response = requests.get(target)

soup = BeautifulSoup(response.content, 'html.parser')
data = []

table = soup.find('div', class_='complex-stat-table_wrap__t4tzy custom-scrollbar_wrap__qkItA custom-scrollbar__hor__yG43Q')
# print(table)
if table:
    rows = table.find_all('div', class_='complex-stat-table_row__Jiu1w')
    for row in rows[1:]:
        columns = row.find_all('div')
        try:
            Player = columns[1].text.strip()
        except IndexError:
            Player = ""

        try:
            Team = columns[2].text.strip()
        except IndexError:
            Team = ""

        try:
            GP = columns[3].text.strip()
        except IndexError:
            GP = ""

        try:
            GS = columns[4].text.strip()
        except IndexError:
            GS = ""

        try:
            Min = columns[5].text.strip()
        except IndexError:
            Min = ""

        try:
            PTS = columns[6].text.strip()
        except IndexError:
            PTS = ""

        try:
            PM_2 = columns[7].text.strip()
        except IndexError:
            PM_2 = ""

        try:
            PA_2 = columns[8].text.strip()
        except IndexError:
            PA_2 = ""

        try:
            P2proc = columns[9].text.strip()
        except IndexError:
            P2proc = ""

        try:
            PM_3 = columns[10].text.strip()
        except IndexError:
            PM_3 = ""

        try:
            PA_3 = columns[11].text.strip()
        except IndexError:
            PA_3 = ""

        try:
            P3proc = columns[12].text.strip()
        except IndexError:
            P3proc = ""

        try:
            FTM = columns[13].text.strip()
        except IndexError:
            FTM = ""

        try:
            FTA = columns[14].text.strip()
        except IndexError:
            FTA = ""

        try:
            FTAproc = columns[15].text.strip()
        except IndexError:
            FTAproc = ""

        try:
            OR = columns[16].text.strip()
        except IndexError:
            OR = ""

        try:
            DR = columns[17].text.strip()
        except IndexError:
            DR = ""

        try:
            TR = columns[18].text.strip()
        except IndexError:
            TR = ""

        try:
            AST = columns[19].text.strip()
        except IndexError:
            AST = ""

        try:
            STL = columns[20].text.strip()
        except IndexError:
            STL = ""

        try:
            TO = columns[21].text.strip()
        except IndexError:
            TO = ""

        try:
            BLK = columns[22].text.strip()
        except IndexError:
            BLK = ""

        try:
            BLKA = columns[23].text.strip()
        except IndexError:
            BLKA = ""

        try:
            FC = columns[24].text.strip()
        except IndexError:
            FC = ""

        try:
            FD = columns[25].text.strip()
        except IndexError:
            FD = ""

        try:
            PIR = columns[26].text.strip()
        except IndexError:
            PIR = ""

        data.append({
        'Player': Player,
        'Team': Team,
        'GP': GP,
        'GS': GS,
        'Min': Min,
        'PTS': PTS,
        'PM_2': PM_2,
        'PA_2': PA_2,
        'P2proc': P2proc,
        'PM_3': PM_3,
        'PA_3': PA_3,
        'P3proc': P3proc,
        'FTM': FTM,
        'FTA': FTA,
        'FTAproc' : FTAproc,
        'OR': OR,
        'DR': DR,
        'TR': TR,
        'AST': AST,
        'STL': STL,
        'TO': TO,
        'BLK': BLK,
        'BLKA': BLKA,
        'FC': FC,
        'FD' : FD,
        'PIR': PIR
    })

# Print the scraped data
for entry in data:
    print(entry)

# Create a DataFrame from the extracted data
df = pd.DataFrame(data)
    # Print the first 20 rows of the DataFrame
print(df)
df.to_csv('Basket.csv')


# df = pd.read_csv('Basket.csv')
# print(df.to_string())