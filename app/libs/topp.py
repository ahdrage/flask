
from bs4 import BeautifulSoup
from app import db
from app.models import Listing

import requests
import sqlite3 as lite
import sys
import spotipy

s_client = spotipy.Spotify()

con = lite.connect('toplist.db')

#import pandas as pd

from random import randint
from time import sleep

#initial url and make it possible to use soup to get the url for the back button. 
url = requests.get('http://lista.vg.no/liste/topp-20-single/1/dato/2004/uke/46')
data = url.text
soup = BeautifulSoup(data, 'html.parser')
counter = 0
tracks = []
fullUrl = ""

for listing in Listing.query.all():
	db.session.delete(listing)
db.session.commit()



#script goes until we reach the last page  
while not fullUrl.endswith('dato/2004/uke/43'):

	#getting part of url from the "forrige" (previous page) button. 
	partUrl = (soup.tr.a).get("href")
	fullUrl = "http://lista.vg.no" + partUrl
	url = requests.get(fullUrl)
	data = url.text
	soup = BeautifulSoup(data, 'html.parser') 

	artist = soup.find('tbody').find('tr').find('a', attrs={'class':'artist'}).text
	findTitle = soup.find('tbody').find('tr').find('a', attrs={'class':'album'})
	title = findTitle['title']

	year = int(fullUrl.split('/')[-3])
	weekNumber = int(fullUrl.split('/')[-1])

	results = s_client .search(title, limit=1)
	spotifyUrl = results['tracks']['items'][0]['preview_url']
	spotifyId =  results['tracks']['items'][0]['id']
	image = results['tracks']['items'][0]['album']['images'][0]['url']

	

	listing = Listing(
		year=year,
    		week_number=weekNumber,
    		artist=artist,
  		title=title,
    		spotify_url=spotifyUrl,
    		spotify_id=spotifyId,
    		image=image
	)
	db.session.add(listing)
	db.session.commit()
	
