import requests
import time


import feedparser
from requests import get

base = ""
urls = ["http://renocontractor.ca/feed", "https://www.myhousedesignbuild.com/feed/", "https://tanglycottage.wordpress.com/feed/", "http://www.englishhomestead.com/feeds/posts/default", "https://gardenerd.com/feed", "https://www.organicgardener.com.au/rss", "https://www.espoma.com/feed/", "https://sustainablegarden.blogspot.com/feeds/posts/default", "https://gardentherapy.ca/feed/"]
# more writing
urls1 = ["http://earth911.com/feed/", "https://ecofriend.com/feed", "https://greenlivingguy.com/feed/", "https://forestnation.com/feed/", "https://www.fool.com/a/feeds/partner/googlechromefollow?apikey=5e092c1f-c5f9-4428-9219-908a47d2e2de", "https://www.automotiveworld.com/feed/", "https://paultan.org/feed/"]
# more writing
urls2 = ["https://www.insurancejournal.com/topics/homeowners-insurance/feed/", "https://www.addicted2decorating.com/feed?x=2", "https://feeds.feedburner.com/southernhospitalityblog/PQqu", "http://feeds.apartmenttherapy.com/apartmenttherapy/main", "https://stylebyemilyhenderson.com/feed", "https://www.chrislovesjulia.com/feed/", "http://feeds.feedblitz.com/drivenbydecor?x=1"]

urls3 = ["https://www.hellolovelystudio.com/feed", "https://missmustardseed.com/feed/atom/", "https://www.worthingcourtblog.com/feed", "https://startathomedecor.com/feed/", "https://thecitycottage.com/feed/", "https://growandsharegarden.wordpress.com/feed/", "https://www.latimes.com/world-nation/rss2.0.xml#nt=1col-7030col1", "https://www.latimes.com/business/rss2.0.xml"]

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


