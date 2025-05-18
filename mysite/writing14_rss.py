import requests
import time


import feedparser
from requests import get

base = ""
urls = ["http://feeds.weblogssl.com/applesfera", "https://feeds2.feedburner.com/ElBlogDeEnriqueDans", "https://www.htcmania.com/external.php?type=RSS2", "https://www.microsiervos.com/index.xml", "https://hipertextual.com/tecnologia/feed", "https://computerhoy.com/rss_all/all/rss.xml", "http://feeds.weblogssl.com/xataka2", "http://feeds.weblogssl.com/genbeta", "https://www.muycomputer.com/feed/", "https://www.tuexperto.com/feed/", "https://feeds.feedburner.com/andro4all", "https://feeds.feedburner.com/ipadizate", "https://www.movilzona.es/feed/?post_type%5B0%5D=post&post_type%5B1%5D=page&post_type%5B2%5D=best-pages&post_type%5B3%5D=branded&post_type%5B4%5D=noticias&post_type%5B5%5D=reportajes&post_type%5B6%5D=product&post_type%5B7%5D=tutoriales"]
# more writing
urls1 = ["https://tecknexus.com/feed/", "https://www.5gtechnologyworld.com/feed/", "https://www.theverge.com/tech/rss/index.xml", "https://www.theverge.com/science/rss/index.xml", "https://www.theverge.com/rss/creators/index.xml", "https://www.theverge.com/rss/environment/index.xml", "https://www.theverge.com/rss/entertainment/index.xml", "https://www.theverge.com/transportation/rss/index.xml", "https://www.theverge.com/reviews/rss/index.xml", "https://www.equipmentworld.com/feed/", "https://feeds.feedburner.com/StateTech", "https://www.nextgov.com/rss/all/", "https://governmenttechnologyinsider.com/feed/", "https://www.govpilot.com/blog/rss.xml", "https://www.fiercewireless.com/rss/xml", "https://www.rcrwireless.com/feed"]
# more writing
urls2 = ["https://blogs.cisco.com/tag/wireless/feed", "https://www.banglatribune.com/feed/tech-and-gadget", "https://adamlobo.tv/feed/", "https://omghackers.com/feed/", "https://nasilemaktech.com/feed/", "https://klgadgetguy.com/feed/", "https://amanz.my/feed/", "https://pokde.net/feed", "https://productnation.co/my/feed/", "https://technave.com//feed", "https://soyacincau.com/feed/", "https://www.lowyat.net/feed/", "https://technode.com/feed/", "https://www.techinasia.com/tag/china/feed", "https://pandaily.com/feed/", "http://www.technologynewschina.com/feeds/posts/default?alt=rss", "https://chinese.engadget.com/rss.xml", "https://attoday.co.uk/feed/", "https://www.itnews.com.au/rss/rss.ashx", "https://www.cravingtech.com/feed", "https://techau.com.au/feed/"]

urls3 = ["https://www.zdnet.com/au/rss.xml", "https://propakistani.pk/category/tech-and-telecom/feed/", "https://www.techjuice.pk/feed/", "https://www.technologistan.pk/feed/", "https://researchsnipers.com/category/tech/feed/", "https://tribune.com.pk/feed/technology", "https://startuppakistan.com.pk/category/tech/feed/", "https://www.aajenglish.tv/feeds/technology/", "https://www.digitalinformationworld.com/feeds/posts/default", "https://www.pctipp.ch/PCTIPP-Newsfeed.html", "https://techcentral.co.za/feed/", "https://mybroadband.co.za/news/feed", "https://www.itweb.co.za/rss", "https://stuff.co.za/feed/", "https://bandwidthblog.co.za/feed/", "https://www.bizcommunity.com/rss/196/706.html", "https://techfinancials.co.za/feed/"]

urls4 = ["https://capetownguy.co.za/category/latest-news/technews/feed/", "https://www.techafricanews.com/feed/", "http://feeds.news24.com/articles/news24/SouthAfrica/rss", "https://rss.iol.io/iol/news/south-africa/gauteng", "https://businesstech.co.za/news/feed/", "https://www.theedgesearch.com/feeds/posts/default?alt=rss", "https://www.techfinancials.co.za/feed/", "https://www.digitalstreetsa.com/feed/", "https://www.smetechguru.co.za/feed/", "https://www.businesstechafrica.co.za/feed/", "https://www.thesouthafrican.com/technology/feed/", "https://techdailypost.co.za/feed/", "https://www.techinafrica.com/feed/", "https://www.embedded.com/feed/", "https://www.cnx-software.com/feed/", "https://hackaday.com/feed/"]

urls5 = ["https://www.eejournal.com/category/embedded/feed/", "https://circuitcellar.com/category/cc-blog/feed/", "https://linuxgizmos.com/feed/", "https://www.fenews.co.uk/category/edtech/feed/", "https://meetings.skift.com/feed/", "https://www.eventindustrynews.com/category/news/event-technology/feed", "https://www.hdblog.it/feed/", "https://feeds.hwupgrade.it/rss_news.xml", "https://www.wired.it/feed/rss", "https://www.androidworld.it/feed/", "https://feeds.feedburner.com/Androidiani", "https://www.navigaweb.net/feeds/posts/default?alt=rss", "https://www.telefonino.net/feed/", "https://www.webnews.it/feed/", "https://www.smartworld.it/feed", "https://www.macitynet.it/feed/", "https://www.giardiniblog.it/feed"]

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


for rss_url in urls4:
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



for rss_url in urls5:
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