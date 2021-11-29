"""
Created on Tue Nov 23 14:01:23 2021

@author: anabeatrizmacedo
"""
import pandas as pd
import seaborn as sns
from selenium import webdriver
import time
class NBA_AllTime:
    def __init__(self, driver, n_pages):
        self.driver=driver
        self.n_pages=n_pages
        url = 'https://www.nba.com/stats/alltime-leaders/?SeasonType=Regular%20Season'
        self.driver.get(url)
        df = pd.DataFrame()
        for c in range(n_pages):
            web_element=self.driver.find_element_by_xpath("""/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table""")
            #print(web_element.text)
            df2 = pd.read_html(web_element.get_attribute('outerHTML'))
            df = df.append(df2)
            time.sleep(2)
            self._prox_pag()
        self.driver.quit()
        self._clean_df(df)
        
    def _prox_pag(self):
        p= self.driver.find_element_by_xpath('/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/a[2]')
        p.click()
            
    def _clean_df(self,df):
        df = df.reset_index(drop=True)
        df = df.replace('-', 0)
        df = df.rename(columns={'#':'Ranking'})
        colunas = list(df.columns)
        colunas.remove('Player')
        df[colunas] = df[colunas].apply(pd.to_numeric,axis=1)
        df.set_index('Player', inplace=True)
        self.df=df
    
    def get_table(self):
        return self.df

