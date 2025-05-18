import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://futurism.com/feed", "https://www.futurity.org/feed/", "https://singularityhub.com/feed/", "https://www.nextbigfuture.com/feed", "https://www.inverse.com/rss", "https://www.trendhunter.com/rss", "http://singularityscience.com/blog/category/futurism/feed", "https://www.deutschland.de/en/feed-news/rss.xml", "http://newsfeed.zeit.de/index", "https://www.thelocal.de/feeds/rss.php", "https://www.kn-online.de/arc/outboundfeeds/rss/", "https://jungefreiheit.de/feed/", "https://taz.de/!p4608;rss/", "https://www.abendzeitung-muenchen.de/storage/rss/rss/alle-artikel-abendzeitung.xml", "https://rss.focus.de/"]
# more writing
urls1 = ["https://www.ln-online.de/arc/outboundfeeds/rss/", "https://www.ostsee-zeitung.de/arc/outboundfeeds/rss/", "https://www.handelsblatt.com/contentexport/feed/top-themen", "https://www.op-marburg.de/arc/outboundfeeds/rss/", "https://rss.sueddeutsche.de/rss/Topthemen", "https://feed.ksta.de/feed/rss/index.rss", "https://www.nd-aktuell.de/rss/aktuell.php", "https://stuttgart-journal.de/tp3/feed/", "https://www.ruhrnachrichten.de/feed/", "https://www.stern.de/feed/standard/alle-nachrichten/", "https://www.freiepresse.de/rss/rss_chemnitz.php", "https://www.muensterschezeitung.de/rss/feed/mz_lokales", "https://www.aachener-zeitung.de/feed.rss"]
# more writing
urls2 = ["https://ga.de/feed.rss", "https://www.tagesschau.de/xml/rss2/", "https://www.mopo.de/feed/", "https://www.jungewelt.de/feeds/newsticker.rss", "https://www.mainpost.de/storage/rss/rss/topnews.xml", "https://rp-online.de/feed.rss", "https://www.faz.net/rss/aktuell/", "https://www.haz.de/arc/outboundfeeds/rss/", "https://www.lvz.de/arc/outboundfeeds/rss/", "https://semiengineering.com/feed/", "https://www.semiconductor-today.com/rss/news.xml", "https://semiwiki.com/feed/", "https://techxplore.com/rss-feed/semiconductors-news/", "https://www.eejournal.com/category/semiconductor/feed/", "https://anysilicon.com/feed/"]

urls3 = ["https://www.digitimes.com/rss/daily.xml", "https://www.esecurityplanet.com/cloud/feed/", "https://insidebitcoins.com/feed", "https://blockchainwire.io/feed-rss.xml", "https://www.thecryptoupdates.com/feed/", "https://blockchain.news/rss", "https://blog.coinfund.io/feed", "https://coinweez.com/feed/", "https://www.blockchainnewssite.com/feed/", "https://www.engadget.com/tag/logitech/rss.xml", "https://hitconsultant.net/category/digital-health-2/feed/"]

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


