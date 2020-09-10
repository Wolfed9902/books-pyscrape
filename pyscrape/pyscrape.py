# Extended Web Scraper (GUI)
# Author: Dylan Wolfe
# Date: 9/10/2020
# This program is specifically made to be used with books.toscrape.com.

#-- Imports --#

from tkinter import *
from tkinter import messagebox
from extendedscrape import scrape_page

root = Tk()
root.title('books-pyscrape (https://github.com/Wolfed9902)')

#-- Functions --#

def start_scrape():
    output = scrape_page(1)
    messagebox.showinfo("Results", output)

title_label = Label(root, text="Welcome to Books-Pyscrape!")
title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

page_label = Label(root, text="Choose a catalogue page to scrape (1-50)")
page_label.grid(row=1, column=0, columnspan=6, padx=10, pady=10)

button_scrape = Button(root, text="Scrape First Page", command=start_scrape)
button_scrape.grid(row=2, column=0)

root.mainloop()
