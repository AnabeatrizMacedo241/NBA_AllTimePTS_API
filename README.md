# NBA all-time points analysis API 🏀
<h4><a href="#introduction">About the API</a> | <a href="#instruction">How to use</a> | <a href="#reference">Reference</a> | <a href="#functions">Documentation</a> | <a href="#code">Github</a> </h4>

<br />

<h2 id="introduction">About the API </h2>
<p>
	Working with data from the National Basketball Association all-time points leaders table.
Have you ever wondered who is the player with most points on the NBA? Or how long will Lebron take to become the leader? Or just curiosity about your favorite players statistics? Well, you are in the right place. By this API we can get insights from many basketball players and how they made/are making impact on the league.
</p>

<br />

<h2 id="instruction">How to use</h2>

<strong>Libraries needed</strong>

    pip install pandas
    pip install time
    pip install re
    pip install selenium

<br />

<strong>Installing the API</strong>

    pip install NBA-AllTimePTS-API
  
 <br/>   
    
<strong>Importing the API</strong>

    from NBA_AllTimePTS_API import Stats

<br />

<strong>Example of use</strong>

<img width="1182" alt="Screen Shot 2021-11-30 at 15 42 40" src="https://user-images.githubusercontent.com/84348494/144108221-aabc3efc-0569-4c3a-840b-e934e16bbe4f.png">

<br />
	
<h2 id="functions">Methods</h2>

| Method:                | What the method does:                                                                                                   |
| :----------------------------- | :------------------------------------------------------------------------------------------------------------------- |
|`get_table(driver, n_pages)`| Returns a dataset with the players data by the number of pages you insert                                                                                         |
|`get_player(player_name)`| Returns information of a specific player                                                        |
|`top3Chart()`| Returns the top 3 all-time points leaders of NBA                                                          |
|`isLebronLeader()`| Returns how many points and games LeBron needs to become the all-time points leader or if he has already become the leader                                                                         |
|`bestTS()`| Returns the player with the best TS% and their table Ranking position   |
|`bestFG()`| Returns the player with the best FG% and their table Ranking position   |
|`best3P( , minimumAttempts=100)`| Returns the player with the best 3P% and their table Ranking position                                             |
|`bestFT()`| Returns the player with the best FT% and their table Ranking position  |
|`overallStats( , player_name)`| Returns the MPG, PPG, RPG, APG, SPG and TOPF of a specific player  |
|`overallRebounds( , player_name)`| Returns the % of offensive and defensive rebounds of a specific player  |
|`tovPercent( , player_name)`| Estimate percentage of turnovers per 100 plays by a specific player |
|`mostRebounds()`| Returns the player with the most Rebounds and their table Ranking position |
|`mostAssists()`| Returns the player with the most Assists and their table Ranking position   |
|`mostSteals()`| Returns the player with the most Steals and their table Ranking position     |
|`mostBlocks()`| Returns the player with the most Blocks and their table Ranking position     |
|`mostTurnovers()`| Returns the player with the most Turnovers and their table Ranking position |
|`bestOffensivePlayer()`| Returns the best Offensive Player and their table Ranking position  |
|`bestDefensivePlayer()`| Returns the best Defensive Player and their table Ranking position|
<p>Parameters:
	<ul>
		<li>driver= The webdriver you wish to use(I.e: Chrome, Firefox etc.)</li>
		<li>n_pages= Number of pages of data you want.</li>
  <li>player_name= Name of the player you want.</li>
  <li>minimumAttempts = This is a optional parameter, if not given: by deafault it will be 100.</li>  
	</ul>
</p>

<br />

<h2 id="code">Github Repository</h2>

Repository with the documentation and examples of how to use the package. 

<ul>
	<li>https://github.com/AnabeatrizMacedo241/NBA_AllTimePTS_API</li>
</ul>

<br />

<h2 id="reference">Reference</h2>

<ul>
	<li>https://www.nba.com/stats/alltime-leaders/</li>
</ul>

<br />
