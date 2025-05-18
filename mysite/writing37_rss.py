import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://thewillnigeria.com/news/feed/", "https://www.nigerianeye.com/feeds/posts/default", "https://www.africanexaminer.com/feed/", "https://naijnaira.com/feed/", "https://thenews-chronicle.com/feed/", "https://www.informationng.com/feed", "https://pointblanknews.com/pbn/feed/", "https://www.herald.ng/feed/", "https://hallmarknews.com/feed/", "https://www.theinfostride.com/feed/", "https://businessday.ng/feed/"]
# more writing
urls1 = ["https://tndonlinenews.com.ng/feed/", "https://newsblenda.com/feed/", "https://www.nonprofitpro.com/feed/", "https://donorbox.org/nonprofit-blog/feed", "https://ssir.org/site/rss_2.0", "https://charityvillage.com/feed/", "https://nonprofitquarterly.org/feed/", "http://clairification.com/feed/", "https://thenonprofittimes.com/feed/", "https://timesofindia.indiatimes.com/rssfeeds/1221656.cms"]
# more writing
urls2 = ["http://feeds.feedburner.com/NDTV-LatestNews", "https://www.indiatoday.in/rss/1206578", "https://indianexpress.com/feed/", "https://www.thehindu.com/news/national/?service=rss", "http://www.news18.com/rss/india.xml", "https://www.business-standard.com/rss/latest.rss", "https://www.dnaindia.com/feeds/india.xml", "https://www.deccanchronicle.com/rss_feed"]

urls3 = ["https://www.storifynews.com/feed/", "https://hubnetwork.in/feed/", "https://kashmirnews.in/feed/", "https://vindhyafirst.com/feed/", "https://www.sangritoday.com/rss/latest-posts", "https://biovoicenews.com/feed/", "https://theprobe.in/feed/", "https://www.telanganatribune.com/feed/"]

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


