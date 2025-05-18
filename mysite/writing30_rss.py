import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://blogs.perficient.com/category/industries/healthcare/feed/", "https://www.netflixjunkie.com/feed/", "https://www.techradar.com/feeds/tag/netflix", "https://blog.apilayer.com/feed/", "http://www.gsmarena.com/rss-news-reviews.php3", "https://www.androidauthority.com/feed", "http://www.androidcentral.com/feed", "https://www.gizchina.com/feed/", "https://www.gizmochina.com/category/news/feed/", "https://mobilityarena.com/feed/"]
# more writing
urls1 = ["https://phandroid.com/feed/", "https://www.nextpit.com/feed/main.xml", "https://in.pcmag.com/mobile-phones.xml", "https://www.techadvisor.com/latest/mobile-phone/rss", "https://www.galaxyclub.nl/feed/", "https://histalk2.com/feed/", "https://www.digitalhealth.net/feed/", "https://www.healthcareittoday.com/feed/", "https://medinform.jmir.org/feed/atom", "https://medicalxpress.com/rss-feed/health-informatics-news/"]
# more writing
urls2 = ["https://blogs.perficient.com/category/industries/healthcare/feed/", "https://hitconsultant.net/feed/", "https://www.eonline.com/syndication/feeds/rssfeeds/topstories.xml", "http://www.tmz.com/rss", "https://feeds.distribution.dotdashmeredith.com/v3/rss/4780ef1e-1952-43da-abd9-3b7c690f1f72", "https://hollywoodlife.com/feed/", "https://theshaderoom.com/feed/", "http://www.filmfare.com/feeds/feeds.xml", "https://yogossip.com/rss.xml"]

urls3 = ["https://allcelebrities.us/feed/", "https://www.pinkvilla.com/rss.xml", "https://socialitelife.com/feed/", "https://www.closerweekly.com/feed/", "https://allaboutthetea.com/feed/", "https://celebmix.com/feed/", "https://www.entertainmentdaily.co.uk/feed/", "https://www.soapoperadigest.com/feed/?q=rss", "https://vipmagazine.ie/feed/", "https://www.buzzfeed.com/celebrity.xml", "https://www.usmagazine.com/feed/"]

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


