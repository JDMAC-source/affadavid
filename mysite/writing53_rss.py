import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.archanaskitchen.com/?format=feed&type=atom", "https://mytastycurry.com/feed", "https://www.youtube.com/feeds/videos.xml?channel_id=UCmoX4QULJ9MB00xW4coMiOw&x=1", "https://www.youtube.com/feeds/videos.xml?channel_id=UC_R8qIXaTKpkAJuuiZhHTmA&x=1", "https://www.youtube.com/feeds/videos.xml?channel_id=UCg_QZ-5-zU6eQjxIHjnyqQg", "http://www.archdaily.com/feed/rss/", "https://architizer.wpengine.com/feed/"]
# more writing
urls1 = ["https://www.dezeen.com/feed/", "https://www.archpaper.com/feed", "https://www.decoist.com/feed/", "https://www.designboom.com/feed/", "http://www.architecturalrecord.com/rss/articles", "https://feeds.feedburner.com/contemporist", "https://bestcafedesigns.com/feed/", "https://www.architectsjournal.co.uk/feed", "https://feeds.feedburner.com/architecturelab", "https://buildingandinteriors.com/feed/"]
# more writing
urls2 = ["http://archeyes.com/feed", "https://bustler.net/feed", "https://brandondonnelly.com/feed/", "https://www.avontuura.com/feed/", "http://www.urbanrealm.com/rss", "https://www.archiseek.com/feed/", "https://worldarchitecture.org/blogs/wanews/rss/", "https://zeenews.india.com/rss/india-national-news.xml", "https://zeenews.india.com/rss/world-news.xml", "https://zeenews.india.com/rss/business.xml"]

urls3 = ["https://zeenews.india.com/rss/sports-news.xml", "https://zeenews.india.com/rss/entertainment-news.xml", "https://zeenews.india.com/rss/technology-news.xml", "https://www.baunetz-id.de/rss-latest.xml", "http://design-milk.com/feed/", "https://www.designboom.com/feed/", "https://www.dezeen.com/feed", "https://www.printmag.com/blog-feed.xml", "https://www.hongkiat.com/blog/feed/", "https://www.creativebloq.com/feed?x=1"]

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


