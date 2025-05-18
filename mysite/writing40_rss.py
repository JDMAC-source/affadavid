import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://infinityretro.com/feed/", "https://retrododo.com/feed/", "https://www.kdnuggets.com/feed", "https://www.snowflake.com/feed/", "https://www.precisely.com/feed", "https://aws.amazon.com/blogs/big-data/feed/", "https://towardsdatascience.com/feed", "https://hevodata.com/learn/feed/", "https://feed.infoq.com/ai-ml-data-eng/", "https://www.immigration.ca/feed/", "https://www.smalldeadanimals.com/feed/", "https://immigcanada.com/feed/"]
# more writing
urls1 = ["https://www150.statcan.gc.ca/n1/rss/dai-quo/0-eng.atom", "https://www.printaction.com/feed/", "https://triathlonmagazine.ca/feed/", "https://www.wingsmagazine.com/feed/", "https://www.benefitscanada.com/feed/", "https://www.renewcanada.net/feed/", "https://www.iphoneincanada.ca/feed/", "https://www.cicnews.com/feed", "https://www.helicoptersmagazine.com/feed/", "https://www.automationmag.com/feed/", "https://www.canadiansecuritymag.com/feed/"]
# more writing
urls2 = ["https://runningmagazine.ca/feed/", "https://thecjn.ca/feed/", "https://www.foodincanada.com/feed/", "https://feeds.skynews.com/feeds/rss/home.xml", "http://www.independent.co.uk/rss", "http://www.huffingtonpost.co.uk/feeds/index.xml", "https://www.dailyrecord.co.uk/news/?service=rss", "https://www.thesun.co.uk/topic/conservative-leadership-contest/feed/", "https://www.politics.co.uk/feed/"]

urls3 = ["https://www.mirror.co.uk/?service=rss", "http://www.standard.co.uk/rss", "http://theconversation.com/uk/articles.atom", "https://www.manchestereveningnews.co.uk/?service=rss", "https://feeds.feedburner.com/daily-express-news-showbiz", "https://metro.co.uk/feed/", "https://www.birminghammail.co.uk/?service=rss", "https://www.theargus.co.uk/news/rss/", "https://www.pinknews.co.uk/feed/", "https://www.yorkpress.co.uk/news/rss/"]

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


