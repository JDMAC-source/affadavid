import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.vortez.net/news_rss", "https://tftcentral.co.uk/feed", "https://thinkcomputers.org/feed/", "https://wccftech.com/topic/hardware/feed/", "https://www.igorslab.de/en/feed/", "https://www.techpowerup.com/rss/reviews", "https://feeds.feedburner.com/VideoCardzcom", "https://www.pcworld.com/feed", "https://www.fierceelectronics.com/rss/xml", "https://www.gas-sensing.com/news/feed/", "https://feeds.feedburner.com/SensorTips", "https://www.portugal.com/feed/"]
# more writing
urls1 = ["https://www.bocadolobo.com/blog/category/furniture/feed/", "https://primeeventos.com.br/feed/", "https://www.blogdoscruzeiros.com/feed/", "https://www.funchaldailyphoto.com/feeds/posts/default", "https://feeds.feedburner.com/tympanus", "https://edpamanu.blogspot.com/feeds/posts/default?alt=rss", "https://susannedrechsler.wordpress.com/feed/", "https://tympanus.net/codrops/feed/", "http://mixologynews.com.br/feed/", "http://blog.winetourismportugal.com/rss.xml", "https://www.youtube.com/feeds/videos.xml?channel_id=UCw0V33yTFGA5iEujve75zwQ"]
# more writing
urls2 = ["https://www.youtube.com/feeds/videos.xml?channel_id=UCq-4yNTWjFcAj_iFTTmv4Aw", "https://www.youtube.com/feeds/videos.xml?channel_id=UCXmR58tBJnQD0qvz6t_noTA", "https://theintellify.com/feed/", "https://www.youtube.com/feeds/videos.xml?channel_id=UCutPI2lji_hFToXec7qOCFA", "https://www.forbes.com/innovation/feed2", "https://feeds.feedburner.com/intelnewsroom", "http://feeds.feedburner.com/RenewableEnergyNewsRssFeed", "https://cleantechnica.com/feed/", "https://www.altenergymag.com/rss/news", "http://www.carbonbrief.org/rss"]

urls3 = ["https://www.exaputra.com/feeds/posts/default", "https://www.eservices4u.com.au/blog-feed.xml", "https://solarindustrymag.com/feed", "https://www.2greenenergy.com/blog/feed/", "http://cleantechies.com/feed/", "https://www.theguardian.com/environment/renewableenergy/rss", "http://feeds.mashable.com/mashable", "http://feeds.mashable.com/mashable/entertainment", "https://mashable.com/culture/feed/", "http://feeds.mashable.com/mashable/tech", "https://mashable.com/category/social-good/feed/", "https://dev.to/feed"]

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


