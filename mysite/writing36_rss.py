import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.news18.com/rss/latest.xml", "https://www.news18.com/rss/movies.xml", "https://www.news18.com/rss/world.xml", "https://www.news18.com/rss/india.xml", "https://www.9jadailyfeeds.com.ng/feed/", "https://creebhills.com/feed", "https://mcebiscoo.com/feed/", "https://amebo9ja.com/feed/", "https://www.akelicious.net/feed/", "https://beeniewords.com/feed/", "https://premium9ja.com/feed/", "https://www.expressiveinfo.com/feed/", "https://www.glamcityz.com/feed/", "https://contents101.com/feed/"]
# more writing
urls1 = ["https://chinadigitaltimes.net/feed/", "https://thediplomat.com/category/china-power/feed/", "https://china-environment-news.net/feed/", "http://www.nytimes.com/topic/destination/china/rss.xml", "http://feeds.beijingbulletin.com/rss/55582c89cb296d4c", "https://www.chinaentertainmentnews.com/feeds/posts/default", "https://news.microsoft.com/feed/", "http://feeds.windowscentral.com/wmexperts", "https://blogs.windows.com/feed/", "https://mspoweruser.com/feed/" ,"https://www.zdnet.com/blog/microsoft/rss.xml", "https://msftnewsnow.com/feed/", "https://techcommunity.microsoft.com/plugins/custom/microsoft/o365/custom-blog-rss?tid=-3510255867542948717&size=25"]
# more writing
urls2 = ["https://globalinfo247.com/feed/", "https://dailyreport.ng/feed/", "https://www.insidenaija.com.ng/feed/", "https://newsblenda.com/feed/", "https://emeraldloaded.net/feed/", "https://www.nigeriafilms.com/feed/", "https://www.naijanowell.com/feed/", "https://nigeriamag.com/feed/", "https://www.rideedy.com/feeds/posts/default?alt=rss", "https://www.naijabroadcast.com.ng/feeds/posts/default", "https://mathewtegha.com/feed/", "http://feeds.dzone.com/home", "https://sdtimes.com/feed/", "https://www.yesitlabs.com/feed/", "https://binmile.com/feed/", "https://webkul.com/blog/feed/", "https://www.developer-tech.com/feed/"]

urls3 = ["https://dev.to/feed", "https://vivaldi.com/feed/", "https://star-knowledge.com/feed/", "https://www.madetech.com/feed/", "https://www.sigmasolve.com/feed/", "https://guardian.ng/feed/", "https://www.premiumtimesng.com/feed", "https://punchng.com/feed/", "https://pmnewsnigeria.com/feed/", "https://dailypost.ng/feed/", "https://www.channelstv.com/feed/", "https://converseer.com/feed/", "https://thebureau.com.ng/feed/", "https://independent.ng/feed/", "https://www.tori.ng/feed/rss.xml", "https://leadership.ng/feed/", "https://tribuneonlineng.com/feed/", "https://www.ripplesnigeria.com/feed/", "https://dailynigerian.com/feed/"]

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


