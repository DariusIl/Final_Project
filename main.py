from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

#  URL of the webpage for data scrap
target = "https://www.euroleaguebasketball.net/euroleague/stats/expanded/?size=1000&viewType=traditional&seasonMode=All&statisticMode=perGame"

# Initialize a Selenium WebDriver (ChromeDriver)
driver = webdriver.Chrome()

# Sending an HTTP GET request to the URL
driver.get(target)

# Waiting time for the page to load
time.sleep(3)

# Scroll down to load all rows, we set 30 to get 587 rows
for _ in range(30):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Getting the page source after loading all rows
page_source = driver.page_source

# Close the Selenium WebDriver
driver.quit()

# Parse the HTML content and scrap data using BeautifulSoup
soup = BeautifulSoup(page_source, 'html.parser')

data = []
# finding and extracting elements
table = soup.find('div',
                  class_='complex-stat-table_wrap__t4tzy custom-scrollbar_wrap__qkItA custom-scrollbar__hor__yG43Q')
#
if table:
    rows = table.find_all('div', class_='complex-stat-table_row__Jiu1w')
# extracting data , skipping the header row (index 0)
    for row in rows[1:]:
        columns = row.find_all('div')

        data.append({
            'Player': columns[1].text.strip(),
            'Team': columns[2].text.strip(),
            'GP': columns[3].text.strip(),
            'GS': columns[4].text.strip(),
            'Min': columns[5].text.strip().split(':')[0],
            'PTS': columns[6].text.strip().replace('.', ','),
            'PM_2': columns[7].text.strip().replace('.', ','),
            'PA_2': columns[8].text.strip().replace('.', ','),
            'P2proc': columns[9].text.strip('%').replace('.', ','),
            'PM_3': columns[10].text.strip().replace('.', ','),
            'PA_3': columns[11].text.strip().replace('.', ','),
            'P3proc': columns[12].text.strip('%').replace('.', ','),
            'FTM': columns[13].text.strip().replace('.', ','),
            'FTA': columns[14].text.strip().replace('.', ','),
            'FTAproc': columns[15].text.strip('%').replace('.', ','),
            'OR': columns[16].text.strip().replace('.', ','),
            'DR': columns[17].text.strip().replace('.', ','),
            'TR': columns[18].text.strip().replace('.', ','),
            'AST': columns[19].text.strip().replace('.', ','),
            'STL': columns[20].text.strip().replace('.', ','),
            'TO': columns[21].text.strip().replace('.', ','),
            'BLK': columns[22].text.strip().replace('.', ','),
            'BLKA': columns[23].text.strip().replace('.', ','),
            'FC': columns[24].text.strip().replace('.', ','),
            'FD': columns[25].text.strip().replace('.', ','),
            'PIR': columns[26].text.strip().replace('.', ',')
        })

# Creating DataFrame from the extracted data
df = pd.DataFrame(data)

# Printing all rows of the DataFrame
print(df)
df.to_csv('BasketAll3.csv')