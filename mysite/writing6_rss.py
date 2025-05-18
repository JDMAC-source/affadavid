import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://languagelog.ldc.upenn.edu/nll/?feed=rss2", "https://languagehat.com/feed/", "https://www.echojs.com/rss", "https://www.youtube.com/feeds/videos.xml?channel_id=UCCODtTcd5M1JavPCOr_Uydg&x=1", "https://www.tipsclear.com/feed/", "https://www.filmfare.com/feeds/feeds.xml", "https://uploadarticle.com/feed/", "https://thelifestylejournalist.com/feed/", "https://www.flypped.com/feed/", "https://www.atlantamagazine.com/feed/"]
# more writing
urls1 = ["https://www.thefalcoholic.com/rss", "https://www.artsatl.org/feed/", "https://atlanta.eater.com/rss/index.xml", "https://365atlantatraveler.com/feed/", "http://feeds.feedblitz.com/atlonthecheap", "https://www.fanbolt.com/feed/", "http://www.ventureatlanta.org/feed/", "https://www.tonetoatl.com/feeds/posts/default", "https://www.atlantarealestateforum.com/feed/", "https://www.peachtreehoops.com/rss/index.xml", "https://www.finegardening.com/feed"]
# more writing
urls2 = ["http://feeds.feedburner.com/GardenTherapy", "https://www.epicgardening.com/blog/feed", "https://gardenerspath.com/feed/", "https://www.gardenista.com/rss/", "https://growagoodlife.com/feed/", "https://gardenrant.com/feed/atom", "https://lisasgardenadventureinoregon.blogspot.com/feeds/posts/default?alt=rss", "https://feeds.feedburner.com/Activehistoryca", "https://clarkesworldmagazine.com/?feed=rss2", "https://file770.com/feed/"]


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