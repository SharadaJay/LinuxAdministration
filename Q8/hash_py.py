import sys
import hashlib
import string
import secrets

def getSaltAsString(length=32):
    alpha = string.ascii_letters + string.digits
    salt = ''.join(secrets.choice(alpha) for _ in range (length))
    return salt

def getHash(password,salt):
    hashVal = hashlib.sha512((salt+password).encode())
    return hashVal.hexdigest()

password = str(sys.argv[1])
salt = getSaltAsString()
hash = getHash(password,salt)
print(hash)
