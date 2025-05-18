import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.flyingpenguin.com/?feed=rss2", "https://www.secureblink.com/rss-feeds/threat-feed", "https://www.theguardian.com/technology/data-computer-security/rss", "https://www.fiercebiotech.com/rss/biotech/xml", "https://www.labiotech.eu/feed/", "https://bioengineer.org/feed/", "https://www.biopharmadive.com/feeds/news/", "https://feeds.feedburner.com/GenGeneticEngineeringAndBiotechnologyNews", "https://www.nature.com/subjects/biotechnology.rss", "https://www.sciencedaily.com/rss/plants_animals/biotechnology.xml", "https://phys.org/rss-feed/biology-news/biotechnology/"]
# more writing
urls1 = ["https://endpts.com/feed/", "https://www.rand.org/blog.topic.biotechnology.html.xml", "https://bio.news/feed/"]
# more writing



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


