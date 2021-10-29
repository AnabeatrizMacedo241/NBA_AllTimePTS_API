"""
Created on Tue Oct 26 14:25:27 2021

@author: anabeatrizmacedo
"""
import pandas as pd
from selenium import webdriver
from nba_api.stats.endpoints import playergamelog
from nba_api.stats.library.parameters import SeasonAll
import seaborn as sns
url = 'https://www.nba.com/stats/alltime-leaders/?SeasonType=Regular%20Season'
driver = webdriver.Chrome()
driver.get(url)

def prox_pag():
    #Next page function
    p= driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]')
    p.click()
    
#Creates a dataframe
df = pd.DataFrame()
#Scrapes the first 2 pages of the dataframe
for c in range(2):
    web_element=driver.find_element_by_xpath("""/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table""")
    #print(web_element.text)
    df2 = pd.read_html(web_element.get_attribute('outerHTML'))
    df = df.append(df2)
    prox_pag()
driver.quit()
#df.to_csv('nba_ALLTIME.csv', index=False)
#Locates the top 3 players ny their names
kareem = df.loc[(df['Player']=='Kareem Abdul-Jabbar')]
malone = df.loc[(df['Player']=='Karl Malone')]
lebron = df.loc[(df['Player']=='LeBron James')]
#Only look for the column 'PTS'of the dataframe
pts_first = kareem['PTS']
pts_second = malone['PTS']
pts = lebron['PTS']
#Nba api to get data about LeBron's career
lebron_games = playergamelog.PlayerGameLog(player_id='2544', season=SeasonAll.all)
lebron_games_df = lebron_games.get_data_frames()[0] 
lebron_games_df_points = lebron_games_df['PTS']
#Checking how many points and games LeBron needs to become the all-time points leader based on his average career points
for pt in pts:
  if pt>38387:
    print('Lebron is the all-time NBA points leader!')
  elif pt>36928:
    print('Lebron is the second all-time NBA points leader!')
    for difference in pts_first:
      difference = difference-pt
      mean = lebron_games_df_points.mean()
      games = difference/mean
      print('Lebron needs to score {} points in {} to surprass Kareem Abdul-Jabaar'.format(difference,round(games)))
  else:
    print('Lebron is still the third all-time NBA points leader')
    for difference in pts_first:
      difference = difference-pt
      mean = lebron_games_df_points.mean()
      games = difference/mean
      print('Lebron needs {} points in {} games to surprass Kareem Abdul-Jabaar'.format(difference,round(games)))
    for difference in pts_second:
      difference = difference-pt
      mean = lebron_games_df_points.mean()
      games = difference/mean
      print('Lebron needs {} points in {} games to surprass Karl Malone'.format(difference,round(games)))
    
#Creates a horizontal bar graph with the results
df_top3 = df[:3]
ax = sns.barplot(x='PTS', y='Player', data=df_top3, palette='rainbow')
ax.set_title('All-time NBA points leaders', size=15)
ax.set_xlabel('Total points(Until now)',size=12)
ax.set_ylabel('Players', size =12)