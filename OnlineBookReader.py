import os
import random
import re
import sys

class Book:
    def __init__(self, pages, author, title, version="Standard"):
        self.content = pages
        self.length = len(pages)
        self.author = author
        self.title = title
        self.version = version
    def __eq__(self, other):
        return (self.author == other.author and
        self.title == other.title and self.version == other.version)

    def __hash__(self):
        return hash((self.author,self.title,self.version))

    class BookProgress:
        def __init__(self, book):
            self.__book = book
            self.current_page = 0

        def get_current_page(self):
            return self.__book.content[self.current_page]
        
        def next_page(self):
            if self.current_page + 1 <= self.__book.length:
                self.current_page += 1
                return self.__book.content[self.current_page]
            else:
                return None

        def previous_page(self):
            if self.current_page > 0:
                self.current_page -= 1
                return self.__book.content[self.current_page]
            else:
                return None

        def peek_page(self, page):
            if page >= 0 and page <= self.__book.length:
                return self.__book.content[page]
        


class OnlineReader:
    def __init__(self, site_name, intial_books=None):
        self.site_name = site_name
        self.usernames = set()
        self.users = []
        if not intial_books:
            self.__book_set = set()
            self.library = dict()
        else:
            self.__book_set = set(intial_books)
            self.library = dict()
            for b in self.__book_set:
                if not self.library.get(b.author, False):
                    self.library[b.author] = [b]
                else:
                    self.library[b.author].append(b)

    def add_books(self, books):
        for b in books:
            if b not in self.__book_set:
                self.__book_set.add(b)
                if not self.library.get(b.author, False):
                    self.library[b.author] = [b]
                else:
                    self.library[b.author].append(b)

    def new_user(self, username):
        if username in self.usernames:
            return None
        self.usernames.add(username)
        self.users.append(User(username,self))

    class User:
        def __init__(self, username, site):
            self.site = site
            self.username = username
            self.__book_set = set()
            self.books_progress = []

        def get_book(self, author, title, version=None):
            book = None
            for b in self.site.library.get(author,[]):
                if b.title == title and (version is None or b.version == version):
                    if b not in self.__book_set:
                        book = b
                        break
            if book:
                self.books_progress.append(Book.BookProgress(book))
                return self.books_progress[-1]
            return None
            

    
