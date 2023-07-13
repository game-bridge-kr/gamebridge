from dataclasses import dataclass, field
from urllib.parse import urlunparse


@dataclass
class UrlComponents:
    path: str
    query: str = ""
    scheme: str = "https"
    netloc: str = field(init=False)

    def __iter__(self):
        return (i for i in (self.scheme, self.netloc, self.path, '', self.query, ''))

    def to_url(self) -> str:
        return urlunparse(self)