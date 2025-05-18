import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.business-standard.com/rss/latest.rss", "https://www.thestreet.com/.rss/full/", "http://feeds.benzinga.com/benzinga", "https://www.marketbeat.com/feed/", "https://money.com/money/feed/", "https://moneyweek.com/feed/all", "https://www.finance-monthly.com/feed/", "https://www.europeanfinancialreview.com/feed/", "https://moneymorning.com/feed/"]
# more writing
urls1 = ["https://cfi.co/feed", "https://dealbreaker.com/.rss/full/", "https://www.finews.com/news/english-news?format=feed&type=rss", "https://www.space.com/home/feed/site.xml", "https://spacenews.com/feed/", "https://www.nasa.gov/rss/dyn/breaking_news.rss", "https://www.astronomy.com/feed/", "https://spaceflightnow.com/feed/", "http://spaceq.ca/feed/"]
# more writing
urls2 = ["https://www.spacedaily.com/spacedaily.xml", 'https://www.sciencenews.org/topic/space/feed', "https://www.cbsnews.com/latest/rss/space", "https://phys.org/rss-feed", "https://www.esa.int/rssfeed/TopNews", "https://earthsky.org/feed/", "https://www.thespacereview.com/articles.xml", "https://www.universetoday.com/feed", "https://www.marsdaily.com/marsdaily.xml"]

urls3 = ["https://skyandtelescope.com/astronomy-news/feed/", "https://feeds.feedburner.com/satelit", "http://www.autoblog.com/rss.xml", "https://www.automotive-fleet.com/rss"]

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


