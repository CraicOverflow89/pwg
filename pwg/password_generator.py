from functools import reduce
from random import randrange
from uuid import uuid4


class PasswordGenerator:
    @staticmethod
    def create() -> str:
        """
        Creates a random password
        :return: string of fifteen characters
        """

        def insertCharAt(string: str, character: str, position: int) -> str:
            """
            Inserts a character at a position into a specific string
            :param string: the string to insert a character into
            :param character: the string to insert
            :param position: the position at which to insert the character into the string
            :return: new string with inserted character
            """
            return string[:position] + character + string[position:]

        return reduce(
            lambda v, it: insertCharAt(v, it, randrange(len(v))),
            [
                chr(randrange(97, 123)),
                chr(randrange(65, 91)),
                str(randrange(10)),
                chr([33, 35, 36, 37, 38][randrange(5)]),
            ],
            str(uuid4()).replace("-", "").upper()[-11:],
        )
