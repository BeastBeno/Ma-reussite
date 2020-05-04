import hashlib

def makehash(password):
     print(hashlib.sha256(str.encode(password)).hexdigest())

makehash("1234")