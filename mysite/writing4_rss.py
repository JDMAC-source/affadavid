import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.powerofpositivity.com/feed/", "https://sholarichards.com/feed/", "https://www.marktechpost.com/feed/", "https://www.unite.ai/feed/", "https://hanhdbrown.com/feed/", "https://dailyai.com/feed/", "https://aiquantumintelligence.com/feed/", "https://www.technologyreview.com/topic/artificial-intelligence/feed", "http://www.kdnuggets.com/feed", "https://nanonets.com/blog/rss/", "https://www.artificiallawyer.com/feed/", "https://blog.marekrosa.org/feeds/posts/default", "https://aihub.org/feed/?cat=-473", "https://besthomesandkitchens.com/feed/"]
# more writing
urls1 = ["https://www.digitalmediatrend.com/feed/", "https://researchsnipers.com/feed/", "https://textalks.com/feed/", "https://a-sports.tv/feed/", "https://www.myvirtualjourney.com/feed/", "https://www.youtube.com/feeds/videos.xml?channel_id=UCbbgUXmCq-6tsCQQmWsQkOg", "https://www.youtube.com/feeds/videos.xml?channel_id=UCiWrjBhlICf_L_RK5y6Vrxw", "https://www.youtube.com/feeds/videos.xml?channel_id=UCarQwI55y9yLxbQOsOkG9cw", "https://www.youtube.com/feeds/videos.xml?channel_id=UCuqBZWK9Wrol_4Y22DzisFQ", "https://www.youtube.com/feeds/videos.xml?channel_id=UC0Mpd1WnxCz9PXCZZjBVGOQ", "https://www.sianvictoria.com/blog?format=rss"]
# more writing
urls2 = ["http://www.birminghammail.co.uk/?service=rss", "https://theironroom.wordpress.com/feed/", "https://www.birminghamworld.uk/news/rss", "https://www.mlbtraderumors.com/feed", "https://blogs.fangraphs.com/feed/", "https://razzball.com/feed/", "https://d1baseball.com/feed/", "https://diamondnotes.substack.com/feed", "https://www.yardbarker.com/rss/sport_merged/1", "https://www.baseballprospectus.com/feed/", "https://www.royalsreview.com/rss/current", "https://www.draysbay.com/rss/index.xml", "https://www.batterypower.com/rss/index.xml", "https://www.southsidesox.com/rss", "https://www.gaslampball.com/rss/current"]


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