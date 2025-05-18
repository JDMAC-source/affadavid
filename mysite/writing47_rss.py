import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://thenewsmill.com/feed/", "http://tehelka.com/feed/", "https://thenewshimachal.com/feed/", "https://indiaobservers.com/feed/", "https://startupreporter.in/feed/", "https://eastasiaforum.org/feed/", "https://newsnblogs.com/feed/", "https://hrmasia.com/feed/", "https://newsin.asia/feed/", "https://nwasianweekly.com/feed/", "https://www.financeasia.com/rss/latest", "https://www.asianmilitaryreview.com/feed/", "http://asiasamachar.com/feed/"]
# more writing
urls1 = ["https://thewallet.com.pk/feed", "https://theasialive.com/feed", "https://vosa.tv/feed/", "https://www.indothainews.com/feed/", "https://www.retailnews.asia/feed/", "https://www.asianexpress.co.uk/feed/", "https://transasianews.com/rss.xml", "https://flatteredwithflutter.com/feed/", "https://www.finegardening.com/feed", "http://feeds.feedburner.com/GardenTherapy", "https://www.epicgardening.com/blog/feed"]
# more writing
urls2 = ["https://gardenerspath.com/feed/", "https://www.gardenista.com/rss/", "https://growagoodlife.com/feed/", "http://growinginthegarden.com/feed", "https://gardenrant.com/feed/atom", "https://lisasgardenadventureinoregon.blogspot.com/feeds/posts/default?alt=rss", "https://harvesttotable.com/feed/", "https://oldworldgardenfarms.com/feed/", "https://www.youtube.com/feeds/videos.xml?channel_id=UCfJl4Yf0MrI2RIkqnoHe8rA&x=1"]

urls3 = ["https://www.youtube.com/feeds/videos.xml?channel_id=UCMTIngNCfZOlfT83hEkMR1Q&x=1", "https://balconygardenweb.com/feed/", "https://homeyimprovements.com/feed/", "https://homeimprovementblogs.com/hg-blog/feed/", "http://allenrothhq.com/blog/feed/", "https://www.remodelista.com/feed/", "https://stylebyemilyhenderson.com/feed", "https://feeds.feedburner.com/feedburner/SeNU", "https://blog.renovationfind.com/feed/", "https://mycoastalwindows.com/feed/"]

for rss_url in urls:
    xml = base + rss_url

    # Limit feed output to 5 items
    # To disable limit simply do not provide the argument or use None
    feed = feedparser.parse(xml)
    # Print out feed meta data
    
    count = 0
    # Iteratively print feed items
    for item in feed.entries:
        print(xml + "  " + str(count))
        count += 1
        print(item.title)
        print(item.summary)
        
        r = requests.post('https://www.predictionary.us/B/posts/',data={'title':item.title, "body":item.summary, "url2": item.link})
        
        print(r.status_code)
        print(r.text)



for rss_url in urls1:
    xml = base + rss_url

    # Limit feed output to 5 items
    # To disable limit simply do not provide the argument or use None
    feed = feedparser.parse(xml)
    # Print out feed meta data
    
    count = 0
    # Iteratively print feed items
    for item in feed.entries:
        print(xml + "  " + str(count))
        count += 1
        print(item.title)
        print(item.summary)
        
        r = requests.post('https://www.predictionary.us/B/posts/',data={'title':item.title, "body":item.summary, "url2": item.link})
        
        print(r.status_code)
        print(r.text)


for rss_url in urls2:
    xml = base + rss_url

    # Limit feed output to 5 items
    # To disable limit simply do not provide the argument or use None
    feed = feedparser.parse(xml)
    # Print out feed meta data
    
    count = 0
    # Iteratively print feed items
    for item in feed.entries:
        print(xml + "  " + str(count))
        count += 1
        print(item.title)
        print(item.summary)
        
        r = requests.post('https://www.predictionary.us/B/posts/',data={'title':item.title, "body":item.summary, "url2": item.link})
        
        print(r.status_code)
        print(r.text)



for rss_url in urls3:
    xml = base + rss_url

    # Limit feed output to 5 items
    # To disable limit simply do not provide the argument or use None
    feed = feedparser.parse(xml)
    # Print out feed meta data
    
    count = 0
    # Iteratively print feed items
    for item in feed.entries:
        print(xml + "  " + str(count))
        count += 1
        print(item.title)
        print(item.summary)
        
        r = requests.post('https://www.predictionary.us/B/posts/',data={'title':item.title, "body":item.summary, "url2": item.link})
        
        print(r.status_code)
        print(r.text)


