import requests
import time


import feedparser
from requests import get

base = ""
urls = ["http://www.askamanager.org/feed", "https://www.careeraddict.com/rss_feeds/articles.rss", "https://www.inspireglobalsolutions.com/feed/", "https://careeralley.com/feed/", "https://www.personalbrandingblog.com/feed/", "https://eatyourcareer.com/feed/", "https://middleme.net/feed/", "https://mysteryfile.com/blog/?feed=rss2", "http://feeds.feedburner.com/blogspot/therapsheet", "https://www.escapewithdollycas.com/feed/", "https://drusbookmusing.com/feed/", "https://shortmystery.blogspot.com/feeds/posts/default?alt=rss", "https://lesasbookcritiques.com/feed/", "http://feeds.feedblitz.com/omnimysterynews", "https://www.criminalelement.com/feed/", "https://writerswhokill.blogspot.com/feeds/posts/default", "https://mysteryreadersinc.blogspot.com/feeds/posts/default", "https://brevity.wordpress.com/feed/", "https://www.journeysixty6.com/blog.rss", "http://heppas.blogspot.com/feeds/posts/default", "https://ysbookreviews.wordpress.com/feed/"]
# more writing
urls1 = ["https://www.apartmenttherapy.com/main.rss", "https://techcrunch.com/feed/", "https://www.billboard.com/feed/", "https://gizmodo.com/rss", "http://feeds.mashable.com/mashable", "http://lifehacker.com/index.xml", "https://feeds.feedburner.com/blogspot/bboSV", "http://feeds.hbr.org/harvardbusiness", "http://www.engadget.com/rss.xml", "http://www.theverge.com/rss/frontpage", "https://www.entrepreneur.com/latest.rss", "https://www.fastcompany.com/latest/rss?truncated=true", "https://perezhilton.com/feed/", "http://feeds.kottke.org/main", "http://www.tmz.com/rss", "https://www.wired.com/feed/rss", "http://www.gq.com/services/rss/feeds/latest.xml", "http://feeds.arstechnica.com/arstechnica/index/", "http://hotair.com/feed", "https://www.nme.com/feed", "https://talkingpointsmemo.com/feed", "https://www.ibelieve.com/rss/", "https://www.womenoffaith.com/blog.rss", "http://blog.lifeway.com/womenallaccess/feed/", "https://cdn.reviveourhearts.com/podcasts/revive-our-hearts.rss"]
# more writing
urls2 = ["https://www.worthbeyondrubies.com/feed/", "https://ichoosemybestlife.com/feed/", "http://www.w2wministries.org/feeds/posts/default", "https://sarahsundy04.blogspot.com/feeds/posts/default", "https://annmariepablico.com/feed/", "https://www.thisiscolossal.com/feed/", "https://hyperallergic.com/feed/", "https://www.artforum.com/rss", "https://bottleneckgallery.com/blogs/news.atom", "https://lauriepace.blogspot.com/feeds/posts/default?alt=rss", "https://www.youtube.com/feeds/videos.xml?channel_id=UCWQDLMCM7FdlhAM6jPIycbA", "https://feeds.feedburner.com/50WordStories", "https://folksburywoods.com/feed/", "https://shortmystery.blogspot.com/feeds/posts/default?alt=rss", "https://flashfictionmagazine.com/feed/", "https://www.classroomfreebies.com/feeds/posts/default?alt=rss", "https://wordhistories.net/feed/", "https://worshipleader.com/feed/", "https://www.worshipideas.com/feed/", "https://www.experiencingworship.com/exw.rss", "https://www.positive.news/feed/", "https://mypositiveoutlooks.com/feed/"]


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