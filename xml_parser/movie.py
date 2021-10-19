from __future__ import annotations
from typing import List
from xml.etree import ElementTree

class Movie:
    def __init__(
        self,
        title: str,
        year: str
    ):
        self.title = title
        self.year = year

    @classmethod
    def from_xml(cls, source: str) -> List[Movie]:
        tree = ElementTree.parse(source)
        collection = tree.getroot()
        movies = []

        for category in collection:
            for decade in category:
                for movie in decade:
                    for child in movie.findall("year"):
                        movies.append(
                            cls(movie.attrib["title"],
                                child.text)
                        )
        return movies


if __name__ == '__main__':
    movies = Movie.from_xml("market.xml")
    print(movies)
