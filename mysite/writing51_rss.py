import requests
import time


import feedparser
from requests import get

base = ""
urls = ["http://gardentherapy.ca/feed", "http://feeds.feedblitz.com/thistlewoodfarm", "http://feeds.feedburner.com/dreamgreendiy/dyiE", "https://feeds.feedburner.com/busyinbrooklyn", "https://feeds.feedburner.com/petticoatjunktion/lvrn", "https://artzyfartzycreations.com/feed/", "https://blog.embracehomeloans.com/feed/", "https://www.wdrb.com/search/?f=rss&t=article&c=news&l=50&s=start_time&sd=desc"]
# more writing
urls1 = ["https://www.wtvq.com/feed/", "https://www.wnky.com/feed/", "https://www.wlky.com/topstories-rss", "http://feeds.kentucky.statenews.net/rss/7dea3e4d4c76f3fa", "https://www.lex18.com/news/covering-kentucky.rss", "https://lexingtonky.news/feed/", "https://ky-leadernews.com/feed/", "https://www.wkrn.com/news/kentucky/feed/", "https://www.owensborotimes.com/feed/", "https://www.safetyandhealthmagazine.com/rss/topic/99-news"]
# more writing
urls2 = ["https://safetyrisk.net/feed/", "http://dramarnathgiri.blogspot.com/feeds/posts/default", "https://ohsinsider.com/feed/", "https://www.sindonews.com/feed", "https://www.surveysensum.com/feed", "https://asean.org/feed/", "https://mediaindonesia.com/feed", "https://www.weddingku.com/rss/", "https://businessnews.co.id/feed/", "https://www.viva.co.id/get/all", "http://feeds.indonesianews.net/rss/f9295dc05093c851"]

urls3 = ["https://www.atlantamagazine.com/feed/", "https://www.thefalcoholic.com/rss", "https://www.artsatl.org/feed/", "https://atlanta.eater.com/rss/index.xml", "https://365atlantatraveler.com/feed/", "http://feeds.feedblitz.com/atlonthecheap", "https://www.fanbolt.com/feed/", "http://www.ventureatlanta.org/feed/", "http://www.atlantaeats.com/feed/", "https://www.tonetoatl.com/feeds/posts/default"]

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


