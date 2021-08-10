import sys
import hashlib
import string
import secrets

def getSalt(length=32):
    alpha = string.ascii_letters + string.digits
    salt = bytes(''.join(secrets.choice(alpha) for _ in range (length)),'utf-8')
    return salt

def getHash(password,salt):
    hashVal = hashlib.pbkdf2_hmac(hash_name='sha512',password=password, salt=salt,iterations=200000)
    return hashVal.hex()

password = bytes(str(sys.argv[1]),'utf-8')
salt = getSalt()
hash = getHash(password,salt)
print(hash)
