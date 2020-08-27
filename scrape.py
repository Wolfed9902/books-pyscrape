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

	# Find all titles on page
	title_re = '<a href=.*?title=.*?</a.*?>' # First 'title' tag and the '/title' tag that comes after.
	title_results = re.findall(title_re, html, re.IGNORECASE)

	title_results[:] = [re.sub('<.*?title="', "", entry) for entry in title_results] # Subtract left-side filler
	title_results[:] = [re.sub('".*?a>', '', entry) for entry in title_results] # Subtract right-side filler

	#print(title_results)

	return(title_results)

def scrape_price(html): # For books.toscrape.com

	# Find all prices on page
	price_re = '<p class="price_color".*?</p>'
	price_results = re.findall(price_re, html, re.IGNORECASE)

	price_results[:] = [re.sub('<.*?>', "", entry) for entry in price_results]

	#print(price_results)

	return(price_results)

#-- MAIN --#

raw_html = scrape_init()

title_list = scrape_title(raw_html)
price_list = scrape_price(raw_html)

# Creates a dictionary that contains titles with matching prices. 
combined_list = {title_list[entry]: price_list[entry] for entry in range(len(price_list))}

print(combined_list)

input('Press Enter to end the program.')