class Stats(NBA_AllTime):
    
    def get_player(self, player_name):
        player = self.df.loc[player_name]
        if len(player)==0:
            raise  ExceptionPlayerName('No results for this player, check if you wrote his name correctly.')
        return(player)

    def top3Chart(self):
        print(f'First, {self.df.index[0]}: {round(self.df.PTS[0])} points')
        print(f'Second, {self.df.index[1]}: {round(self.df.PTS[1])} points')
        print(f'Third, {self.df.index[2]}: {round(self.df.PTS[2])} points')

    def isLebronLeader(self): #LeBron all-time leader function
        df_lebron = self.df.copy()
        pts_lebron = df_lebron.loc['LeBron James', 'PTS']
        pts_first =  df_lebron['PTS'][0]
        pts_second = df_lebron['PTS'][1]
        lebronMeanPTS = pts_lebron/df_lebron.loc['LeBron James', 'GP']
        difference_first= pts_first-pts_lebron
        difference_second =  pts_second-pts_lebron
        games_first = difference_first/lebronMeanPTS
        games_second = difference_second/lebronMeanPTS
        if pts_lebron>pts_first:
            print('Lebron is the all-time NBA points leader!')
        elif pts_lebron>pts_second:
            print('Lebron is the second all-time NBA points leader!')
            print(f'Lebron needs to score {round(difference_first)} points in {round(games_first)} games to surprass {self.df.index[0]}')
        else:
            print('Lebron is still the third all-time NBA points leader')
            print(f'Lebron needs to score {round(difference_first)} points in {round(games_first)} games to surprass {self.df.index[0]}')
            print(f'Lebron needs {round(difference_second)} points in {round(games_second)} games to surprass {df_lebron.index[1]}')

    def bestTS(self):
        ts = self.df['TS%'].max()
        player = self.df.loc[self.df['TS%']==ts]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'Best FG% is {ts}% from {player_name} in the {position}th place on the all-time points list.')
        
    def bestFG(self):
        fg = self.df['FG%'].max()
        player = self.df.loc[self.df['FG%']==fg]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'Best FG% is {fg}% from {player_name} in the {position}th place on the all-time points list.')


    def best3P(self, minimumAttempts=100):
        df_3A = self.df.loc[self.df['3PA']>minimumAttempts]
        df_3Percent = df_3A['3P%'].max()
        player = self.df.loc[self.df['3P%']==df_3Percent]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'Best 3P% with, at least, {minimumAttempts} attempts is {player_name} with a {df_3Percent}% and he is at the {position}th place on the all-time points list.')
    
    def bestFT(self):
        ft = self.df['FT%'].max()
        player = self.df.loc[self.df['FT%']==ft]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'Best FT% is {ft}% from {player_name} in the {position}th place from the all-time points list.')
    
    def overallStats(self, player_name):
        player = self.df.loc[player_name]
        mpg = player['MIN']/player['GP']
        ppg = player['PTS']/player['GP']
        rpg = player['REB']/player['GP']
        apg = player['AST']/player['GP']
        spg = player['STL']/player['GP']
        topg = player['TOV']/player['GP']
        if len(player)==0:
            raise  ExceptionPlayerName('No results for this player, check if you wrote his name correctly.')
        print(f'{player_name} stats:\nMPG:{mpg:.1f}\nPPG:{round(ppg,1)}\nRPG:{round(rpg,1)}\nAPG:{round(apg,1)}\nSPG:{round(spg,1)}\nTOPG:{round(topg,1)}')
      
    def overallRebounds(self, player_name):
        player = self.df.loc[player_name]
        df_ovr = (player['OREB'])+(player['DREB'])
        oreb = (player['OREB']/df_ovr)*100
        dreb = (player['DREB']/df_ovr)*100
        if len(player_name)==0:
            raise  ExceptionPlayerName('No results for this player, check if you wrote his name correctly.')
        print(f'The overall reobunds of {player_name}:\n{round(oreb)}% offensive\n{round(dreb)}% defensive.')
    
    def tovPercent(self, player_name):
        player = self.df.loc[player_name]
        tov = 100*(player['TOV']/(player['FGA']+0.44*(player['FTA']+player['TOV'])))
        if len(player)==0:
            raise  ExceptionPlayerName('No results for this player, check if you wrote his name correctly.')
        print(f'The TOV% of {player_name} is {tov}%.')
        
    def mostRebounds(self):
        mostREB = self.df['REB'].max()
        player = self.df.loc[self.df['REB']==mostREB]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'The player with mosts rebounds is {player_name} with {mostREB} rebounds at the {position}th in the all-time points list')

    def mostAssists(self): 
        mostAST = self.df['AST'].max()
        player = self.df.loc[self.df['AST']==mostAST]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'The player with mosts assists is {player_name} with {mostAST} assists at the {position}th in the all-time points list')
    
    def mostSteals(self):
        mostSTL = self.df['STL'].max()
        player = self.df.loc[self.df['STL']==mostSTL]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'The player with most steals is {player_name} with {mostSTL} steals at the {position}th in the all-time points list')
    
    def mostBlocks(self):
        mostBLK = self.df['BLK'].max()
        player = self.df.loc[self.df['BLK']==mostBLK]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'The player with most blocks is {player_name} with {mostBLK} blocks at the {position}th in the all-time points list')
    
    def mostTurnovers(self):
        mostTOV = self.df['TOV'].max()
        player = self.df.loc[self.df['TOV']==mostTOV]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'The player with most turnovers is {player_name} with {mostTOV} turnovers at the {position}th in the all-time points list')
         
    def bestOffensivePlayer(self):
        self.df['OFE'] = ((self.df['PTS']+self.df['AST']+self.df['BLK']+self.df['REB']-(self.df['FGA']-self.df['FGM'])-(self.df['FTA']-self.df['FTM'])-self.df['TOV'])/self.df['GP'])
        higherOFE = self.df['OFE'].max()
        player = self.df.loc[self.df['OFE']==higherOFE]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'Best offensive player efficiency is {player_name} with a {round(higherOFE,1)} and he is at the {position}th place on the all-time points list.')
        
    def bestDefensivePlayer(self): #40 is an outstanding performance, 10 is an average performance
        self.df['DFE'] = ((self.df['STL']+self.df['BLK']+self.df['REB'])/self.df['GP'])
        higherDFE = self.df['DFE'].max()
        player = self.df.loc[self.df['DFE']==higherDFE]
        player_name = player.index[0]
        position = player.loc[player.index[0], 'Ranking']
        print(f'Best defense player efficiency is {player_name} with a {round(higherDFE,2)} and he is at the {position}th place on the all-time points list.')
        
class ExceptionPlayerName(Exception):
    pass

#tabele = get_table(webdriver.Chrome(),1)