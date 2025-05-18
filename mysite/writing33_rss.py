import requests
import time


import feedparser
from requests import get

base = ""
urls = ["http://feeds.trendmicro.com/TrendMicroResearch", "https://www.bleepingcomputer.com/feed"]
# more writing
urls1 = ["http://www.techrepublic.com/rssfeeds/topic/security/?feedType=rssfeeds", "https://heimdalsecurity.com/blog/feed/", "http://securityaffairs.co/wordpress/feed", "https://www.tripwire.com/state-of-security/feed/", "https://www.secpod.com/blog/feed/", "https://www.cyberdefensemagazine.com/feed/", "https://socprime.com/feed/", "https://www.lastwatchdog.com/feed/", "https://any.run/cybersecurity-blog/feed/", "https://www.helpnetsecurity.com/feed/", "https://www.cm-alliance.com/cybersecurity-blog/rss.xml"]
# more writing
urls2 = ["https://www.wsj.com/xml/rss/3_7455.xml", "https://www.wsj.com/xml/rss/3_7014.xml", "https://www.wsj.com/xml/rss/3_7041.xml", "https://www.wsj.com/xml/rss/3_7085.xml", "https://www.johndcook.com/blog/feed/", "https://www.technologyreview.com/feed/", "https://terrytao.wordpress.com/feed/", "https://towardsdatascience.com/feed", "https://egyptian-gazette.com/technology/feed/", "https://startuptalky.com/rss/", "https://startupreporter.in/feed/", "https://officechai.com/feed/", "https://entrackr.com/feed/"]

urls3 = ["https://inc42.com/feed/", "https://yourstory.com//feed", "https://www.indianweb2.com/feeds/posts/default", "http://www.autoblog.com/rss.xml", "https://www.automotive-fleet.com/rss", "https://www.am-online.com/news/latest-news/rss.xml", "https://www.automotiveaddicts.com/feed"]

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


