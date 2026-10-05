from typing import Iterable, Literal, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime

__all__ = ["SortBy", "SearchIn", "Exclude", "Domain",
           "DateFromTo", "Lang", "Country", "Sources",
           "Category", "Query", "ApiKey", "Size", "Page"]

# Right now mypy will extract the types from these declarations so I'm doing this instead of traditional type aliasing.

type SortBy = Iterable[Literal["relevancy", "popularity", "publishedAt"]]
type SearchIn = Iterable[Literal["title", "description", "content"]]
type Exclude = Iterable[Any]
type Domain = Iterable[Any]
type DateFromTo = datetime
type Lang = Literal["ar","de","en","es","fr","he","it","nl","no","pt","ru","sv","ud","zh"]
type Country = str
type Sources = str
type Category = str
type Query = str
type ApiKey = str
type Size = int
type Page = int
