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
# replace and split data
        data.append({
            'Player': columns[1].text.strip(),
            'Team': columns[2].text.strip(),
            'GP': columns[3].text.strip(),
            'GS': columns[4].text.strip(),
            'Min': columns[5].text.strip().split(':')[0],
            'PTS': columns[6].text.strip(),
            'PM_2': columns[7].text.strip(),
            'PA_2': columns[8].text.strip(),
            'P2proc': columns[9].text.strip('%'),
            'PM_3': columns[10].text.strip(),
            'PA_3': columns[11].text.strip(),
            'P3proc': columns[12].text.strip('%'),
            'FTM': columns[13].text.strip(),
            'FTA': columns[14].text.strip(),
            'FTAproc': columns[15].text.strip('%'),
            'OR': columns[16].text.strip(),
            'DR': columns[17].text.strip(),
            'TR': columns[18].text.strip(),
            'AST': columns[19].text.strip(),
            'STL': columns[20].text.strip(),
            'TO': columns[21].text.strip(),
            'BLK': columns[22].text.strip(),
            'BLKA': columns[23].text.strip(),
            'FC': columns[24].text.strip(),
            'FD': columns[25].text.strip(),
            'PIR': columns[26].text.strip()
        })

# # Creating DataFrame from the extracted data
df = pd.DataFrame(data)

# Printing all rows of the DataFrame
print(df)
# save to CSV
df.to_csv('BasketAll4.csv')

# add import for pie chart
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('BasketAll4.csv')
df['PM_2'] = df['PM_2'].astype(float)
df['PM_3'] = df['PM_3'].astype(float)
df['FTM'] = df['FTM'].astype(float)
#
# # 1 New Plot TOP 10 players by GP
top_10_GP = df.nlargest(10, 'GP')
df2 = top_10_GP
print(top_10_GP)
Player = df2['Player']
GP = df2['GP']
plt.figure(figsize=(10, 8))
plt.plot(Player,GP, label='linija', color='blue', linestyle ='--', marker = 'o')

plt.legend()
plt.xlabel('x')
plt.xticks(rotation=25)
plt.xlabel('y')
plt.title('TOP_game_play')
plt.show()

# 2 New Hist Top 2 points players vs 3 points
# Extract the top ten players based on 'PM_2'
top_10_players2 = df.nlargest(10, 'PM_2')

# Extract the 'Player', 'PM_2', and 'PM_3' values of the top ten players
players = top_10_players2['Player']
twopointers_made = top_10_players2['PM_2']
threepointers_made = top_10_players2['PM_3']

# Create a stacked bar chart for the top ten players
plt.bar(players, twopointers_made, label='2-Pointers Made', color='skyblue')
plt.bar(players, threepointers_made, bottom=twopointers_made, label='3-Pointers Made', color='limegreen')

# Customize the plot
plt.title('Top 10 Players - 2-Pointers and 3-Pointers Made')
plt.xlabel('Player')
plt.ylabel('Number of Made Shots')
plt.legend()

# Rotate x-axis labels
plt.xticks(rotation=90)

# Show the plot
plt.show()

## 3 All players pts MIN MAX Median and AVG
plt.figure(figsize=(8, 6))  # Optional: Set the figure size
plt.boxplot(df['PTS'], vert=False)

# Calculate and display the statistics
max_points = df['PTS'].max()
min_points = df['PTS'].min()
median_points = df['PTS'].median()
avg_points = df['PTS'].mean()

# Annotate the plot with statistics
plt.text(max_points, 1, f'Max: {max_points}', va='center')
plt.text(min_points, 1, f'Min: {min_points}', va='center')
plt.text(median_points, 1.2, f'Median: {median_points}', va='center')
plt.text(avg_points, 0.8, f'Avg: {avg_points:.2f}', va='center')

plt.title(' Points Max, Min, Median, and Average')
plt.xlabel('Points')
plt.show()

# 4 TOP 10 Players PTS

top_10_players = df.nlargest(10, 'PTS')

# Extract the 'PTS' values and player
pts = top_10_players['PTS']
players = top_10_players['Player']
plt.figure(figsize=(20, 20))
# Create  bar chart for the top ten players
plt.barh(players, pts, color='skyblue')

for player, pt in zip(players, pts):
    plt.text(pt, player, str(pt),va='center')

# Customize the plot
plt.title('Top 10 Players - Points Distribution')
plt.xlabel('Points (PTS)')
plt.ylabel('Player')

# Show the plot
plt.show()

##5 TOP GP vs losser 2/3 points

# Calculate and display the statistics
top_30_GP = df.nlargest(30, 'GP')
df2 = top_30_GP
print(top_30_GP)

# Extract the losser 5 players based on 'PTS'
top_losser2 = df2.nsmallest(5, 'PTS')
df3= top_losser2
print(top_losser2)

# Extract the 'Player', 'PM_2', and 'PM_3' values of the top 5 lossers players
players = top_losser2['Player']
twopointers_made = top_losser2['PM_2']
threepointers_made = top_losser2['PM_3']

# Create a stacked bar chart for the top 5 players
plt.bar(players, twopointers_made, label='2-Pointers Made', color='skyblue')
plt.bar(players, threepointers_made, bottom=twopointers_made, label='3-Pointers Made', color='limegreen')

# Customize the plot
plt.title('Top 5 lossers - 2-Pointers and 3-Pointers Made')
plt.xlabel('Player')
plt.ylabel('Number of Made Shots')
plt.legend()

# Rotate x-axis labels
plt.xticks(rotation=90)

# Show the plot
plt.show()



#6 all 2/3/F in Pie

# make data
sum_2_points = np.sum(df['PM_2'])
sum_3_points = np.sum(df['PM_3'])
sum_FMT = np.sum(df['FTM'])
# print(sum_FMT)
plt.figure(figsize=(10, 8))
x = [sum_2_points, sum_3_points, sum_FMT]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
# pie chart
labels = ['2Points', '3Points', 'FMT']
plt.pie(x, colors=colors, center=(4, 4),
       wedgeprops={"linewidth": 1, "edgecolor": "white"}, labels=labels, autopct='%1.1f%%',
       startangle=90)
plt.title('2points/3points/FMT Total')
# Show the plot
plt.show()

