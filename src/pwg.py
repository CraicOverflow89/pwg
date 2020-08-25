from random import randrange
from uuid import uuid4

print("".join([
	chr(randrange(97, 123)),
	str(randrange(10)),
	chr([33, 35, 36, 37, 38][randrange(5)]),
	str(uuid4()).replace("-", "").upper()[-12:]
]))