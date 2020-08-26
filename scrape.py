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

	# Find book title
	title_re = "<a href=.*?.*?</a.*?>" # First 'title' tag and the '/title' tag that comes after.
	match_results = re.search(title_re, html, re.IGNORECASE)
	title = match_results.group()
	title = re.sub("<.*?>", "", title) # Remove tags

	print(title)

	return

def scrape_price(html): # For books.toscrape.com

	# Find price
	pricetag_index = html.find("<p class='price_color'>")
	start_index = pricetag_index + len("<p class='price_color'>")
	end_index = html.find("</p>")
	price = html[start_index:end_index]

	print(price)

	return

#-- MAIN --#

raw_html = scrape_init()

scrape_title(raw_html)


input('Press Enter to end the program.')
