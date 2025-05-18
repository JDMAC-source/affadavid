import requests
import time


import feedparser
from requests import get

base = ""
urls = ["http://www.latimes.com/politics/rss2.0.xml", "https://www.latimes.com/health/rss2.0.xml", "https://www.latimes.com/science/rss2.0.xml", "https://www.latimes.com/style/rss2.0.xml", "https://www.latimes.com/environment/rss2.0.xml#nt=1col-7030col1", "https://www.latimes.com/food/rss2.0.xml", "https://www.latimes.com/entertainment/rss2.0.xml", "https://www.latimes.com/sports/rss2.0.xml"]
# more writing
urls1 = ["https://www.latimes.com/opinion/rss2.0.xml#nt=1col-7030col1", "https://www.latimes.com/obituaries/rss2.0.xml#nt=1col-7030col1", "https://www.latimes.com/topic/education.rss", "https://www.latimes.com/topic/fires.rss", "https://www.latimes.com/homeless-housing.rss", "https://www.latimes.com/entertainment-arts/movies/rss2.0.xml#nt=1col-7030col1", "https://www.latimes.com/entertainment-arts/tv/rss2.0.xml#nt=1col-7030col1"]
# more writing
urls2 = ["https://www.latimes.com/topic/earthquakes.rss", "https://www.latimes.com/entertainment-arts/awards/rss2.0.xml#nt=1col-7030col1", "https://www.youtube.com/feeds/videos.xml?channel_id=UC-BlDCX__nCLs_ZF9meYQbw&x=1", "https://budgetsaresexy.com/feed/", "https://family-budgeting.co.uk/feed/", "https://becentsational.com/feed/", "https://www.booandmaddie.com/category/home-life/feed/"]

urls3 = ["https://www.thehomelife.co.uk/feed/", "https://www.ukhomeimprovement.co.uk/feed/", "https://www.totallandscapecare.com/feed", "https://www.lawnandlandscape.com/rss/", "https://feeds.feedburner.com/landscapemanagementpro", "https://www.turfmagazine.com/feed/", "https://www.prolandscapermagazine.com/feed/", "http://www.twostylishkays.com/feeds/posts/default"]

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


