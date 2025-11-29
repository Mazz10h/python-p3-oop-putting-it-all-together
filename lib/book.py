#!/usr/bin/env python3

class Book:

    def __init__(self, title="Unknown", page_count=0, author="Unknown"):
        self.title = title
        self.page_count = page_count
        self.author = author

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            print("title must be a string")
            return
        if not value.strip():
            print("title must be a non-empty string")
            return
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            print("author must be a string")
            return
        if not value.strip():
            print("author must be a non-empty string")
            return
        self._author = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
