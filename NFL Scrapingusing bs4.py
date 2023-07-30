from bs4 import BeautifulSoup
import requests

url = 'https://www.pro-football-reference.com/teams/was/2022.htm'
r = requests.get(url)

content = r.text

soup = BeautifulSoup(content, 'html.parser')

title = soup.title.text
print(f'Page Title: {title}')




'''<div id="all_team_stats" class="table_wrapper">

<div class="section_heading assoc_team_stats" id="team_stats_sh">
  <span class="section_anchor" id="team_stats_link" data-label="Team Stats and Rankings"></span><h2>Team Stats and Rankings</h2>    <div class="section_heading_text">
      <ul>
      </ul>
    </div>'''