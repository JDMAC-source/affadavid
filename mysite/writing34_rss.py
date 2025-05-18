import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.statnews.com/category/biotech/feed/", "https://www.biocentury.com/rss/BioCentury.xml", "https://biotechstrategyblog.com/feed/", "https://libraries.mit.edu/news/feed/", "https://librarytechnology.org/rss/", "https://www.cnet.com/rss/deals/", "https://www.cnet.com/rss/how-to/", "https://dutchreview.com/feed/", "https://www.culy.nl/feed/", "https://www.francescakookt.nl/feed/", "https://radicalfire.com/feed/"]
# more writing
urls1 = ["https://www.manify.nl/feed/", "https://www.31mag.nl/feed/", "https://www.expatrepublic.com/feed/", "https://www.amsterdamfoodie.nl/blog/feed/", "https://www.verhuisbedrijfdirect.nl/feed/", "https://simplifaster.com/feed/", "https://athletechnews.com/category/tech/feed/", "https://www.sportsvideotech.com/feed/", "https://engineering.salesforce.com/feed/", "https://blogs.cisco.com/tag/engineering/feed", "https://steveblank.com/feed/", "https://thestartupmag.com/feed/", "https://www.eu-startups.com/feed/", "https://startupnation.com/feed/"]
# more writing
urls2 = ["https://www.startupdaily.net/feed/", "https://medium.com/feed/swlh", "https://yourstory.com/feed/", "https://blog.ourcrowd.com/feed/", "https://www.alleywatch.com/category/startups/feed/", "https://www.techpluto.com/feed", "https://alltopstartups.com/feed/", "https://siliconcanals.com/news/startups/feed/", "https://gritdaily.com/feed/", "https://startups.co.uk/feed/", "https://feeds.feedburner.com/siliconflorist", "https://futurestartup.com/feed/", "https://www.startupcan.ca/feed/", "https://startuptipsdaily.com/feed/"]

urls3 = ["https://www.automotiveworld.com/feed/", "https://paultan.org/feed/", "https://ihsmarkit.com/BlogFeed.ashx?i=Automotive"]

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


