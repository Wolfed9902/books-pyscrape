# Simple Web Scraper
# Author: Dylan Wolfe
# Date: 8/25/2020
# This program is specifically made to be used with books.toscrape.com.

#-- Imports --#
import re
from urllib.request import urlopen


#-- Functions --#
def scrape_init(select_num):

	# Open url and read HTML
	url = "http://books.toscrape.com/catalogue/page-%s.html" % select_num
	page = urlopen(url)
	html_encoded = page.read()
	html = html_encoded.decode("utf-8")

	return html

def scrape_title(html):

	# Find all titles on page
	title_re = '<a href=.*?title=.*?</a.*?>' # First 'title' tag and the '/title' tag that comes after.
	title_results = re.findall(title_re, html, re.IGNORECASE)

	title_results[:] = [re.sub('<.*?title="', "", entry) for entry in title_results] # Subtract left-side filler
	title_results[:] = [re.sub('".*?a>', '', entry) for entry in title_results] # Subtract right-side filler

	return(title_results)

def scrape_price(html): # For books.toscrape.com

	# Find all prices on page
	price_re = '<p class="price_color".*?</p>'
	price_results = re.findall(price_re, html, re.IGNORECASE)

	price_results[:] = [re.sub('<.*?>', "", entry) for entry in price_results] # Subtract tags

	return(price_results)

def scrape_page(select_num):

	# Call func to retreive page html.
	raw_html = scrape_init(select_num)

	# Call funcs to extract titles and prices.
	title_list = scrape_title(raw_html)
	price_list = scrape_price(raw_html)

	# Creates a dictionary that contains titles with matching prices.
	combined_list = {title_list[entry]: price_list[entry] for entry in range(len(price_list))}

	scrape_dict_output(combined_list)

	return

def select_page():

	# Choose page according to user input

	while True:
		select_num = input("Choose a catalogue page to scrape (1-50).\n")
		try:
			select_num = int(select_num)
		except:
			print("Please enter a number. (1-50)\n")
			continue
		if select_num < 1 or select_num > 50:
			print("Please enter a number. (1-50)\n")
			continue
		break

	scrape_page(select_num)

	return

def scrape_dict_output(dict):

	# Nicely ordered dictionary output

	print("Results:")
	for title, price in dict.items():
		print("{} [{}]".format(title, price))

	return

#-- MAIN --#

select_page()

input('Press Enter to end the program.')
