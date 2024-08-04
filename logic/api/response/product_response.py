from typing import TypedDict


class FavListData(TypedDict):
    add: int
    remove: int
    switch: int


class FavList(TypedDict):
    action: str
    data: FavListData
