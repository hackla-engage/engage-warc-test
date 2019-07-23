# Engage parser test repo

This repo will contain saved instances of Santa Monica website in warc format

## Depends

`git pip3 pyenv-virtualenv python3`

OSX

`brew install git pyenv-virtualenv python3`



## How to install
```
git clone https://github.com/hackla-engage/engage-warc-test.git
cd engage-warc-test
virtualenv venv/ --no-site-packages
source venv/bin/activate
pip3 install -r requirements.txt
```


## How to playback archives
```
wayback
```



## How to record pages
```
wayback --record --live -a
navigate to http://localhost:8080/smgov/record/<url> in the browser # --auto-interval is unnecessary
```

## How to reindex collections
```
wb-manager reindex smgov
```

## HackforLa Scraper Library

https://github.com/hackla-engage/engage-scraper

### Models
https://github.com/hackla-engage/engage-scraper/blob/master/engage_scraper/scraper_logics/santamonica_scraper_models.py

### Process
https://github.com/hackla-engage/engage-scraper/blob/master/engage_scraper/scraper_logics/santamonica_scraper_logic.py 

## Source Website
https://www.smgov.net/departments/clerk/agendas.aspx

https://www.smgov.net/departments/clerk/AgendasRssToHTML.aspx

https://www.smgov.net/departments/clerk/agendas_rss.ashx

## Depends
https://pywb.readthedocs.io/en/latest/index.html

https://warc.readthedocs.io/en/latest/

## Helpful Links
standalone warc player https://github.com/webrecorder/webrecorder-player
