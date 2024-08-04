from logic.api.response.fav_list_response import FavListData, FavList


class Product:
    def __init__(self, action: str, add: int, remove: int, switch: int):
        self.action = action
        self.data = FavListData(add=add, remove=remove, switch=switch)

    @classmethod
    def from_fav_list(cls, favlist: FavList) -> 'Product':
        return cls(
            action=favlist['action'],
            add=favlist['data']['add'],
            remove=favlist['data']['remove'],
            switch=favlist['data']['switch']
        )

    def to_dict(self) -> FavList:
        return {
            'action': self.action,
            'data': {
                'add': self.data['add'],
                'remove': self.data['remove'],
                'switch': self.data['switch']
            }
        }

    def __repr__(self):
        return f"Product(action={self.action}, add={self.data['add']}, remove={self.data['remove']}, switch={self.data['switch']})"
