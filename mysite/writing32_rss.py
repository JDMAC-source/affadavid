import requests
import time


import feedparser
from requests import get

base = ""
urls = ["http://feeds.feedburner.com/TheHackersNews", "https://www.darkreading.com/rss_simple.asp?f_auth=322", "http://feeds.feedburner.com/Securityweek", "https://www.helpnetsecurity.com/feed/", "https://hackread.com/feed/", "https://cyble.com/feed/", "https://www.itsecurityguru.org/feed/", "https://www.csoonline.com/news/index.rss"]
# more writing
urls1 = ["https://gbhackers.com/feed/", "https://www.bankinfosecurity.com/rss-feeds", "https://www.cyberdefensemagazine.com/feed/", "https://www.cybersecurity-insiders.com/feed/", "https://www.grahamcluley.com/feed/", "https://informationsecuritybuzz.com/feed/", "https://www.govinfosecurity.com/rssFeeds.php?type=main", "https://thecyberpost.com/feed/", "https://www.gsmarena.com/rss-news-reviews.php3"]
# more writing
urls2 = ["https://www.esimstudios.com/feeds/posts/default", "https://blog.scalefusion.com/feed/", "https://feed.cnet.com/feed/topics/mobile", "https://gadgets.ndtv.com/rss/mobiles/feeds", "https://www.trustedreviews.com/type/mobile-phones/feed", "https://www.gizbot.com/rss/mobile-fb.xml", "https://www.how2shout.com/feed", "https://www.knowyourmobile.com/taxonomy/term/3155/feed", "https://www.mobigyaan.com/feed"]

urls3 = ["https://feeds.feedburner.com/rcrwireless/sLmV", "http://www.techadvisor.co.uk/latest/mobile-phone/rss", "https://www.nextpit.com/feed/main.xml", "https://www.wsj.com/xml/rss/3_7031.xml"]

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


