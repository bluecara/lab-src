# Crawling

from bs4 import BeautifulSoup
import requests
import sys
import urllib.request as req
#import urllib.parse as parse
from datetime import datetime
from time import sleep

def getResult(args):
    if len(args) > 0: 
        for ar in args:        
            print("\t" + ar.select_one('h3.h_lst > span').string
                  + ' = ' + ar.select_one('div.head_info > span.value').string
                  + ' (' + ar.select_one('div.head_info > span.change').string.strip()
                  + ' ' + ar.select_one('div.head_info > span.blind').string + ')'
                  + "\n"
                )
    else:
        print("\n\tNo data")
    return


print('- Exchange rate : ' + datetime.now().strftime('%Y-%m-%d') + " -\n")

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://finance.naver.com/marketindex/'

print("Requests >>>\n")
res = requests.get(url, verify=True)
soup = BeautifulSoup(res.content, 'html.parser')
el = soup.select('#exchangeList li')
#el = soup.find('ul', {'id': 'exchangeList'}).find_all('li')
getResult(el)
#sys.exit(0)

print("-----------------------------------------\n")
sleep(1)

print("Urlopen >>>\n")
res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
el = soup.select('#exchangeList li')
getResult(el)
