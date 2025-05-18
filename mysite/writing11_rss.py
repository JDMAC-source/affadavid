import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://greenchristian.org.uk/blog/feed/", "https://devotionaltreasure.wordpress.com/feed/", "https://techcrunch.com/feed/", "http://www.theverge.com/rss/frontpage", "https://www.wired.com/feed/rss", "https://mashable.com/feeds/rss/all", "https://gizmodo.com/rss", "https://www.cnet.com/rss/news/", "https://www.engadget.com/rss.xml", "http://feeds.feedburner.com/venturebeat/SZYF", "https://readwrite.com/feed/?x=1", "https://technosdata.com/feed/", "https://www.zdnet.com/news/rss.xml", "https://www.calsoftinc.com/blogs/feed", "https://trusecai.com/feed/"]
# more writing
urls1 = ["https://www.techhive.com/feed", "https://feeds.feedburner.com/RedmondPie", "https://mobilesyrup.com/feed/", "https://www.droid-life.com/feed/", "https://www.ecoustics.com/feed/", "https://feeds.feedburner.com/IeeeSpectrumFullText", "http://feeds.howtogeek.com/HowToGeek", "https://www.digitaltrends.com/feed/", "https://feeds.macrumors.com/MacRumors-All", "http://feeds.arstechnica.com/arstechnica/technology-lab", "https://feeds.feedburner.com/oreilly/radar/atom", "http://rss.slashdot.org/Slashdot/slashdotMain?format=xml", "http://www.techspot.com/backend.xml"]
# more writing
urls2 = ["http://feed.androidauthority.com/", "https://www.androidcentral.com/rss.xml", "http://www.macworld.com/index.rss", "https://fossbytes.com/feed/?x=1", "https://www.bleepingcomputer.com/feed", "https://appleinsider.com/rss/news/", "http://www.theregister.co.uk/headlines.atom", "https://hackaday.com/blog/feed/", "https://www.trustedreviews.com/feed", "https://feeds.feedburner.com/thenextweb", "https://www.technologyreview.com/topnews.rss", "https://bgr.com/tech/feed/", "https://www.slashgear.com/feed/", "https://feeds.feedburner.com/techdirt/feed", "http://www.extremetech.com/feed"]

urls3 = ["https://siliconangle.com/feed/", "https://www.geekwire.com/feed/", "https://www.ilounge.com/feed", "https://vulcanpost.com/feed/", "http://feeds.feedburner.com/Techeblog", "https://www.siliconrepublic.com/feed/", "https://techaeris.com/feed/", "https://www.afritechmedia.com/feed/", "http://www.technobuffalo.com/feed/", "https://www.techradar247.com/feed/rss", "https://irishtechnews.ie/feed/", "http://www.imore.com/feed", "https://www.techrepublic.com/rssfeeds/articles/", "https://www.webproeducation.org/feed/", "https://www.techpreview.org/feed/", "http://feeds.betanews.com/bn"]

urls4 = ["https://www.greenbot.com/feed/", "https://www.pcworld.com/index.rss", "https://feeds.feedburner.com/thenextweb", "http://feeds.arstechnica.com/arstechnica/index/", "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"]

urls5 = [""]

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


for rss_url in urls4:
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



