import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://ottawacitizen.com/feed/", "https://www.stratfordbeaconherald.com/feed", "https://www.straight.com/content/rss", "https://www.dailyheraldtribune.com/feed", "https://ygknews.ca/feed/", "https://paherald.sk.ca/feed/", "https://westernstandardonline.com/feed/", "http://www.sunnysouthnews.com/feed/", "https://www.pembrokeobserver.com/category/news/local-news/feed", "https://www.cjnews.com/feed"]
# more writing
urls1 = ["https://www.thecanadianpressnews.ca/search/?f=rss", "https://defence-blog.com/category/news/army/feed/", "https://www.army-technology.com/feed/", "https://www.ausa.org/news/rss.xml", "https://www.lebarmy.gov.lb/en/rss.xml", "https://allthingsnuclear.org/feed/", "https://nuclear-news.net/feed/", "https://www.ans.org/news/feed/", "https://www.world-nuclear-news.org/?rss=feed", "https://www.nucnet.org/feed.rss"]
# more writing
urls2 = ["https://www.accountingtoday.com/feed?rss=true", "https://studycafe.in/feed/", "https://www.intuitiveaccountant.com/api/rss/content.rss", "https://goingconcern.com/feed/", "https://www.cbh.com/guide/feed/", "https://www.freechurchaccounting.com/church-accounting.xml", "https://www.rfa.org/english/RSS", "https://thediplomat.com/feed"]

urls3 = ["https://asiatimes.com/feed/", "https://e27.co/index_wp.php/feed/", "https://www.channelnewsasia.com/rssfeeds/8395986", "https://www.asiasentinel.com/feed/", "http://www.scmp.com/rss/91/feed", "https://asean.org/feed/", "https://www.campaignasia.com/RSS/rss.ashx?type=Category&ID=718", "https://www.digitalnewsasia.com/rss.xml", "https://splash247.com/category/region/asia/feed/"]

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


