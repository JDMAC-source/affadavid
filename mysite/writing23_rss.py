import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.freecodecamp.org/news/rss", "http://syndication.thedailywtf.com/TheDailyWtf", "http://feeds.dzone.com/home", "https://aiparabellum.com/feed/", "https://sdtimes.com/feed/", "https://zeenews.india.com/rss/india-national-news.xml", "https://zeenews.india.com/rss/world-news.xml", "https://zeenews.india.com/rss/business.xml", "https://zeenews.india.com/rss/sports-news.xml", "https://zeenews.india.com/rss/entertainment-news.xml", "https://zeenews.india.com/rss/technology-news.xml", "https://www.wired.com/feed/category/business/latest/rss"]
# more writing
urls1 = ["https://www.wired.com/feed/category/science/latest/rss", "https://www.wired.com/feed/category/gear/latest/rss", "https://www.wired.com/feed/category/culture/latest/rss", "https://www.wired.com/feed/category/security/latest/rss", "https://www.wired.com/feed/category/transportation/latest/rss", "https://www.wired.com/feed/category/backchannel/latest/rss", "http://ep01.epimg.net/rss/elpais/inenglish.xml", "https://e00-elmundo.uecdn.es/rss/portada.xml", "https://www.eldiario.es/rss", "https://feeds.thelocal.com/rss/es"]
# more writing
urls2 = ["https://euroweeklynews.com/feed/", "https://www.theolivepress.es/feed/", "https://eldiariony.com/feed/", "https://www.majorcadailybulletin.com/feed.rss", "https://theleader.info/feed/", "https://www.butterword.com/feeds/posts/default", "https://www.theseasidegazette.com/feed/", "http://feeds.hbr.org/harvardbusiness", "https://www.entrepreneur.com/latest.rss", "https://www.fastcompany.com/latest/rss?truncated=true", "http://feeds.feedburner.com/SmallBusinessTrends/?feedId=220&uuid=JHEFJFpFDDIDMFLEDIDEFpFDMBEKEBHDBEDD"]

urls3 = ["https://www.inc.com/rss/", "https://techcrunch.com/feed/", "https://smallbusinessbonfire.com/feed/", "https://www.godaddy.com/resources/feed", "https://www.bloomberg.com/professional/feed/", "https://learn.g2crowd.com/rss.xml", "https://www.businessoffashion.com/arc/outboundfeeds/rss/?outputType=xml", "https://www.youngupstarts.com/feed/", "https://www.foodbusinessnews.net/rss/articles", "http://talkingbiznews.com/feed/", "https://www.bluewiremedia.com.au/blog/feed", "https://www.businessblogshub.com/feed/"]

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


