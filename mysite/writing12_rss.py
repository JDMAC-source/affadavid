import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.techworld.com/news/rss", "https://digitaltimesng.com/feed/", "http://feeds.feedburner.com/ilounge", "https://techbullion.com/feed/", "https://www.pocket-lint.com/rss.phtml", "https://gadgetstouse.com/feed/", "https://theawesomer.com/tag/gadgets/feed/", "https://the-gadgeteer.com/feed/", "https://www.geeky-gadgets.com/category/gadgets/feed/", "https://mightygadget.com/feed/", "https://www.gadgetgram.com/feed/", "http://www.techdigest.tv/index.rdf", "https://gadgetsmagazine.com.ph/feed", "https://gadgets-review.com/feed/", "https://www.trendygadget.com/feed/"]
# more writing
urls1 = ["https://www.petagadget.com/feed/", "https://www.smarttechbuzz.net/feeds/posts/default?alt=rss", "https://ttgadget.com/feed/", "https://www.gamingaccessories.in/feed/", "https://www.fingent.com/feed/", "https://www.techrepublic.com/rssfeeds/articles/latest/?feedType=rssfeeds", "https://reciprocaltech.com/feed/", "https://www.ilearnfromcloud.com/feed/", "https://www.cbainfotech.com/feed/", "https://www.shoviv.com/blog/feed/", "https://thecustomizewindows.com/feed/", "https://www.techcracked.com/feeds/posts/default?alt=rss", "https://www.aleaitsolutions.com/feed/"]
# more writing
urls2 = ["https://codingmart.com/feed/", "https://yourstory.com/feed", "https://techpp.com/feed/", "https://itechhacks.com/feed/", "https://hasonss.com/blogs/feed/", "https://www.techrytr.in/feeds/posts/default", "https://techeela.com/feed/", "https://technews360.in/feed/", "https://technoluting.com/feed/", "https://indiatechnologynews.in/feed/", "https://www.techrounder.com/feed/", "https://techinformed.com/feed/", "https://techlomedia.in/feed/", "https://feeds.feedburner.com/Darkhackerworld", "https://www.knowledgenile.com/blogs/feed", "https://youtech.in/feed/", "https://www.ciodive.com/feeds/news"]

urls3 = ["https://www.enterpriseai.news/feed/", "https://go.forrester.com/blogs/feed/?x=1", "https://www.enterprisesecuritytech.com/blog-feed.xml", "https://feed.martech.zone/", "https://martech.org/feed/", "https://martechseries.com/feed/", "https://code.likeagirl.io/feed", "https://sportspyder.com/rss/teams/virginia-tech-hokies-football/articles", "https://virginiatech.sportswar.com/category/article/football/feed/", "https://www.cantechletter.com/feed/"]

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


