# Comprehensive Changelog

## (8/27/2020)

* Added core functionality for scraping from books.toscrape.com.

Functionality includes scrape functions that can retrieve both book titles and prices from the website, as well as compress the separate ordered lists into a dictionary. As of currently, data is retrieved from the first page of the catalogue.

## (8/28/2020)

* Added a simple page selection function with input verification.
* User can now scrape a specific page by number rather than only scrape the first.

## (8/30/2020)

* Modified output formatting and added improved display of scrape results.

## (9/10/2020)

- Added pyscrape.py and extendedscrape.py
  - pyscrape.py contains GUI functionality via tkinter module.
  - extendedscrape.py contains core scrape functionality with pyscrape.py in mind. This will include advanced functions beyond scrape.py
- Initialized a simple, temporary GUI.
- User can currently use the GUI to scrape the first page of books.toscrape.com.

## (9/15/2020)
 - Modified GUI
 - User can now scrape page of their choice
  - Added entry box for page selection
  - Added input validation (general exception)

## (9/20/2020)
 - Scraping a page now creates a file with scrape results in directory 'pyscrape'.
   - File is currently overwritten each scrape.

## (10/11/2020)
 - Initialize search functionality

## (10/25/2020)
 - Fixed bug with duplicate button/entry widget names

## (1/14/2021)
 - Preparation for title search implementation

## (1/29/2021)
 - Basic title search functionality implemented
  - Search only writes to scrape_output.txt as of currently
  - Search only returns first pages
  - Search is broad and returns any title with matching letter/word
