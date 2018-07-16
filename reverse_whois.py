#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

url = 'https://viewdns.info/reversewhois/?q=' # Scrape reverse whois info from here
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
query = input('Enter Registrant Name or Email Address: ')

r = requests.get(url + query, headers = headers)

soup = BeautifulSoup(r.text, 'html.parser')

print( soup('table')[3].get_text(',', strip=True) )