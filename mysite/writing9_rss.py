import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://screenrant.com/feed/movie-reviews/", "https://movieweb.com/rss/movie-reviews", "https://www.sbs.com.au/movies/rss", "https://theplaylist.net/category/reviews/feed/", "https://creativejamie.com/feed/", "https://www.theaceblackblog.com/feeds/posts/default?alt=rss", "https://moviesreview101.com/feed/", "https://collider.com/feed/category/all-reviews/", "https://www.highonfilms.com/feed/", "https://www.themovieblog.com/feed/", "https://rogersmovienation.com/feed/", "https://www.sknr.net/feed/", "https://lylesmoviefiles.com/feed/", "https://everymoviehasalesson.com/blog?format=RSS", "https://indyfilmlibrary.com/feed/"]
# more writing
urls1 = ["https://anygoodfilms.com/feed/", "https://themovierevue.com/feed/", "https://www.cinema-crazed.com/blog/feed/", "https://eofftvreview.wordpress.com/feed/", "https://feeds.feedburner.com/blogspot/vpAFr", "http://marginalrevolution.com/feed", "https://econbrowser.com/feed", "http://www.nakedcapitalism.com/feed", "https://www.econlib.org/feed/main", "http://www.calculatedriskblog.com/feeds/posts/default", "https://inomics.com/insights-rss", "https://ritholtz.com/feed/", "https://www.capitalspectator.com/feed/", "https://www.ft.com/stream/sectionsId/MTA3-U2VjdGlvbnM=?format=rss"]
# more writing
urls2 = ["https://braddelong.substack.com/feed", "http://feeds.feedburner.com/zerohedge/feed", "https://www.armstrongeconomics.com/feed/", "https://mises.org/dailyarticles.xml", "https://www.aier.org/feed/", "http://cafehayek.com/feed", "https://www.alt-m.org/feed/", "https://angrybearblog.com/feed", "https://www.specificfeeds.com/arcadiaeconomics", "https://mostlyeconomics.wordpress.com/feed/", "https://econlife.com/feed/", "https://larspsyll.wordpress.com/feed/", "http://bonddad.blogspot.com/feeds/posts/default", "https://thedangerouseconomist.blogspot.com/feeds/posts/default", "https://robertvienneau.blogspot.com/feeds/posts/default"]


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