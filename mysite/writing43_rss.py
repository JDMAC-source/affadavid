import requests
import time


import feedparser
from requests import get

base = ""
urls = ["https://blockchain.news/rss", "https://thecryptobasic.com/feed/", "https://webscrypto.com/feed/", "https://stealthex.io/blog/feed/", "https://thenewscrypto.com/feed/", "https://dailycoin.com/feed/", "https://blockonomi.com/feed/", "https://bravenewcoin.com/insights/rss", "https://cryptonews.com.au/feed/", "https://coindoo.com/feed/", "https://cryptoshrypto.com/feed/"]
# more writing
urls1 = ["https://thebitcoinnews.com/feed/", "https://nulltx.com/feed/", "https://boxmining.com/feed/", "https://fullycrypto.com/feed", "https://www.tronweekly.com/feed/", "https://crypto-economy.com/feed/", "https://cryptocurrency-coins.blogspot.com/feeds/posts/default", "https://www.cryptobreaking.com/feed/", "https://www.platinumcryptoacademy.com/feed/", "https://www.crypto-news.net/feed/"]
# more writing
urls2 = ["https://coin24h.com/feed/", "https://www.btcethereum.com/blog/feed/", "https://www.kanalcoin.com/feed/", "https://usethebitcoin.com/feed", "https://visionary-finance.com/feed/gn", "https://www.fxopen.blog/feed/", "https://bitcoinchaser.com/feed/", "https://coingape.com/feed/", "https://bitcoinethereumnews.com/feed", "https://cryptogiggle.com/feed/", "https://changelly.com/blog/feed/"]

urls3 = ["https://crypto.aabeyllc.com/feed/", "https://cryptocurrencynews.com/feed/", "https://blocknewsmedia.com/feed/", "https://www.ft.com/rss/home"]

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


