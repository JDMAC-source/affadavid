import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://notayesmanseconomics.wordpress.com/feed/", "https://tinybuddha.com/feed", "https://goodemma.com/feed/", "https://beherenownetwork.com/feed/", "https://mindfulbalance.org/feed/", "https://gentwenty.com/feed/", "https://news.usni.org/feed", "https://www.marinelink.com/news/rss", "https://www.maritime-executive.com/articles.rss", "https://www.bairdmaritime.com/feed/", "https://mfame.guru/category/maritime-news/feed/", "https://africaports.co.za/feed/", "https://www.gearnews.com/manufacturer/fender/feed/", "https://blog.rosettastone.com/feed/", "https://feeds.acast.com/public/shows/66068dc22d276f001657edb1"]
# more writing
urls1 = ["https://www.turkishclass101.com/feed", "https://www.olesentuition.co.uk/blog-feed.xml", "https://www.youtube.com/feeds/videos.xml?channel_id=UCesZBmRS6IgZ3uuiB8RdX0A&x=1", "https://tarunbharat.com/feed/", "https://suryakantdolase.blogspot.com/feeds/posts/default", "https://www.e-abhivyakti.com/feed/", "https://prahaar.in/feed/", "https://nagarchaufer.com/?feed=rss2", "https://pudhari.news/feed", "https://ww2.kqed.org/mindshift/feed/", "http://feeds.feedburner.com/elearningindustry", "https://www.weareteachers.com/feed", "https://www.nytimes.com/section/learning/rss.xml"]

urls0 = ["http://www.insidehighered.com/rss/feed/ihe", "https://feeds.megaphone.fm/KAP3710732955"]

# more writing
urls2 = ["https://larryferlazzo.edublogs.org/feed/", "https://hechingerreport.org/feed/", "https://www.edtechreview.in/feed/", "https://www.gettingsmart.com/feed/", "https://edsource.org/feed/atom", "http://www.eschoolnews.com/feed/", "http://www.middleweb.com/feed/", "https://classtechtips.com/feed/", "https://dianeravitch.net/feed/", "https://caffeinatedrage.com/feed/", "https://www.theguardian.com/teacher-network/rss", "https://www.christiantoday.com/rss", "http://www.thinkinganglicans.org.uk/feed/rdf/", "https://astepfwd.com/feed", "https://www.premierchristianity.com/2055.rss"]


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

# no .link
for rss_url in urls0:
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
        
        r = requests.post('https://www.predictionary.us/B/posts/',data={'title':item.title, "body":item.summary})
        
        print(r.status_code)
        print(r.text)
