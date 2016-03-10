import json
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import pprint
import re
from flask import Flask


with open('iphone6_amazon.json') as json_data:
    review = json.load(json_data)
a = str(review)

blob = TextBlob(a)
pos = 0
neg = 0
neu = 0
cam_pos = 0
ram_pos = 0
stor_pos = 0
batt_pos = 0
cam_neg = 0
ram_neg = 0
stor_neg = 0
batt_neg = 0
cam_neu = 0
ram_neu= 0
stor_neu = 0
batt_neu = 0
for sentence in blob.sentences:
    ##print sentence
    ##print sentence.sentiment.polarity
    if(sentence.sentiment.polarity>0):
        pos += 1
    elif(sentence.sentiment.polarity<0):
        neg += 1
    else:
        neu += 1

print pos
print neg
print neu

for sentence in blob.sentences:
   pprint.pprint(sentence)
##   pprint.pprint(sentence.polarity)
   if(sentence.sentiment.polarity>0):
        for word in sentence.words:
            if(word=='camera'):
             cam_pos+= 1
             print "cam"
        for word in sentence.words:
            if((word=='ram')|(word=='RAM')):
               ram_pos+= 1
               print "ram"
        for word in sentence.words:
            if(word=='storage'):
               stor_pos+= 1
               print "stor"
        for word in sentence.words:
            if(word=='battery'):
               batt_pos+= 1
               print "batt"
   elif(sentence.sentiment.polarity<0):
        for word in sentence.words:
            if(word=='camera'):
             cam_neg+= 1
             print "cam"
        for word in sentence.words:
            if((word=='ram')|(word=='RAM')):
               ram_neg+= 1
               print "ram"
        for word in sentence.words:
            if(word=='storage'):
               stor_neg+= 1
               print "stor"
        for word in sentence.words:
            if(word=='battery'):
               batt_neg+= 1
               print "batt"
   else:
        for word in sentence.words:
            if(word=='camera'):
             cam_neu+= 1
             print "cam"
        for word in sentence.words:
            if((word=='ram')|(word=='RAM')):
               ram_neu+= 1
               print "ram"
        for word in sentence.words:
            if(word=='storage'):
               stor_neu+= 1
               print "stor"
        for word in sentence.words:
            if(word=='battery'):
               batt_neu+= 1
               print "batt"

print 'cam_pos='+ str(cam_pos)
print 'cam_pos='+ str(cam_pos) 
print 'stor_pos='+  str(stor_pos) 
print 'batt_pos='+ str(batt_pos)
print 'cam_neg=' + str(cam_neg) 
print 'ram_neg=' +str(ram_neg)
print 'stor_neg='+ str(stor_neg) 
print 'batt_neg='+ str(batt_neg)

def call(positive):
    return positive
##print cam_neu 
##print ram_neu
##print stor_neu 
##print batt_neu
app = Flask(__name__)

@app.route('/')
def index():
    return call(str(cam_pos)+str(cam_neg))

if __name__ == '__main__':
    app.run(debug=True)









def htc():
    with open('HTC-Desire-326g_amazon.json') as json_data:
        review = json.load(json_data)
    a = str(review)

    blob = TextBlob(a)
    pos = 0
    neg = 0
    neu = 0
    cam_pos = 0
    ram_pos = 0
    stor_pos = 0
    batt_pos = 0
    cam_neg = 0
    ram_neg = 0
    stor_neg = 0
    batt_neg = 0
    cam_neu = 0
    ram_neu= 0
    stor_neu = 0
    batt_neu = 0
    for sentence in blob.sentences:
        ##print sentence
        ##print sentence.sentiment.polarity
        if(sentence.sentiment.polarity>0):
            pos += 1
        elif(sentence.sentiment.polarity<0):
            neg += 1
        else:
            neu += 1
    ret=dict()
    review=dict()
    review['pos']=pos
    review['neg']=neg
    review['neu']=neu
    for sentence in blob.sentences:
       pprint.pprint(sentence)
    ##   pprint.pprint(sentence.polarity)
       if(sentence.sentiment.polarity>0):
            for word in sentence.words:
                if(word=='camera'):
                 cam_pos+= 1
                 print "cam"
            for word in sentence.words:
                if((word=='ram')|(word=='RAM')):
                   ram_pos+= 1
                   print "ram"
            for word in sentence.words:
                if(word=='storage'):
                   stor_pos+= 1
                   print "stor"
            for word in sentence.words:
                if(word=='battery'):
                   batt_pos+= 1
                   print "batt"
       elif(sentence.sentiment.polarity<0):
            for word in sentence.words:
                if(word=='camera'):
                 cam_neg+= 1
                 print "cam"
            for word in sentence.words:
                if((word=='ram')|(word=='RAM')):
                   ram_neg+= 1
                   print "ram"
            for word in sentence.words:
                if(word=='storage'):
                   stor_neg+= 1
                   print "stor"
            for word in sentence.words:
                if(word=='battery'):
                   batt_neg+= 1
                   print "batt"
       else:
            for word in sentence.words:
                if(word=='camera'):
                 cam_neu+= 1
                 print "cam"
            for word in sentence.words:
                if((word=='ram')|(word=='RAM')):
                   ram_neu+= 1
                   print "ram"
            for word in sentence.words:
                if(word=='storage'):
                   stor_neu+= 1
                   print "stor"
            for word in sentence.words:
                if(word=='battery'):
                   batt_neu+= 1
                   print "batt"

    spec=dict()
    spec['cam_pos']=cam_pos
    spec['cam_neg']=cam_neg
    spec['stor_pos']=stor_pos
    spec['stor_neg']=stor_neg
    spec['battery_pos']=battery_pos
    spec['battery_neg']=battery_neg
    spec['ram_pos']=ram_pos
    spec['ram_neg']=ram_neg
    ret['review']=review
    ret['spec']=spec
    return ret
    
        
