from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

# #  URL of the webpage for data scrap
# target = "https://www.euroleaguebasketball.net/euroleague/stats/expanded/?size=1000&viewType=traditional&seasonMode=All&statisticMode=perGame"
#
# # Initialize a Selenium WebDriver (ChromeDriver)
# driver = webdriver.Chrome()
#
# # Sending an HTTP GET request to the URL
# driver.get(target)
#
# # Waiting time for the page to load
# time.sleep(3)
#
# # Scroll down to load all rows, we set 30 to get 587 rows
# for _ in range(30):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#
# # Getting the page source after loading all rows
# page_source = driver.page_source
#
# # Close the Selenium WebDriver
# driver.quit()
#
# # Parse the HTML content and scrap data using BeautifulSoup
# soup = BeautifulSoup(page_source, 'html.parser')
#
# data = []
# # finding and extracting elements
# table = soup.find('div',
#                   class_='complex-stat-table_wrap__t4tzy custom-scrollbar_wrap__qkItA custom-scrollbar__hor__yG43Q')
# #
# if table:
#     rows = table.find_all('div', class_='complex-stat-table_row__Jiu1w')
# # extracting data , skipping the header row (index 0)
#     for row in rows[1:]:
#         columns = row.find_all('div')
#
#         data.append({
#             'Player': columns[1].text.strip(),
#             'Team': columns[2].text.strip(),
#             'GP': columns[3].text.strip(),
#             'GS': columns[4].text.strip(),
#             'Min': columns[5].text.strip().split(':')[0],
#             'PTS': columns[6].text.strip(),
#             'PM_2': columns[7].text.strip(),
#             'PA_2': columns[8].text.strip(),
#             'P2proc': columns[9].text.strip('%'),
#             'PM_3': columns[10].text.strip(),
#             'PA_3': columns[11].text.strip(),
#             'P3proc': columns[12].text.strip('%'),
#             'FTM': columns[13].text.strip(),
#             'FTA': columns[14].text.strip(),
#             'FTAproc': columns[15].text.strip('%'),
#             'OR': columns[16].text.strip(),
#             'DR': columns[17].text.strip(),
#             'TR': columns[18].text.strip(),
#             'AST': columns[19].text.strip(),
#             'STL': columns[20].text.strip(),
#             'TO': columns[21].text.strip(),
#             'BLK': columns[22].text.strip(),
#             'BLKA': columns[23].text.strip(),
#             'FC': columns[24].text.strip(),
#             'FD': columns[25].text.strip(),
#             'PIR': columns[26].text.strip()
#         })
#
# # # Creating DataFrame from the extracted data
# df = pd.DataFrame(data)
#
# # Printing all rows of the DataFrame
# print(df)
# df.to_csv('BasketAll4.csv')

# add import
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('BasketAll4.csv')
df['GP'] = df['GP'].astype(int)
df['Min'] = df['Min'].astype(int)
##New Plot
# top_10_GP = df.nlargest(10, 'GP')
# df2 = top_10_GP
# print(top_10_GP)
# Player = df2['Player']
# GP = df2['GP']
#
# plt.plot(Player,GP, label='linija', color='blue', linestyle ='--', marker = 'o')
#
# plt.legend()
# plt.xlabel('x')
# plt.xticks(rotation=90)
# plt.xticks(f)
# plt.xlabel('y')
# plt.title('TOP')
# plt.show()

#New Hist
# top_min_players = df.nlargest(10, 'Min')
# print(top_min_players)
# df3 = top_min_players
# Player = df3['Player']
# Min = df3['Min']
#
# plt.hist(df3,  bins=20, label = "Min", color='purple',alpha = 0.7, edgecolor = 'black' )
#
# plt.legend()
# plt.xlabel('Player')
# plt.ylabel('Min')
# plt.xticks(rotation=90)
# plt.rcParams['xtick.labelsize'] = 2
# plt.title('Top min players')
# plt.show()


#
df['PTS'] = df['PTS'].astype(float)
top_PTS = df.nlargest(10, 'PTS')
print(top_PTS)
df4 = top_PTS
Player = df4['Player']
PTS = df4['PTS']
GP= df4['GP']
Min = df4['Min']
plt.style.use('_mpl-gallery')

# make data
x = np.arange(0, 10, 2)
ay = ['PTS']
by = ['GP']
cy = ['Min']
y = np.vstack([ay, by, cy])

# plot
fig, ax = plt.subplots()

ax.stackplot(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()


#palyginti top 10 trikaskiu metikus su 2  rezultatyvumu ( stackplot(x, y)
# plt.style.use('_mpl-gallery')
#
# # make data
# x = np.arange(0, 10, 2)
# ay = [1, 1.25, 2, 2.75, 3]
# by = [1, 1, 1, 1, 1]
# cy = [2, 1, 2, 1, 2]
# y = np.vstack([ay, by, cy])
#
# # plot
# fig, ax = plt.subplots()
#
# ax.stackplot(x, y)
#
# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 8), yticks=np.arange(1, 8))
#
# plt.show()
