import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://bankloch.blogspot.com/feeds/posts/default", "https://www.pymnts.com/feed/", "https://www.thespuzz.com/feed/", "http://www.macrumors.com/macrumors.xml", "https://9to5mac.com/feed/", "http://www.macworld.com/index.rss", "http://daringfireball.net/feeds/main", "https://www.apple.com/newsroom/rss-feed.rss", "http://www.imore.com/feed", "https://www.cultofmac.com/feed/", "https://www.macobserver.com/feed/", "https://www.mactrast.com/feed"]
# more writing
urls1 = ["http://feeds.feedburner.com/idropnews/feed", "http://www.nytimes.com/topic/company/apple-incorporated/rss.xml", "https://apple.stackexchange.com/feeds/week", "https://www.makeuseof.com/service/ios/feed/", "https://www.theverge.com/apple/rss/index.xml", "https://www.engadget.com/topics/apple/rss.xml", "http://feeds.arstechnica.com/arstechnica/apple/", "https://www.idownloadblog.com/feed/", "https://mashable.com/category/apple/feed/"]
# more writing
urls2 = ["https://www.redmondpie.com/category/apple/feed/", "https://www.ilounge.com/feed", "https://macsecurity.net/feed", "https://feeds.feedburner.com/iphoneincanada", "https://ioshacker.com/feed", "https://feedpress.me/sixcolors", "https://mjtsai.com/blog/feed/", "https://www.theapplepost.com/feed/", "https://www.aboveavalon.com/notes?format=RSS", "https://tidbits.com/feed/", "http://appadvice.com/appnn/feed/rss", "https://www.iphonelife.com/blog/all/all/feed"]

urls3 = ["https://osxdaily.com/feed/", "https://macdailynews.com/feed/", "https://www.iclarified.com/rss/rss.xml", "https://appleosophy.com/feed/", "https://www.theguardian.com/technology/apple/rss", "https://www.youtube.com/feeds/videos.xml?channel_id=UCE_M8A5yxnLfW0KghEeajjw&x=1", "https://pcper.com/feed/", "https://www.tomshardware.com/feeds/rss2/all.xml", "https://www.wepc.com/feed/", "https://en.overclocking.com/feed/", "https://www.pcguide.com/feed/"]

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


