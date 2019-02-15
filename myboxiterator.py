# -*- coding: utf-8 -*-


class MyBoxIterator(object):
    def __init__(self, film_shell: list):
        self.film_shell = film_shell
        self.len = len(film_shell)
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.len:
            raise StopIteration
        else:
            self.counter += 1
            return self.film_shell[self.counter]
