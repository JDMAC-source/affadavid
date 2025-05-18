import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.makeuseof.com/feed/", "https://www.iphoneincanada.ca/feed/", "https://techcouver.com/feed/", "https://itnerd.blog/feed/", "https://betakit.com/feed/", "https://www.youtube.com/feeds/videos.xml?channel_id=UCsTcErHg8oDvUnTzoqsYeNw&x=1", "https://techrseries.com/feed/", "https://hrtechfeed.com/feed/"]
# more writing

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




