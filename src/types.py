from pathlib import Path
from typing import NamedTuple, List, Optional, Union
from urllib.parse import urlparse

__all__ = ['Image', 'Archive', 'Chapter', 'Meta', 'LocalImage']


class Image(NamedTuple):
    idx: int  # sequent image index
    url: str  # image url
    extension: Optional[str]  # preferred extension
    alternative_urls: Optional[List[str]]  # alternative urls
    name_format: str = '{idx:>03}-{name}.{extension}'
    type: Optional[str] = None  # image type

    def __str__(self) -> str:
        name = urlparse(self.url).path
        return self.name_format.format(
            idx=self.idx,
            url=self.url,
            extension=self.extension or 'png',
            name=name,
        )


class LocalImage(NamedTuple):
    image: Image

    def path(self, base_path: Path) -> Path:
        return base_path.resolve().joinpath(self.image.__str__())


class Archive(NamedTuple):  # for some sites
    idx: int  # sequent archive index
    url: str  # archive url
    name: str  # archive name
    date: Optional[str]  # chapter publication date
    name_format: str = 'arc_{idx:>03}-{name}'

    def __str__(self):
        # chapter human-friendly name
        return self.name_format.format(
            idx=self.idx,
            url=self.url,
            name=self.name,
            date=self.date,
        )


class Chapter(NamedTuple):
    """
    Example: Chapter(vol='4', ch='104', name='Tamatan, The Spirit', url='https://bato.to/chapter/1381023')
    """
    vol: str  # sequent chapter index
    ch: str  # sequent chapter index
    url: str  # chapter url
    name: str  # chapter human-friendly name
    date: Optional[str] = None  # chapter publication date
    name_format: str = 'vol_{vol:>03}_ch_{ch:>03}-{name}'

    def __str__(self):
        # chapter human-friendly name
        return self.name_format.format(
            vol=self.vol,
            ch=self.ch,
            url=self.url,
            name=self.name,
            date=self.date,
        )


class Meta(NamedTuple):
    url: str  # manga url
    author: str  # author (Translated variant)
    author_original: str  # author (Original variant)
    title: str  # title (Translated variant)
    title_original: str  # title (Original variant)
    annotation: str
    keywords: List[str]
    cover: Union[str, bytes]  # manga cover url OR bytes
    rating: float  # manga rating (<int> / 10)
