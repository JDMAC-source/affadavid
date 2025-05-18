import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://3dnews.ru/news/rss", "https://mobile-review.com/all/feed/", "https://www.cnews.ru/inc/rss/biz.xml", "https://www.iphones.ru/feed", "https://xakep.ru/feed/", "https://appleinsider.ru/feed", "https://www.digitalhealth.net/news/feed/", "https://feeds.feedburner.com/KevinMd-MedicalWeblog", "https://hitconsultant.net/feed/", "https://www.fiercehealthcare.com/rss/xml", "https://feeds.feedburner.com/HealthcareIndustryTrendsBlog", "https://www.healthcaredive.com/feeds/news", "https://healthcareguys.com/feed/", "https://www.healthworkscollective.com/category/technology/feed/", "https://www.med-technews.com/api/rss/content.rss"]
# more writing
urls1 = ["https://histalk2.com/feed", "https://electronichealthreporter.com/feed/", "https://htn.co.uk/feed/", "https://feeds.feedburner.com/AustralianHealthInformationTechnology", "https://www.healthcareittoday.com/feed/", "https://www.healthcare.digital/blog-feed.xml", "https://www.ahrq.gov/rss.xml", "https://www.healthtechmagazines.com/feed/", "https://www.healthtechdigital.com/feed/"]
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





