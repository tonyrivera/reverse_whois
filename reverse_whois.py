#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import argparse

# Config
# URL to scrape reverse whois data
url = 'https://viewdns.info/reversewhois/?q='
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0'}

# Command Line Interface
parser = argparse.ArgumentParser(description='Reverse Whois Lookup')
parser.add_argument("-i", "--input", help='Email or Full Name', required=True)
args = parser.parse_args()

r = requests.get(url + args.input, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')

for row in soup('table')[3].find_all('tr'):
    print(row.find_all('td')[0].text)
