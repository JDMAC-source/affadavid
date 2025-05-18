import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://wecanmag.com/feed/", "https://startupreporter.in/feed/", "https://startupsac.com/feed/", "http://redrocketvc.blogspot.com/feeds/posts/default?alt=rss", "https://e27.co/index_wp.php/feed/", "http://www.kdnuggets.com/feed", "https://www.analyticsvidhya.com/feed/", "https://www.offshorewind.biz/feed/", "https://nawindpower.com/feed", "https://w3.windfair.net/wind-energy/news.rss", "https://cleantechnica.com/category/clean-power/wind-energy/feed/", "https://www.evwind.es/feed", "https://windinsider.com/category/news/feed/"]
# more writing
urls1 = ["https://windpowernl.com/feed/", "https://www.theguardian.com/environment/windpower/rss", "https://blog.google/rss/", "https://cloudblog.withgoogle.com/rss/", "https://android-developers.googleblog.com/feeds/posts/default?alt=rss", "https://feeds.feedburner.com/google/think", "https://www.zdnet.com/topic/google/rss.xml", "https://www.theverge.com/rss/google/index.xml", "https://feeds.feedburner.com/GoogleAppsUpdates", "https://feeds.feedburner.com/GoogleMapsMania", "https://www.apple.com/newsroom/rss-feed.rss"]
# more writing
urls2 = ["https://news.samsung.com/global/feed", "https://blog.dell.com/en-us/feed/", "https://blogs.oracle.com/rss", "https://about.fb.com/feed/", "https://www.breakfastleadership.com/blog?format=rss", "https://thefintechtimes.com/feed/", "https://www.finextra.com/rss/blogs.aspx/?x=1", "https://www.financemagnates.com/fintech/feed/", "https://www.fintechfutures.com/feed/", "https://www.fintechweekly.com/fintech-news.rss", "https://fintechnews.sg/feed/", "https://australianfintech.com.au/blog/feed/", "https://fintechreview.net/feed/"]

urls3 = ["https://www.etoro.com/news-and-analysis/feed/", "https://techbullion.com/feed/", "https://www.bobsguide.com/category/bankingtech/fintech/feed/", "https://finovate.com/feed/", "https://fintechnews.ch/feed/", "https://www.atmmarketplace.com/rss/", "https://ncfacanada.org/feed/", "https://fintecbuzz.com/feed/", "https://www.regtechtimes.com/feed/", "https://www.fintechinshorts.com/feed/", "https://fintechnews.hk/feed/", "https://blog.imarticus.org/feed/", "http://bankautomationnews.com/feed/", "https://www.intelalley.com/feed/"]

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


