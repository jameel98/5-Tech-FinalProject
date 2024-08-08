import json


class ConfigProvider:

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty library.")

    @staticmethod
    def save_cookies(cookies):
        try:
            with open('../config/cookies.json', 'w') as file:
                json.dump(cookies, file)
        except FileNotFoundError:
            print(f"File cookies.json not found. Starting with an empty library.")
