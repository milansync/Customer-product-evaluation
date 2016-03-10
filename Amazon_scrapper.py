import requests
from bs4 import BeautifulSoup
import json
import pprint

url="http://www.amazon.in/product-reviews/B00O4WTN9E/ref=cm_cr_dp_see_all_summary?ie=UTF8&showViewpoints=1&sortBy=byRankDescending"
r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
span = soup.findAll('span', attrs={'class': 'a-size-base review-text'})
a=dict()
i=0
for spans in span:
   print spans.text
   a[i]=spans.text
   i=i+1
fil=open('iphone6_amazon.json','w')
json.dump(a, fil)  
   
