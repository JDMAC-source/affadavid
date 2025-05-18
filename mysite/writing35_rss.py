import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://cybersecurity.att.com/site/blog-all-rss", "https://www.news18.com/rss/business.xml", "https://www.news18.com/rss/entertainment.xml", "https://www.news18.com/rss/lifestyle.xml", "https://www.news18.com/rss/tech.xml", "https://www.news18.com/rss/politics.xml", "https://www.news18.com/rss/education-career.xml", "https://www.news18.com/rss/opinion.xml", "https://www.news18.com/rss/sports.xml"]
# more writing
urls2 = ["https://www.news18.com/rss/markets.xml", "https://www.news18.com/rss/explainers.xml", "https://www.news18.com/rss/football.xml", "https://www.news18.com/rss/breaking-news.xml", "https://www.news18.com/rss/tax.xml", "https://www.news18.com/rss/hockey.xml", "https://www.news18.com/rss/astrology.xml", "https://www.news18.com/rss/auto.xml", "https://www.news18.com/rss/web-stories.xml", "https://www.news18.com/rss/formula-one.xml"]

urls3 = ["https://www.lindaikejisblog.com/feed", "https://www.bellanaija.com/feed/", "https://www.naijanews.com/feed/", "https://www.uncleakin.com/feeds/posts/default", "https://www.naijabulletin.com/feed/", "https://diazhub.com/feed/", "https://notjustok.com/feed/", "https://www.gistlover.com/feed/", "https://newsonlineng.com/feed/", "https://goldennewsng.com/feed/", "https://thenewsguru.com/feed/"]


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



