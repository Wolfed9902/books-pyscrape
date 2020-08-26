# Simple Web Scraper
# Author: Dylan Wolfe
# Date: 8/25/2020
#

#-- Imports --#
import re
from urllib.request import urlopen


#-- Functions --#
def scrape_init():

	# Open url and read HTML
	url = "http://books.toscrape.com/"
	page = urlopen(url)
	html_encoded = page.read()
	html = html_encoded.decode("utf-8")

	#print(html)

	return html

def scrape_title(html):

	# Find all titles
	title_re = '<a href=.*?title=.*?</a.*?>' # First 'title' tag and the '/title' tag that comes after.
	title_results = re.findall(title_re, html, re.IGNORECASE)

	title_results[:] = [re.sub("<.*?>", "", entry) for entry in title_results]

	#title = match_results.group()
	#title = re.sub("<.*?>", "", title) # Remove tags

	print(title_results)

	return

def scrape_price(html): # For books.toscrape.com

	# Find price

	print(price)

	return

#-- MAIN --#

raw_html = scrape_init()

scrape_title(raw_html)


input('Press Enter to end the program.')
