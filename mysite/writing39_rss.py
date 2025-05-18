import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.sahilonline.net/rss/ur/latest", "https://news1india.in/feed/", "https://krooknews.com/feed/", "http://feeds.indiasnews.net/rss/701ee96610c884a6", "https://www.pioneeredge.in/feed/", "https://www.ndnewsexpress.com/feed/", "https://theindiabizz.com/feed/", "https://www.assamtimes.org/rss.xml", "https://www.smarttechtoday.com/feed/", "https://www.indiavision.com/feed/"]
# more writing
urls1 = ["https://prod-qt-images.s3.amazonaws.com/production/thequint/feed.xml", "https://techgenyz.com/feed/", "https://newsblare.com/feed/", "https://arunachaltimes.in/index.php/feed/", "https://thelivenagpur.com/feed/", "http://bilkulonline.com/feed/", "https://latestnewsupdate4you.blogspot.com/feeds/posts/default", "https://risingkashmir.com/feed/", "https://odishabarta.com/feed/"]
# more writing
urls2 = ["https://www.marketingdive.com/feeds/news/", "https://www.dmnews.com/feed/", "https://www.adweek.com/rss/", "https://www.socialmediatoday.com/feeds/news/", "https://feeds.feedburner.com/CMSWire", "https://www.searchenginejournal.com/feed/atom/", "http://feeds.mediapost.com/mediadailynews", "https://marcommnews.com/feed/"]

urls3 = ["https://www.mediaupdate.co.za/feed", "https://digiday.com/feed/", "https://www.socialmediaexaminer.com/feed/", "https://brandequity.economictimes.indiatimes.com/rss/marketing", "https://feeds.feedburner.com/ausretrogamer/usYt", "https://www.indieretronews.com/feeds/posts/default?alt=rss", "https://www.oldschoolgamermagazine.com/feed/", "https://www.arcadeattack.co.uk/feed/"]

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


