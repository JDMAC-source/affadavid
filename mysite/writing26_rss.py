import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://economictimes.indiatimes.com/markets/expert-view/rssfeeds/50649960.cms", "https://economictimes.indiatimes.com/markets/commodities/rssfeeds/1808152121.cms", "https://economictimes.indiatimes.com/markets/forex/rssfeeds/1150221130.cms", "https://economictimes.indiatimes.com/markets/bonds/rssfeeds/2146846.cms", "https://economictimes.indiatimes.com/news/india/rssfeeds/81582957.cms", "https://economictimes.indiatimes.com/markets/web-stories/rssfeeds/92205028.cms", "https://economictimes.indiatimes.com/news/web-stories/rssfeeds/84644705.cms", "https://economictimes.indiatimes.com/news/newsblogs/rssfeeds/65098458.cms"]
# more writing
urls1 = ["https://economictimes.indiatimes.com/news/economy/rssfeeds/1373380680.cms", "https://economictimes.indiatimes.com/news/company/rssfeeds/2143429.cms", "https://economictimes.indiatimes.com/news/defence/rssfeeds/46687796.cms", "https://economictimes.indiatimes.com/news/international/rssfeeds/858478126.cms", "https://economictimes.indiatimes.com/news/elections/rssfeeds/65869819.cms", "https://economictimes.indiatimes.com/news/sports/rssfeeds/26407562.cms", "https://economictimes.indiatimes.com/news/science/rssfeeds/39872847.cms", "https://economictimes.indiatimes.com/news/et-tv/rssfeedsvideo/48897386.cms"]
# more writing
urls2 = ["https://economictimes.indiatimes.com/news/latest-news/rssfeeds/20989204.cms", "https://economictimes.indiatimes.com/industry/auto/rssfeeds/13359412.cms", "https://economictimes.indiatimes.com/rssfeeds/13358259.cms", "https://economictimes.indiatimes.com/industry/cons-products/rssfeeds/13358759.cms", "https://economictimes.indiatimes.com/industry/energy/rssfeeds/13358350.cms", "https://www.siliconvalley.com/feed/", "https://www.metrosiliconvalley.com/feed/", "https://appinventiv.com/feed/", "https://digiconasia.net/feed", "https://prosglobalinc.com/feed/", "http://www.autoblog.com/rss.xml"]

urls3 = ["http://feeds.feedburner.com/Speedhunters", "https://www.carexpert.com.au/feed", "https://www.caranddriver.com/rss/all.xml/", "https://www.autodailydiary.com/feeds/posts/default", "https://www.motor1.com/rss/news/all/", "https://www.pistonheads.com/xml/news091.asp", "https://www.hemmings.com/stories/feed", "https://ihsmarkit.com/BlogFeed.ashx?i=Automotive", "https://www.autocar.co.uk/rss", "https://blog.dupontregistry.com/feed/", "https://feeds.highgearmedia.com/?sites=TheCarConnection&type=all", "https://feeds.feedburner.com/BmwBlog"]

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


