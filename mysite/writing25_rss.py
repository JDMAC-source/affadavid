import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://economictimes.indiatimes.com/mf/mf-news/rssfeeds/1107225967.cms", "https://economictimes.indiatimes.com/industry/renewables/rssfeeds/81585238.cms", "https://economictimes.indiatimes.com/industry/indl-goods/svs/rssfeeds/13357688.cms", "https://economictimes.indiatimes.com/industry/healthcare/biotech/rssfeeds/13358050.cms", "https://economictimes.indiatimes.com/industry/services/rssfeeds/13354120.cms", "https://economictimes.indiatimes.com/industry/media/entertainment/rssfeeds/13357212.cms", "https://economictimes.indiatimes.com/industry/transportation/rssfeeds/13353990.cms", "https://economictimes.indiatimes.com/rssfeeds/13357270.cms"]
# more writing
urls1 = ["https://economictimes.indiatimes.com/small-biz/sme-sector/rssfeeds/11993058.cms", "https://economictimes.indiatimes.com/small-biz/trade/rssfeeds/68806566.cms", "https://economictimes.indiatimes.com/wealth/tax/rssfeeds/47119912.cms", "https://economictimes.indiatimes.com/wealth/save/rssfeeds/47119915.cms", "https://economictimes.indiatimes.com/wealth/invest/rssfeeds/48997553.cms", "https://economictimes.indiatimes.com/tech/information-tech/rssfeeds/78570530.cms", "https://economictimes.indiatimes.com/tech/technology/rssfeeds/78570561.cms", "https://economictimes.indiatimes.com/tech/funding/rssfeeds/78570550.cms", "https://economictimes.indiatimes.com/tech/startups/rssfeeds/78570540.cms"]
# more writing
urls2 = ["https://economictimes.indiatimes.com/jobs/hr-policies-trends/rssfeeds/98937485.cms", "https://economictimes.indiatimes.com/jobs/exams-results/rssfeeds/97860466.cms", "https://economictimes.indiatimes.com/opinion/et-editorial/rssfeeds/3376910.cms", "https://economictimes.indiatimes.com/opinion/et-commentary/rssfeeds/3389985.cms", "https://economictimes.indiatimes.com/opinion/speaking-tree/rssfeeds/52109321.cms", "https://economictimes.indiatimes.com/nri/migrate/rssfeeds/79038827.cms", "https://economictimes.indiatimes.com/nri/visit/rssfeeds/79038765.cms", "https://economictimes.indiatimes.com/magazines/et-magazine/rssfeeds/7771003.cms", "https://economictimes.indiatimes.com/jobs/rssfeeds/107115.cms"]

urls3 = ["https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms", "https://economictimes.indiatimes.com/News/rssfeeds/1715249553.cms", "https://economictimes.indiatimes.com/prime/rssfeeds/69891145.cms", "https://economictimes.indiatimes.com/small-biz/rssfeeds/5575607.cms", "https://economictimes.indiatimes.com/wealth/rssfeeds/837555174.cms", "https://economictimes.indiatimes.com/mf/rssfeeds/359241701.cms", "https://economictimes.indiatimes.com/opinion/rssfeeds/897228639.cms", "https://economictimes.indiatimes.com/magazines/rssfeeds/1466318837.cms", "https://economictimes.indiatimes.com/markets/ipos/fpos/rssfeeds/14655708.cms", "https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms"]

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


