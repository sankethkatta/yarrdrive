import requests, os
from redis import StrictRedis; redis = StrictRedis(db=1)
from bs4 import BeautifulSoup
import re

page = requests.get("http://www.imdb.com/search/title?title_type=tv_series").text
soup = BeautifulSoup(page)

shows = {}
all_links = soup.findAll(attrs={"href": re.compile("/title/.*")})

for link in all_links:
    if link.text != "":
        shows[link.text] = {'name': link.text, 'url': link.attrs['href'], 'img': ""}

for show, details in shows.iteritems():
    show_page = requests.get("http://www.imdb.com%s" % details['url']).text
    show_soup = BeautifulSoup(show_page)
    img_td = show_soup.find(attrs={"id": "img_primary"})
    shows[show]['img'] = img_td.findNext('img').attrs['src']

    cleaned_show = show.capitalize().replace(" ", "_") 
    os.system("wget -O %s %s" % ("covers/"+cleaned_show+".jpg", shows[show]['img']))

    
    #redis.hset("tv:%s" & redis.incr('tv'), details)

import pdb; pdb.set_trace()
