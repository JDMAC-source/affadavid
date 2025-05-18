import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://deadline.com/feed/", "http://www.vanityfair.com/rss", "https://perezhilton.com/feed/", "https://www.bollywoodlife.com/feed/", "http://www.justjared.com/feed/", "https://stylecaster.com/feed/", "https://realityblurb.com/feed/", "https://balleralert.com/feed/", "https://feeds.feedburner.com/bossiprss", "http://www.glamourmagazine.co.uk/rss", "https://thejasminebrand.com/feed/", "https://www.celebitchy.com/feed/"]
# more writing
urls1 = ["https://sandrarose.com/feed/", "https://www.thehollywoodgossip.com/feed", "https://www.gofugyourself.com/feed", "https://www.intouchweekly.com/?feed=posts-p1", "https://www.lifeandstylemag.com/?feed=posts-p1", "https://www.jimmystarsworld.com/feed/", "https://ohnotheydidnt.livejournal.com/data/rss/", "https://bckonline.com/feed/", "https://www.femalefirst.co.uk/celebrities/rss", "https://www.wesmirch.com/feed.xml", "https://gossipbucket.com/feed/", "https://feeds.extratv.com/atom/"]
# more writing
urls2 = ["https://feeds.toofab.com/atom", "https://w-newz.blogspot.com/feeds/posts/default?alt=rss", "https://rsvpmagazine.ie/feed", "http://www.cambio.com/rss.xml", "https://www.allabouttrh.com/feed/", "https://ohmygossip.nordenbladet.com/feed", "https://hushhushbiz.com/feed/", "https://honkmagazine.com/feed/", "https://www.youtube.com/feeds/videos.xml?channel_id=UCotI-SqRXnkAZX4bMqlRNjw&x=1", "https://www.youtube.com/feeds/videos.xml?channel_id=UCdtXPiqI2cLorKaPrfpKc4g&x=1"]

urls3 = ["https://www.youtube.com/feeds/videos.xml?channel_id=UCXTcOUK4-Oy933BDO3DbXLQ", "https://www.youtube.com/feeds/videos.xml?channel_id=UCP1hdrxYHdebGqbQawOMRpQ", "https://www.youtube.com/feeds/videos.xml?channel_id=UCZF0z6CyEs_e_IXaB57xqSA", "https://www.youtube.com/feeds/videos.xml?channel_id=UCdILIiuXr2UQUhc5SFVbKtw", "https://www.youtube.com/feeds/videos.xml?channel_id=UCbY6-Gp0aEHJpS9vPtcKWeA", "https://www.youtube.com/feeds/videos.xml?channel_id=UChJfh0Y4ycfMbf2SHQzRasg"]

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


