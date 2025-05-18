import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://mettisglobal.news/feed/", "https://www.globalsmallbusinessblog.com/feeds/posts/default", "https://www.mcdaccginc.com/blog-feed.xml", "http://www.dynamicbusiness.com.au/feed", "https://afleo.com/feed/", "https://feeds.businessinsider.com/custom/all", "https://www.theguardian.com/business/series/guardian-business-live/rss", "https://www.cloudcomputing-news.net/feed/", "https://feeds.feedburner.com/cioreview/fvHK", "https://www.techrepublic.com/rssfeeds/topic/cloud/"]
# more writing
urls1 = ["https://cloudtweaks.com/feed/", "https://www.snowflake.com/feed/", "https://www.cloudwards.net/articles/feed/", "https://cloudsecurityalliance.org/blog/feed/", "http://feeds.feedburner.com/ClPlBl", "https://blogs.cisco.com/tag/cloud-computing/feed", "https://www.hospitalitymagazine.com.au/feed/", "https://hoteliermaldives.com/feed/", "https://www.hospitalitybusiness.co.nz/feed/", "http://www.hotelowner.co.uk/feed/", "http://feeds.feedburner.com/bighospitality/news"]
# more writing
urls2 = ["https://www.asianhospitality.com/feed/", "https://www.hospitality.today/feed.rss", "https://hotelsmag.com/news-categories/hospitality/feed/", "https://africahotelreport.com/feed/", "https://www.hospitalitynet.org/news/global.xml", "https://insights.ehotelier.com/category/global-news/feed/", "https://revenue-hub.com/feed/", "https://www.hotelbusiness.com/feed/", "https://currentaffairs.adda247.com/feed/", "https://www.legacyias.com/index.php/feed/"]

urls3 = ["https://www.roadtovr.com/feed/", "https://www.uploadvr.com/feed/", "https://www.xrom.in/xrnews/blog-feed.xml", "https://economictimes.indiatimes.com/rssfeedsdefault.cms", "https://economictimes.indiatimes.com/prime/money-and-markets/rssfeeds/62511286.cms", "https://economictimes.indiatimes.com/news/politics-and-nation/rssfeeds/1052732854.cms", "https://economictimes.indiatimes.com/industry/rssfeeds/13352306.cms", "https://economictimes.indiatimes.com/tech/rssfeeds/13357270.cms"]

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


