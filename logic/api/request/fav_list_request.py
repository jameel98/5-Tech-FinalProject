from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIFavList:
    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider.load_from_file('../../../config.json')
        self.api_fav = ConfigProvider.load_from_file('../../../config/favorite.json')
        self.api_url = ConfigProvider.load_from_file('../../../config/api_urls.json')

    def add_item_to_fav_list(self):
        return self._request.post_request(self.api_url["add_to_favorite"],
                                        self.api_fav["favorite_headers"],
                                        self.api_fav["favorite_payload"])
