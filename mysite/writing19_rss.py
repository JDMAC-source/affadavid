import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://underkg.co.kr/news/rss", "https://www.koreaittimes.com/rss/S1N1.xml", "https://www.handelsblatt.com/contentexport/feed/top-themen", "https://www.basicthinking.de/blog/category/technologie/feed/", "https://www.mactechnews.de/Rss/News.x", "https://www.toptechnews.de/feed/", "https://tech-blogs.de/feed/", "https://cleantechnica.com/feed/", "https://envirotecmagazine.com/feed/", "https://www.womenincleantechsustainability.org/feed/", "http://cleantechies.com/feed/", "https://techxplore.com/rss-feed/energy-green-tech-news/"]
# more writing
urls1 = ["https://techcrunch.com/category/climate/feed/", "https://energycentral.com/topics/greentech/rss.xml", "https://rss.itmedia.co.jp/rss/2.0/topstory.xml", "https://www.watch.impress.co.jp/data/rss/1.0/ipw/feed.rdf", "https://ascii.jp/rss.xml", "https://feeds.feedburner.com/SdJapan", "https://www.gizmodo.jp/index.xml", "https://www.appbank.net/feed", "https://japantoday.com/category/tech/feed", "https://www.muypymes.com/feed", "http://feeds.feedburner.com/WwwhatsNew", "https://www.elespanol.com/rss/elandroidelibre/"]
# more writing
urls2 = ["https://planetpython.org/rss20.xml", "https://realpython.com/atom.xml?format=xml", "https://www.howtogeek.com/feed/", "https://boingboing.net/feed", "https://www.denofgeek.com/uk/feeds/tv", "https://www.majorgeeks.com/files/rss", "https://www.geeky-gadgets.com/feed/", "https://geekmamas.com/feed/", "https://www.geekextreme.com/feed/", "https://thenerdstash.com/feed/", "https://granitegeek.concordmonitor.com/feed/", "https://geekdad.com/feed/", "https://www.geekgirlauthority.com/feed/rss/", "https://allagesofgeek.com/feed/", "https://www.geekfeed.com/feed/", "https://thegeek.games/feed/"]

urls3 = ["https://feeds.feedburner.com/APiusManAHolyThriller", "https://seogeek.io/feed/", "https://musictech.com/feed/", "https://www.soundonsound.com/latest_news.xml", "https://www.mixonline.com/feed", "https://www.kvraudio.com/rss/kvr_news_top.rss", "https://www.synthanatomy.com/feed", "https://blog.native-instruments.com/feed/", "https://www.synthtopia.com/feed/", "https://cdm.link/feed/", "https://24gadget.ru/rss.xml", "https://hi-news.ru/feed", "https://rb.ru/feeds/all/", "https://runet.news/feed.rss", "https://www.computerra.ru/feed/", "https://habr.com/en/rss/all/all/?fl=en"]

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


