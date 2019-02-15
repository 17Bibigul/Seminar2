# -*- coding: utf-8 -*-


class Film(object):
    min_recommended_duration = 10  # class attribute #1
    max_recommended_duration = 60  # class attribute #1

    def __init__(self, name: str, duration: int, country: str):
        """
        The constructor method to initialize the attributes of the class
        Args:
            name: film name
            duration: film duration in minutes
            country: producing country
        """
        self.name = name
        self.duration = duration
        self.country = country

    def change_max_recommended_duration(self, max_recommended_duration):
        """
        Inner methods for change variables
        Returns:

        """
        self.max_recommended_duration = max_recommended_duration


class FilmShell(object):
    def __init__(self):
        self.contained_film = []

    def add(self, film: object):
        self.contained_film.append(film)

    def len(self):
        return len(self.contained_film)

    def remove(self, film: object):
        self.contained_film.remove(film)

    def contains(self, film: object):
        return film in self.contained_film

    def iterator(self, film):
        return self.contained_film.count(film)

