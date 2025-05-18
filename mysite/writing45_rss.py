import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.way.com/blog/feed/", "https://www.onallcylinders.com/feed/", "https://feeds.feedburner.com/Automoblognet", "https://bangshift.com/feed", "https://autotalk.com.au/feed", "https://www.carexpert.com.au/feed", "https://2nernation.com/feed/", "https://www.francetoday.com/feed/", "https://www.myfrenchlife.org/feed/", "https://technplay.com/feed/", "https://feeds.feedblitz.com/LawlessFrench"]
# more writing
urls1 = ["https://www.frenchentree.com/feed/", "https://bonjourparis.com/feed/", "http://www.crash.fr/feed/", "https://frenchquartermag.com/index.php/feed/", "https://www.newsmax.com/rss/Newsfront/16/", "https://www.newsmax.com/rss/Politics/1/", "https://www.newsmax.com/rss/TheWire/118/", "https://www.newsmax.com/rss/Health-News/177/", "https://www.newsmax.com/rss/US/18/", "https://www.newsmax.com/rss/SciTech/20/", "https://www.newsmax.com/rss/GlobalTalk/162/"]
# more writing
urls2 = ["http://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009", "https://globalnews.ca/feed/", "https://rabble.ca/rss.xml", "https://feeds.feedburner.com/np_top_stories.rss", "https://torontosun.com/feed/", "https://feeds.feedburner.com/FP_TopStories", "https://vancouversun.com/feed/?x=1", "https://toronto.citynews.ca/feed/", "https://montrealgazette.com/feed", "https://calgaryherald.com/feed"]

urls3 = ["https://edmontonjournal.com/feed/", "https://windsorstar.com/feed", "https://theprovince.com/feed", "https://calgarysun.com/feed", "https://ottawasun.com/feed/", "https://feeds.feedblitz.com/thetyee", "https://thestarphoenix.com/feed", "https://edmontonsun.com/feed", "https://www.nationalobserver.com/front/rss", "https://www.biv.com/rss", "https://leaderpost.com/feed/", "https://www.owensoundsuntimes.com/category/news/local-news/feed"]

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


