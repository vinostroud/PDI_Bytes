import os
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET  

import requests
from bs4 import BeautifulSoup


# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    tree = ET.parse(tempfile)
    root = ET.fromstring(content)  #can consolidate tree and root into one line: root = ET.fromstring('placeholder_content_variable'). This assumes etree imported as ET
    #fromstring is a class method
    categories = [c.text for c in root.iterfind('channel/item/category')] #iterfind is  method in ElementTree module, it finds elements in XML or HTML
    c = Counter(categories) #note c is a different variable than c.text above in categories
    return c.most_common(n)
print(get_pybites_top_tags(n=5))



'''
Below prints the corret results but is not formatted correctly 
soup = BeautifulSoup(content, 'lxml')

def get_pybites_top_tags(n):
    categories = soup.find_all('category')
    category_count = Counter([category.text for category in categories])
    top_tags = category_count.most_common(n)
    tag_list = [f"({tag}: {count})" for tag, count in top_tags]
    return tag_list


print(get_pybites_top_tags(5))
'''