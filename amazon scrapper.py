import requests
from bs4 import BeautifulSoup



url = "http://www.amazon.in/Google-Nexus-D821-16GB-Black/dp/B00GC1J55C/ref=sr_1_1?ie=UTF8&qid=1441120927&sr=8-1&keywords=nexus+5"
r = requests.get(url)
soup = BeautifulSoup(r.content,'lxml')
div = soup.findAll('div', attrs={'id': 'customer-reviews_feature_div'})

for divs in div:
  divs = soup.findAll('div', attrs={'id': 'a-section'})
  print divs
