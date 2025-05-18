import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.redlegnation.com/feed/", "https://www.brewcrewball.com/rss/current.xml", "https://www.federalbaseball.com/rss/index.xml", "https://www.purplerow.com/rss/current.xml", "https://dodgersdigest.com/feed/", "https://bluejaysnation.com/feed", "https://steelcitypirates.com/feed/", "https://theprospecttimes.com/feed/", "http://drmiraculous.blogspot.com/feeds/posts/default?alt=rss", "https://www.insiderbaseball.com/blog/index.xml", "https://sullybaseball.wordpress.com/feed/", "https://www.dodgersnation.com/feed"]
# more writing
urls1 = ["https://towardsdatascience.com/feed", "https://www.kdnuggets.com/feed", "https://aws.amazon.com/blogs/machine-learning/feed/", "https://medium.com/feed/topic/machine-learning", "https://blog.google/technology/ai/rss/", "https://blogs.cisco.com/tag/machine-learning/feed", "https://nanonets.com/blog/rss/", "https://www.marktechpost.com/category/technology/artificial-intelligence/feed/", "https://towardsai.net/ai/artificial-intelligence/feed", "http://9gagrss.com/feed/", "https://feeds.feedburner.com/CrackedRSS"]
# more writing
urls2 = ["https://thechive.com/feed/", "https://www.normanandozi.com/feed/", "https://icanhas.cheezburger.com/rss", "https://reductress.com/rss", "https://miscellanynews.org/category/humor/feed/", "https://lamebook.com/feed/", "https://humoroutcasts.com/feed/", "https://pleated-jeans.com/feed/", "https://www.elisbergindustries.com/blog/feed", "https://www.politicalirony.com/feed/", "http://www.newsbiscuit.com/feed/", "https://clickhole.com/feeds/rss", "https://www.youtube.com/feeds/videos.xml?channel_id=UCpsSadsgX_Qk9i6i_bJoUwQ&x=1"]


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