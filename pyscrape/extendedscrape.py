# Extended Web Scraper
# Author: Dylan Wolfe
# Date: 9/10/2020
# This program is specifically made to be used with books.toscrape.com.
# This version of scrape.py is made specifically for use with pyscrape.py

#-- Imports --#

import re
from urllib.request import urlopen
from scrape import scrape_init, scrape_title, scrape_price

#-- Functions --#

def scrape_page(select_num):

	# Call func to retreive page html
	raw_html = scrape_init(select_num)

	# Call funcs to extract titles and prices
	title_list = scrape_title(raw_html)
	price_list = scrape_price(raw_html)

	# Creates a dictionary that contains titles with matching prices
	combined_list = {title_list[entry]: price_list[entry] for entry in range(len(price_list))}

	formatted_list = format_output(combined_list)

	return formatted_list

def format_output(dict):

	formatted_list = ""
	bad_chars = ["&#39;"] # artifacts from scrape

	# Nicely ordered dictionary output
	for title, price in dict.items():
		formatted_list += ("{} [{}]".format(title, price))
		formatted_list += ("\n")

	# Replace broken characters in list
	for i in bad_chars:
		formatted_list = formatted_list.replace(i,"'")

	return formatted_list

def write_to_file(list):

	output_file = open("scrape_output.txt", "w")
	output_file.write(list)
	output_file.close

	return

def search_title(book_title):

	# TODO - Search for a title within the catalogue

	i = 1
	title = book_title
	total_scrape = ""

	i = 1
	while i < 4: # scrape the first three pages
		i += 1
		total_scrape += scrape_page(i)

	return total_scrape
