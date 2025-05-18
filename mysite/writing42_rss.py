import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://crypto.news/feed/", "https://www.coinbackyard.com/feed/", "https://www.cryptocurrencyscript.com/blog/feed", "https://coinlabz.com/feed/", "https://medium.com/feed/coinmonks", "https://news.bitcoin.com/feed/", "https://blog.bitfinex.com/feed/", "https://cryptoslate.com/feed/", "https://blog.bitmex.com/feed/"]
# more writing
urls1 = ["https://coincheckup.com/blog/feed/", "https://bitcoinik.com/feed/", "https://coinchapter.com/feed/", "https://coingeek.com/feed/", "https://coinjournal.net/feed/", "https://cryptoticker.io/en/feed/", "https://bitpinas.com/feed/", "https://cryptoadventure.com/feed/", "https://www.bitcoinmarketjournal.com/feed/", "https://www.trustnodes.com/feed", "https://coinrevolution.com/feed/", "https://coinidol.com/rss2/"]
# more writing
urls2 = ["https://bitcoinnews.com/feed/", "https://www.livebitcoinnews.com/feed/", "https://alexablockchain.com/feed/", "https://themerkle.com/feed/", "https://bitrss.com/rss.xml", "https://blocktelegraph.io/feed/", "https://themarketscompass.substack.com/feed", "https://ambcrypto.com/feed/", "https://decrypt.co/feed", "https://cryptonews.com/news/feed/", "https://www.bitdegree.org/crypto/news/rss"]

urls3 = ["https://u.today/rss", "https://coinpedia.org/feed/", "https://dailyhodl.com/feed/", "https://insidebitcoins.com/feed", "https://www.crypto-news-flash.com/feed/", "https://www.cryptela.com/blog-rss", "https://www.cryptonewsz.com/feed/", "https://nowpayments.io/blog/feed", "https://zebpay.com/feed", "https://zycrypto.com/feed/", "https://www.financemagnates.com/cryptocurrency/feed/"]

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


