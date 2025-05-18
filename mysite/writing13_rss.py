import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://bankinnovation.net/feed/", "https://innotechtoday.com/feed/", "https://steveblank.com/feed/", "https://datainnovation.org/feed/", "https://www.androidheadlines.com/category/wearables/feed", "https://www.theverge.com/rss/wearables/index.xml", "https://gadgetsandwearables.com/category/wearables/feed/", "https://www.lawsitesblog.com/feed", "https://legaltechnology.com/feed/", "https://www.legalitprofessionals.com/?format=feed&type=rss", "https://cyberblogindia.in/feed/", "https://feeds.feedblitz.com/law/legal-news/", "https://abovethelaw.com/technology/feed/"]
# more writing
urls1 = ["https://kevin.lexblog.com/feed/", "https://www.artificiallawyer.com/feed/", "https://www.legaltechmonitor.com/feed/", "https://legal-planet.org/feed/", "https://www.bigforktech.com/feed/", "https://www.legaltechdaily.com/feed/", "https://www.goodmanstech.ca/blog-feed.xml", "http://feeds.feedblitz.com/futurelawyer", "https://www.tech4law.co.za/feed/", "https://www.medtechdive.com/feeds/news/", "https://www.medicaldesignandoutsourcing.com/feed/", "https://medtechintelligence.com/feed/", "https://www.med-technews.com/api/rss/content.rss"]
# more writing
urls2 = ["https://unbox.ph/feed/", "https://manilashaker.com/feed/", "https://feeds.feedburner.com/Techpinas", "https://www.gizguide.com/feeds/posts/default?alt=rss", "https://www.noypigeeks.com/feed/", "https://www.technobaboy.com/feed/", "https://www.teknogadyet.com//feeds/posts/default", "https://www.tekkiepinas.xyz/feeds/posts/default", "https://www.techlokalph.com/feeds/posts/default", "https://pinoytechsaga.blogspot.com/feeds/posts/default?alt=rss", "https://www.pinoymetrogeek.com/feeds/posts/default", "https://www.thetechnivore.com/feed/"]

urls3 = ["https://www.techpatrl.com/feed/", "https://everytechever.com/feed/", "https://balastech.com/feed/", "https://www.androidist.net/feeds/posts/default", "https://newsbytes.ph/feed/", "https://dronthego.net/feed/", "https://backendnews.net/feed/", "https://techcrunch.com/category/startups/feed/", "https://techcrunch.com/mobile/feed/", "https://techcrunch.com/category/gadgets/feed/", "https://techcrunch.com/greentech/feed/"]



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


