import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.atlantarealestateforum.com/feed/", "https://www.peachtreehoops.com/rss/index.xml", "https://www.idahofallsidaho.gov/RSSFeed.aspx?ModID=1&CID=All-newsflash.xml", "https://www.eastidahonews.com/feed/", "https://localnews8.com/feed/", "https://www.boisestatepublicradio.org/news.rss", "https://www.idahoednews.org/feed/", "https://kidotalkradio.com/feed/", "https://idahobusinessreview.com/feed/", "https://idahodispatch.com/feed/"]
# more writing
urls1 = ["https://idahocapitalsun.com/feed/", "https://www.politicshome.com/social-affairs/rss", "http://feeds.feedburner.com/daily-express-weather", "https://www.spendwithpennies.com/feed/", "https://feeds.distribution.dotdashmeredith.com/v3/rss/62c70e16-3226-4bc0-879f-b3ef408d0972", "https://juliasalbum.com/feed/", "https://whatsgabycooking.com/feed/", "https://www.rachelcooks.com/feed/", "https://tastecooking.com/feed/", "https://mommyshomecooking.com/feed/"]
# more writing
urls2 = ["http://angiesrecipes.blogspot.com/feeds/posts/default?alt=rss", "http://barbbrinker.blogspot.com/feeds/posts/default?alt=rss", "https://tastesbetterfromscratch.com/feed/", "https://communitynewspapers.com/category/miami-gardens-news/feed/", "https://www.airedalebka.org.uk/blog-feed.xml", "https://homebusinessmag.com/feed", "https://thinkoutsidethecubiclenow.com/feed/", "https://flamesnation.ca/feed/", "https://feeds.feedburner.com/CalgaryDealsBlog"]

urls3 = ["https://itsdatenight.com/feed/", "https://calgaryherald.com/category/life/swerve/feed", "https://www.mysanantonio.com/default/feed/local-news-176.php", "https://sanantonioreport.org/feed/", "https://www.sacurrent.com/sanantonio/Rss.xml", "http://feeds.bizjournals.com/bizj_sanantonio", "https://sanantonio.culturemap.com/feeds/news/?format=xml", "http://feeds.thesanantonionews.net/rss/f18f75b7970654da", "https://www.kens5.com/feeds/syndication/rss/news/local"]

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


