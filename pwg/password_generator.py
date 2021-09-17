from functools import reduce
from random import randrange
from uuid import uuid4

class PasswordGenerator:
    @staticmethod
    def create():
        def insertCharAt(string, character, position):
            return string[:position] + character + string[position:]

        return reduce(
            lambda v, it: insertCharAt(v, it, randrange(len(v))),
            [
                chr(randrange(97, 123)),
                str(randrange(10)),
                chr([33, 35, 36, 37, 38][randrange(5)]),
            ],
            str(uuid4()).replace("-", "").upper()[-12:],
        )
