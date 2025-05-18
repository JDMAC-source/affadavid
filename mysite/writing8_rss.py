import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://devtechnosys.com/insights/feed/", "https://www.universalstreamsolution.com/feed/", "https://ideausher.com/feed/", "https://www.mobulous.com/blog/feed/", "https://appdevelopermagazine.com/RSS/", "https://appsgeyser.com/blog/feed", "https://www.marieclaire.co.uk/feed", "https://order-order.com/feed", "http://www.rocknrollbride.com/feed/", "https://englandnaturally.com/feed/", "https://5thingstodotoday.com/feed/"]
# more writing
urls1 = ["https://www.russh.com/feed/", "https://thedesignfiles.net/feed/", "http://www.tvtonight.com.au/feed", "https://feeds.feedburner.com/NotQuiteNigella", "https://tvblackbox.com.au/feed/", "https://ozzienews.com/feed", "https://www.greenpeace.org.au/feed/", "https://feeds.feedburner.com/mmorpg/news", "https://feeds.feedburner.com/mmobomb", "https://massivelyop.com/feed/", "https://mmos.com/feed"]
# more writing
urls2 = ["https://ragezone.com/feed/", "https://tagn.wordpress.com/feed/", "https://mmofallout.com/feed/atom/", "http://sandboxer.org/feed/", "http://feeds.feedburner.com/ToboldsBlog", "https://aggronaut.com/feed/", "https://bhagpuss.blogspot.com/feeds/posts/default?alt=rss", "https://www.rogerebert.com/feed", "https://lwlies.com/feed/", "https://www.cinemablend.com/rss/topic/reviews/movies"]


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