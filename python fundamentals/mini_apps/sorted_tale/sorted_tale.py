#! /usr/bin/env python3

import utils
import sorts


def print_titles(shelf):
    for book in shelf:
        print(book['title'])


def print_authors(shelf):
    for book in shelf:
        print(book['author'])


bookshelf = utils.load_books('books_small.csv')
print_titles(bookshelf)


# Comparison Functions
# - By Title
def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']


# - By Author
def by_author_ascending(book_a, book_b):
    return book_a['author_lower'] > book_b['author_lower']


# - By length of total characters in title and authors name
def by_total_length(book_a, book_b):
    return len(book_a['author_lower']) + len(book_a['title_lower']) > \
           len(book_b['author_lower']) + len(book_b['title_lower'])


sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
print_titles(bookshelf)

# Create a copy so we don't alter the
# original
bookshelf_v1 = bookshelf.copy()
print_authors(bookshelf_v1)
sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
print_authors(bookshelf_v1)
# 26 swaps!!! That's a lot.

# Create another copy
bookshelf_v2 = bookshelf.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
print_authors(bookshelf_v2)


# Load Larger Bookshelf
long_bookshelf = utils.load_books('books_large.csv')
# sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)
# Bubble sort: There were 1092069 swaps
sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1 , by_total_length)