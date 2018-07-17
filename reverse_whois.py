#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import argparse

# Config
url = 'https://viewdns.info/reversewhois/?q=' # Scrape reverse whois info from here
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}

# Command Line Interface
parser = argparse.ArgumentParser(description = 'Reverse whois from registrant name or email address.')
parser.add_argument("-i", "--input", help = 'enter an email or full name', type = str, required = True)
args = parser.parse_args()

r = requests.get(url + args.input, headers = headers)

soup = BeautifulSoup(r.text, 'html.parser')

for row in soup('table')[3].find_all('tr'):
    print(row.find_all('td')[0].text)