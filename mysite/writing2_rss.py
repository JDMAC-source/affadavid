import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.creativewritingnews.com/feed/", "https://www.writersdigest.com/.rss/full/", "https://killzoneblog.com/feed", "https://writingcooperative.com/feed", "https://selfpublishingadvice.org/feed/", "https://feeds.feedburner.com/WriterUnboxed", "https://writershelpingwriters.net/feed/", "https://advicetowriters.com/advice?format=RSS", "https://thewriteconversation.blogspot.com/feeds/posts/default", "https://www.selfpublishingreview.com/feed/", "https://www.writersdigest.com/.rss/full/", "https://selfpublishing.com/feed/", "https://indiereader.com/feed/", "https://eliteonlinepublishing.com/feed/"]
# more writing
urls1 = ["https://www.youtube.com/feeds/videos.xml?channel_id=UCDHQbU57NZilrhbuZNbQcRA", "https://the-art-of-autism.com/feed/", "https://autismawarenesscentre.com/feed/", "https://marybarbera.com/feed/", "http://www.autismpolicyblog.com/feeds/posts/default", "https://www.ihorror.com/feed/", "https://hellhorror.com/feed", "https://dailydead.com/feed/", "https://bloody-disgusting.com/feed/", "https://feeds.feedburner.com/HorrorNewsnet", "https://www.dreadcentral.com/feed/", "https://haddonfieldhorror.com/feed/", "https://bloghorror.com/feed", "https://www.creepypasta.com/feed", "https://www.horrorbuzz.com/feed/", "https://www.rue-morgue.com/feed/"]
# more writing
urls2 = ["https://www.scifinow.co.uk/feed/", "https://www.horrornewsnetwork.net/feed/", "https://www.screamhorrormag.com/feed/", "https://brokehorrorfan.com/rss", "https://horrorbrains.com/feed/", "https://darkhorrortales.blogspot.com/feeds/posts/default?alt=rss", "https://gruesomemagazine.com/feed/", "https://www.thisishorror.co.uk/feed/podcast/", "https://feeds.feedburner.com/horrorsociety/news", "https://horror.org/category/blog/feed/", "https://moviesandmania.com/category/horror/feed/", "https://scifitalk.com/feed/", "http://realmofhorror-blog.blogspot.com/feeds/posts/default?alt=rss", "https://5d-blog.com/feed/"]


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