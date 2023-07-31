from bs4 import BeautifulSoup
import requests

url = 'https://www.pro-football-reference.com/years/2023/games.htm'
r = requests.get(url)

csv_file_path = r'C:\Users\krstr\OneDrive\Desktop\PDI_Bytes\NFL'
content = r.text
soup = BeautifulSoup(content, 'html.parser')

#lets deal with title
page_title = soup.title.text
print(f'Page Title: {page_title}')


#now going through rows
trs_tags = soup.find_all('tr')  #could also simplify as  =soup('tr')
#print(len(trs_tags))   #returns 342 rows
first_row = trs_tags[0]
#print(first_row)
#print(first_row('th'))

#print(first_row.find_all('td'))  #returns empty list


'''
ths_tags = soup.find_all('th')
print(ths_tags[0])
#print(len(ths_tags))
'''

week_header = soup.find_all('th', text = 'Week') 

print(week_header) #prints out a lot of unformated gibberish






'''
table = soup.find("table", {"id": "games"})
rows = table.find_all("tr")
print (table.prettify())
#print(rows)

'''


'''
# Print out the schedules week by week
for i in range(len(weeks)):
    print(f"Week {weeks[i]}:")
    print(f"{days[i]} {dates[i]} - {visitor_teams[i]} {visitor_scores[i]} {home_teams[i]} {home_scores[i]} {times[i]}")
    print()



'''

