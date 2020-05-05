import hashlib

def makehash(password):
     return hashlib.sha256(str.encode(password)).hexdigest()



