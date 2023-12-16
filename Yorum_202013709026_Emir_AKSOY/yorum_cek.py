import requests 
from bs4 import BeautifulSoup   
import csv 
import pandas as pd
comments = []
try:
    r = requests.get('https://www.haber7.com/yorum/oku/3374084') 
    soup = BeautifulSoup(r.content, 'html.parser') 
    for i in soup.find_all('li',class_='news-comment-list-content'):
        d = {}
        comment = i.find('div',class_='content').text.strip()
        d['comment'] = comment
        comments.append(d)
        print(comment)
    df = pd.DataFrame(comments)
    df.to_csv('news-comment-list.csv',index=True,encoding='utf-8-sig')
except Exception as e :
    print("Hata:"+e)