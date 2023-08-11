from bs4 import BeautifulSoup as bs
import requests
import argparse

url_2023 = 'https://www.pro-football-reference.com/years/2023/games.htm'
schedule_url_template = 'https://www.pro-football-reference.com/years/{}/games.htm'

headToHead_csv_path= ' ' #placeholder for path my csv file
   
def main() -> None:
    "business logic happens here"
    args = parse_arguments()
    content = get_2023_week1_schedule(schedule_url_template.format(args.year))
    print(content)


def parse_arguments() -> argparse.Namespace:
    "To avoid hardcoding eg URLs, file paths"
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', '-y', default = '2023', help='year to search for schedule')
    return parser.parse_args()



def filter_for_rows(text: str) -> str:
    return text
    


def get_2023_week1_schedule(url: str) -> str:
    
    response = requests.get(url)
    if not response.ok:
        print('Error getting URL')
    return filter_for_rows(response.content)

#print(get_2023_week1_schedule(schedule_url_template))

main() -y '2022'

'''this function will pull the week 1 schedule, and return the teams'
    head to head matchups, noting home and home. For Example: Home / Det Lions v. Away/ KC Chiefs" 

    '''
    
    











'''
Notes:
confirming directory functions
def main() -> None: #functions returns None
    print("hello world", url_2023)
'''
