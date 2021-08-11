import re
from hashlib import blake2b
import time

def checkName(name: str):
    name_pattern = re.compile(r"(^[A-Z])([a-zA-Z]+)")
    if name_pattern.match(name) is None:
        return False
    else:
        return True

def makeSeed(name: str, age: int) -> str:
    h = blake2b(key=b'2021 decipher')
    key_ = name + str(age)
    h.update(key_.encode())
    return h.hexdigest()

def makeUniqueID(name:str, age: int, seed: str) -> str:
    if makeSeed(name, age) != seed:
        return "Your seed is wrong"
    suffix = f'_{round(time.time())}'
    h = blake2b(key=b'2021 decipher', digest_size=8)
    key_ = name + str(age) + seed
    h.update(key_.encode())
    res = h.hexdigest() + suffix
    return res


