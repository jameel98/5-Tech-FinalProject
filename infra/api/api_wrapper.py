import logging
import os

import requests

from infra.api.response_wrapper import ResponseWrapper
from infra.config_provider import ConfigProvider


class APIWrapper:

    def __init__(self):
        self._request = None
        self._session = requests.Session()
        current_working_directory = os.getcwd()
        self.config = ConfigProvider.load_from_file(current_working_directory + '../../config/config.json')
        self.logger = logging.getLogger(__name__)  # Initialize logger for this class

    def get_request(self, url=None, header=None, body=None):
        """send api get request"""
        self.logger.info(f'send api get request.')
        result = requests.get(url, headers=header, json=body)
        return ResponseWrapper(ok=result.ok, status_code=result.status_code, data=result.json())

    def post_request(self, url=None, header=None, body=None):
        """send api post request"""
        self.logger.info(f'send api post request.')
        result = requests.post(url, headers=header, json=body)
        return ResponseWrapper(ok=result.ok, status_code=result.status_code, data=result.json())
