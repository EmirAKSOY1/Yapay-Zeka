import requests 
from bs4 import BeautifulSoup   
import csv 
import pandas as pd
r = requests.get('https://www.ensonhaber.com/gundem/1') 
counter=1

news_title = []
try:
    soup = BeautifulSoup(r.content, 'html.parser') 
    for link in soup.find_all('span',class_='text'): 
        d={}
        a = link.find('span')
        if(a!=None):
            print(f"{counter}-{a.text}")
            d['id'] = counter
            d['Title'] = a.text
            news_title.append(d)
            counter+=1
    df = pd.DataFrame(news_title)
    print(news_title)
    df.to_csv('scraped_data2.csv', index=False,encoding='utf-8-sig')
    """with open("title.csv", "w",newline='',encoding='utf-8') as f:
        w = csv.DictWriter(f,['id', 'title'])
        w.writeheader()
        w.writerow(news_title)"""
    
except Exception as e:
    print(e)
    
    