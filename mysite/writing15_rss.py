import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.italiamac.it/feed/", "https://www.gadgets360.com/rss/feeds", "http://www.techradar.com/rss", "https://www.digit.in/feed", "https://www.techinasia.com/feed", "https://feeds.feedblitz.com/newatlas", "https://www.ghacks.net/feed/", "https://www.techpout.com/feed/", "https://www.androidheadlines.com/feed", "https://www.iphoneitalia.com/feed", "https://www.smartphonology.it/feed/", "https://www.ispazio.net/feed", "https://defence-blog.com/feed/", "https://www.army-technology.com/feed/", "https://www.airforce-technology.com/feed/"]
# more writing
urls1 = ["https://www.melablog.it/feed/", "http://feeds.feedburner.com/ubergizmo", "https://www.eweek.com/feed/", "https://www.itnews.com.au/rss/rss.ashx", "https://www.techjuice.pk/feed/", "https://researchsnipers.com/feed/", "https://www.nextgov.com/rss/all/", "https://www.naval-technology.com/feed/", "https://www.developer-tech.com/feed", "https://techplugged.com/feed/", "https://futurefive.co.nz/feed", "https://www.gadgetsinnepal.com.np/feed/", "https://ohsem.me/feed/", "https://www.cio.com/index.rss", "https://technode.com/feed/", "https://insiderpaper.com/feed/", "http://www.techcentral.ie/feed/"]
# more writing
urls2 = ["https://www.naval-technology.com/news/feed/", "https://militaryleak.com/feed/", "https://www.defenseone.com/rss/technology/", "https://defense-update.com/feed", "https://breakingdefense.com/full-rss-feed/?v=2", "https://www.paymentsjournal.com/feed/", "https://paymentsnext.com/feed/", "https://www.paymentsdive.com/feeds/news/", "https://www.finextra.com/rss/channel.aspx?channel=payments", "https://www.pymnts.com/feed/", "https://paymentsafrika.com/feed/", "https://ffnews.com/category/newsarticle/paytech/feed/", "https://www.paymentscardsandmobile.com/feed/", "https://www.nfcw.com/feed/"]

urls3 = ["https://bankautomationnews.com/category/allposts/payments/feed/", "https://siliconcanals.com/feed/", "https://skift.com/travel-technology/feed/", "https://www.travelandtourworld.com/news/article/category/travel-technology-news/feed/", "https://www.webintravel.com/feed/", "https://ciente.io/feed/", "https://www.mercurynews.com/business/technology/feed/", "https://rss.slashdot.org/Slashdot/slashdotMain", "https://www.androidheadlines.com/feed", "https://www.techeblog.com/feed/", "https://siliconangle.com/feed/", "https://www.pharmtech.com/rss"]



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


