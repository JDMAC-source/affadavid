import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://feeds.content.dowjones.io/public/rss/mw_topstories", "https://www.fool.co.uk/feed/", "https://smallcaps.com.au/feed/", "https://stockhead.com.au/feed/", "https://www.raskmedia.com.au/feed/", "https://www.fool.com.au/feed/", "http://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms", "http://www.fool.ca/feed/", "https://www.financebrokerage.com/feed/", "http://www.calculatedriskblog.com/feeds/posts/default", "https://www.equitypandit.com/feed/", "https://www.guerillastocktrading.com/feed/", "https://www.shareandstocks.com/feed/", "http://bullsonwallstreet.com/feed/", "https://www.marketbeat.com/rss.ashx?type=headlines"]
urls1 = [""]
urls2 = ["https://www.investing.com/rss/news.rss", "https://seekingalpha.com/market_currents.xml"]

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




'''
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
'''



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
        print(item.link)
        
        r = requests.post('https://www.predictionary.us/B/posts/',data={'title':item.title, "body":item.link, "url2": item.link})
        
        print(r.status_code)
        print(r.text)




