import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://thriftshopcommando.blogspot.com/feeds/posts/default?alt=rss", "https://www.keepingcurrentmatters.com/feed", "https://insteading.com/feed/", "https://www.thegoodtrade.com/features?format=rss", "https://bezen.eco/feed/", "https://alfordhomes.com/feed", "https://www.ecoustics.com/home-theater/feed/", "https://hometheaterhifi.com/feed/", "https://www.insideci.co.uk/our-rss-feeds/full-site.aspx"]
# more writing
urls1 = ["https://www.digitaltrends.com/home-theater/feed/", "https://www.soundandvision.com/rss.xml", "https://hometheaterreview.com/feed/", "https://www.cepro.com/category/audio-video/home-theater/feed/", "https://blog.omnioutdoorliving.com/feed/", "https://stylebyemilyhenderson.com/feed", "http://feeds.apartmenttherapy.com/apartmenttherapy/main", "https://feeds.feedburner.com/houzz"]
# more writing
urls2 = ["https://abeautifulmess.com/feed/", "http://cococozy.com/feed/", "https://www.residencestyle.com/feed/", "https://www.chrislovesjulia.com/feed/", "https://www.home-designing.com/feed", "https://www.remodelista.com/rss/", "https://thedesignfiles.net/feed/", "https://www.decoist.com/feed/", "https://onekindesign.com/feed/", "https://theinteriorsaddict.com/feed", "https://www.desiretoinspire.net/feed/"]

urls3 = ["https://www.pufikhomes.com/en/feed/", "https://www.sadecor.co.za/interior-design-blog/feed/", "http://mydesignchic.com/feed/", "https://beckiowens.com/feed/", "https://feeds.feedburner.com/a_beautiful_mess", "http://www.addicted2decorating.com/feed", "https://southernhospitalityblog.com/feed/", "https://www.manmadediy.com//feed", "https://craftgossip.com/feed/", "https://www.handymantips.org/feed/"]

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


