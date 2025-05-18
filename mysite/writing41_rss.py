import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.thenorthernecho.co.uk/news/rss/", "https://www.theboltonnews.co.uk/news/rss/", "https://www.portsmouth.co.uk/rss/cmlink/1.7167516", "https://www.thescarboroughnews.co.uk/rss", "https://www.larnetimes.co.uk/news/rss", "https://www.walesonline.co.uk/?service=rss", "https://www.thepoke.co.uk/feed/", "https://www.heraldscotland.com/news/rss/", "https://www.belfastlive.co.uk/?service=rss", "https://www.newsuk1.com/feeds/posts/default"]
# more writing
urls1 = ["http://www.cambridge-news.co.uk/rss.xml", "https://www.irishtimes.com/cmlink/news-1.1319192", "https://www.grimsbytelegraph.co.uk/news/?service=rss", "https://www.glasgowtimes.co.uk/news/rss/", "https://www.necn.com/?rss=y", "https://www.deadlinenews.co.uk/feed/", "https://www.positive.news/feed/", "https://londonjournal.co.uk/feed/", "https://consettmagazine.com/feed/", "https://www.thedailymash.co.uk/feed", "https://www.scotsman.com/news/rss"]
# more writing
urls2 = ["https://feeds.breakingnews.ie/bntopstories", "https://www.thescottishsun.co.uk/feed/", "https://www.scottishfield.co.uk/feed/", "https://www.huffingtonpost.co.uk/feeds/index.xml", "https://www.dailyecho.co.uk/news/rss/", "https://www.kentnews.online/feed/", "https://www.northernirelandworld.com/news/rss", "https://www.theguardian.com/politics/conservative-leadership/rss", "https://softwareengineeringdaily.com/feed/", "http://feeds.dzone.com/home"]

urls3 = ["https://cdn.hackernoon.com/feed", "https://www.atlassian.com/engineering/feed", "https://engineering.salesforce.com/feed/", "https://www.oreilly.com/radar/feed/index.xml", "https://cointelegraph.com/rss", "https://bitcoinmagazine.com/feed", "https://bitcoinist.com/feed/", "https://www.newsbtc.com/feed", "https://www.coinspeaker.com/feed/", "https://cryptopotato.com/feed", "https://99bitcoins.com/feed/", "https://cryptobriefing.com/feed/"]

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


