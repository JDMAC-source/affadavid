import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://www.adazing.com/feed/", "https://www.goodkindles.net/feeds/posts/default", "https://gointothestory.blcklst.com/feed", "https://www.writeoutloud.net/rss/blogrss.xml", "https://poetryblog.co.uk/feed/", "https://anotherporch.blogspot.com/feeds/posts/default?alt=rss", "http://odeamichael.blogspot.com/feeds/posts/default?alt=rss", "https://fourcalendarcafe.com/feed/", "https://bartbarkerpoet.com/feed/", "https://stacey-c-johnson.com/feed/", "https://buffer.com/resources/rss/", "https://www.searchenginejournal.com/feed/atom/", "https://www.bkacontent.com/feed/", "https://www.socialsellinator.com/social_selling_blog/rss.xml", "https://seths.blog/feed/atom/", "https://blog.hootsuite.com/feed/", "https://www.semrush.com/blog/feed/", "https://www.socialmediaexaminer.com/feed/", "https://feeds2.feedburner.com/CMSWire", "https://searchengineland.com/feed", "https://digiday.com/feed/", "https://sproutsocial.com/insights/feed/"]
# more writing
urls1 = ["https://www.theparisreview.org/blog/feed/", "http://feeds.feedburner.com/mcsweeneys", "https://janefriedman.com/blog/feed/", "https://electricliterature.com/feed/", "https://lithub.com/feed/", "https://bookriot.com/feed/", "https://i-libri.com/feed/", "https://www.writersdigest.com/.rss/full/", "https://www.complete-review.com/saloon/rss.xml", "https://publicdomainreview.org/rss.xml", "https://www.the-tls.co.uk/feed/", "http://brittlepaper.com/feed/", "https://www.full-stop.net/feed/", "https://spillwords.com/feed/", "https://www.hilobrow.com/feed/", "https://theravensperch.com/feed/", "https://lucianoduarte.com/en/feed/", "https://sourceessay.com/feed/", "https://coursepivot.com/feed/", "http://www.insidehighered.com/rss/feed/ihe", "https://www.weareteachers.com/feed", "http://www.middleweb.com/feed/", "https://www.awai.com/rss/main/rss.xml", "https://feeds.feedburner.com/SeoSandwitch", "https://reactormag.com/feed/", "https://fictionophile.com/feed/"]
# more writing
urls2 = ["https://www.christianbookfinds.com/blog?format=rss", "https://www.freedomfiction.com/feed/", "https://booksbonesbuffy.com/feed/", "https://fictionhorizon.com/feed/", "http://www.crimefictionlover.com/feed/", "https://acfw.com/acfw-blog/feed/", "http://www.longandshortreviews.com/feed/", "https://fromthetbrpile.blogspot.com/feeds/posts/default", "https://bloody-disgusting.com/feed/", "https://www.ihorror.com/feed/", "https://www.dreadcentral.com/feed/", "http://www.screamhorrormag.com/feed/", "https://www.creepypasta.com/feed/", "https://bloghorror.com/feed", "https://dailydead.com/feed/", "https://horrorfacts.com/feed/", "https://www.horrorbuzz.com/feed/", "https://moonmausoleum.com/feed/", "https://horror.org/category/blog/feed/", "https://moviesandmania.com/category/horror/feed/", "https://horrorpatch.com/feed/", "http://realmofhorror-blog.blogspot.com/feeds/posts/default?alt=rss", "https://www.youtube.com/feeds/videos.xml?channel_id=UCu0bxC7vG_HKWJ7ijO9QKwg", "https://moonmausoleum.com/feed/"]


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