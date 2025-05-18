import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.agweek.com/index.rss", "https://www.brownfieldagnews.com/feed/", "https://www.producer.com/feed/", "https://www.realagriculture.com/feed/", "https://americanagnetwork.com/feed/", "https://agnetwest.com/feed/", "https://krishijagran.com/feeds/rss", "https://agupdate.com/search/?f=rss", "https://www.brownfieldagnews.com/feed/"]
#insurance
urls1 = ["https://www.insurancebusinessmag.com/us/rss/", "https://www.artemis.bm/news/feed/", "https://agencychecklists.com/feed/"]
#1 of statistics then _heavy equipment_ nope, okay, uk farming, yay 2... sustainability x2 ... beef x1 ... commodities then SA farming.
urls2 = ["https://statanalytica.com/blog/feed/", "https://www.farminguk.com/RSS/News", "https://www.farmersguide.co.uk/feed/", "https://www.ecowatch.com/feed", "https://earth911.com/feed/", "https://www.beefcentral.com/feed/", "https://oilprice.com/rss/main", "https://economictimes.indiatimes.com/markets/commodities/rssfeeds/1808152121.cms", "https://www.thehindubusinessline.com/markets/commodities/?service=rss", "https://investingnews.com/category/daily/resource-investing/base-metals-investing/copper-investing/feed/", "https://goldsilver.com/industry-news/rss/", "https://www.worldoil.com/rss?feed=news", "https://feeds.feedburner.com/blogspot/LKbcZ", "https://www.farmersweekly.co.za/feed/"]

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




