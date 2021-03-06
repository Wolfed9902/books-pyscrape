# Extended Web Scraper (GUI)
# Author: Dylan Wolfe
# Date: 9/10/2020
# This program is specifically made to be used with books.toscrape.com.

#-- Imports --#

from tkinter import *
from tkinter import messagebox
from extendedscrape import scrape_page, write_to_file, search_title

root = Tk()
root.title('books-pyscrape (https://github.com/Wolfed9902)')
#root.geometry("300x200")

#-- Functions --#

def start_scrape():

    try:
        page_num = int(page_select.get()) # Get page from page_select entry, check for int
        result_output = scrape_page(page_num)
        messagebox.showinfo("Results", result_output)
        write_to_file(result_output)
    except:
        messagebox.showerror("Error", "Please enter a valid number (1-50).")

    return

def start_title():

    try:
        book_title = (entry_search.get())
        result_output = search_title(book_title)
        write_to_file(result_output)
    except:
        messagebox.showerror("Error", "Invalid title.")

    return



#-- Layout --#

title_label = Label(root, text="Welcome to Books-Pyscrape!")
title_label.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

page_label = Label(root, text="Choose a catalogue page to scrape (1-50):")
page_label.grid(row=1, column=0, columnspan=6, padx=10, pady=10)

page_select = Entry(root, width=25)
page_select.grid(row=2, column=0, columnspan=6, padx=10, pady=10)

button_scrape = Button(root, text="Scrape Page", command=start_scrape)
button_scrape.grid(row=3, column=0, columnspan=6, pady=10, padx=10)

page_label = Label(root, text="Search for a book title:")
page_label.grid(row=4, column=0, columnspan=6, padx=10, pady=10)

entry_search = Entry(root, width=25)
entry_search.grid(row=5, column=0, columnspan=6, padx=10, pady=10)

button_search = Button(root, text="Search", command=start_title)
button_search.grid(row=6, column=0, columnspan=6, pady=10, padx=10)

root.mainloop()
