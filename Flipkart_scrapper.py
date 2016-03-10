import requests
from bs4 import BeautifulSoup
import json
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

url="http://www.flipkart.com/apple-iphone-6/p/itme8dvfeuxxbm4r?pid=MOBEYHZ2YAXZMF2J&ref=L%3A-1437727426119711085&srno=p_2&query=iphone+6&otracker=from-search"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
print soup.content
span = soup.findAll('span', attrs={'class': 'review-text'})
a=dict()
i=0
for spans in span:
   print spans.text
   a[i]=spans.text
   i=i+1
   
fil=open('iphone6.json','w')
json.dump(a, fil)


    

  



