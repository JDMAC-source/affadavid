import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://creebhills.com/feed", "https://mcebiscoo.com/feed/", "https://amebo9ja.com/feed/", "https://www.akelicious.net/feed/", "https://beeniewords.com/feed/", "https://premium9ja.com/feed/", "https://www.expressiveinfo.com/feed/", "https://www.glamcityz.com/feed/", "https://contents101.com/feed/"]
# more writing
urls1 = ["https://starofmysore.com/feed/", "https://www.india.com/feed/", "https://www.oneindia.com/rss/news-india-fb.xml", "https://news.abplive.com/home/feed", "https://www.amarujala.com/rss/breaking-news.xml", "https://www.indiatvnews.com/rssnews/topstory.xml", "https://www.opindia.com/feed/", "https://www.thehindubusinessline.com/?service=rss", "https://prod-qt-images.s3.amazonaws.com/production/freepressjournal/feed.xml", "https://www.siasat.com/feed/", "http://feeds.feedburner.com/ScrollinArticles.rss", "https://telanganatoday.com/feed", "https://www.informalnewz.com/feed/", "https://www.sentinelassam.com/feed"]
# more writing
urls2 = ["https://thebetterindia.com/feed/", "http://feeds.feedburner.com/SocialSamosa", "https://www.sinceindependence.com/feed/", "https://assamtribune.com/feed", "https://www.orissapost.com/feed/", "https://chandigarhmetro.com/feed/", "https://tfipost.com/feed/", "https://prod-qt-images.s3.amazonaws.com/production/nationalherald/feed.xml", "https://pragativadi.com/feed/", "https://www.yovizag.com/feed/", "https://bhaskarlive.in/feed/", "https://apnlive.com/feed/", "https://theshillongtimes.com/feed/", "https://kashmirobserver.net/feed/", "https://www.easternherald.com/feed", "https://knnindia.co.in/newsfeed/feedbycategory"]

urls3 = ["https://organiser.org/feed/", "https://feeds.feedburner.com/kashmir-reader", "https://web.statetimes.in/feed/", "https://www.thetimesofbengal.com/feed/", "https://www.sikkimexpress.com/Feed/rss_feed/latest-news", "https://newstodaynet.com/index.php/feed/", "https://thenewsglory.com/feed/", "https://newstodaynet.com/feed/", "https://www.anytvnews.com//feed/", "https://thenorthlines.com/feed/"]

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


