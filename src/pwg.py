from random import randrange
from uuid import uuid4

print(f"j{str(randrange(10))}#" + str(uuid4()).replace("-", "").upper()[:12])