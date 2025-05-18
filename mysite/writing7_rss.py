import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://scifibloggers.com/feed/", "https://reactormag.com/feed/", "https://locusmag.com/feed/", "https://fanfiaddict.com/feed/", "https://www.scifipulse.net/feed/", "https://www.trekcore.com/feed.xml", "https://sf-encyclopedia.com/rss.php", "http://fantasyhotlist.blogspot.com/feeds/posts/default", "http://approachingpavonis.blogspot.com/feeds/posts/default", "https://www.scifinow.co.uk/feed/", "https://trekmovie.com/feed/", "https://www.queerscifi.com/feed/", "https://sffbookreview.wordpress.com/feed/", "https://www.goodreturns.in/rss/goodreturns-fb.xml"]
# more writing
urls1 = ["https://taxguru.in/feed/", "https://freefincal.com/feed/", "https://www.goodmoneying.com/feed/", "https://www.investmentpedia.org/feed/", "https://www.fintoo.in/blog/feed/", "https://www.westernjournal.com/feed/", "http://feeds.feedburner.com/NiemanJournalismLab", "https://www.youthkiawaaz.com/feed/", "https://www.mediaite.com/feed/", "https://journalism.nyu.edu/about-us/news/feed/", "https://pressgazette.co.uk/feed/", "https://www.poynter.org/feed/", "https://authenticstorytelling.net/feed/", "https://www.freepressfail.com/feed/"]
# more writing
urls2 = ["https://onemanandhisblog.com/rss/", "https://dankennedy.net/feed/", "https://irjci.blogspot.com/feeds/posts/default", "https://www.mindbodygreen.com/rss/feed.xml", "https://www.wellandgood.com/feed/", "https://fitfoodiefinds.com/feed/", "https://www.natalieshealth.com/feed/", "https://wellbeingmagazine.com/feed/", "https://www.alive.com/feed/", "https://appadvice.com/feed", "https://android-developers.googleblog.com/feeds/posts/default?alt=rss", "https://www.phonearena.com/feed/apps", "https://feeds.feedburner.com/theiphoneblog"]
urls3 = ["http://scripting.com/rss.xml"]

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
        print(item.summary)
        
        r = requests.post('https://www.predictionary.us/B/posts/',data={'title':"Scripting News - "+item.published, "body":item.summary, "url2": item.link})
        
        print(r.status_code)
        print(r.text)