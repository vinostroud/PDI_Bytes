'''test code for getting a different year's week 1 schedule'''

from bs4 import BeautifulSoup as bs
import requests
import argparse

from .filter_for_rowsFunction import filter_for_rows


def get_2022_week1_schedule(url: str) -> str:
    
    response = requests.get(url)
    if not response.ok:
        print('Error getting URL')
    return filter_for_rows(response.content)