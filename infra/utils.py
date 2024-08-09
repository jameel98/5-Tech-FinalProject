import string
import random


class Utils:

    @staticmethod
    def generate_random_text(N):
        return ''.join(random.choices(string.ascii_uppercase, k=N))
