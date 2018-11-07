""" ECIES.py
    A python commend line program that encrypts and decrypts files based on public key cryptography.
    
    When run from the commandline it will encrypt the file called "test.txt", and then decrypt this file.
    
    References:
      HAC - "Handbook of Applied Cryptography",Menezes, van Oorschot, Vanstone; 1996
      https://pypi.org/project/pycrypto/
      https://github.com/CryptoUSF/Course-Material/blob/master/code/cipher.py
"""
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

def genKey():
	"""randomly generate public key. 
    """
    generator = Random.new().read
    key = RSA.generate(1024, generator)

    publickey = key.publickey()
    privateKey = key

    return publickey, privateKey

def encrypt(publickey):
	"""encrypt the given file.
    """
    f = open ('test.txt', 'r')
    files = open('file.txt', 'w')
    
    line = f.read()

    encrypted = publickey.encrypt(line.encode('utf-8'), 32)
    
    files.write(str(encrypted))
    files.close()
    f.close()

    return encrypted

def decrypt(encrypted, privateKey):
	"""decrypt the given file.
    """
    files = open('file.txt', 'w')
    files.write(str(encrypted))
    files.close()


    anotherfile = open('file.txt', 'r')
    afterline = open('decryptfile.txt', 'w')

    after = privateKey.decrypt(encrypted)

    afterline.write(str(after))

    anotherfile.close()
    afterline.close()

def main():
    public, private = genKey()
    encryptedtext = encrypt(public)
    decrypt(encryptedtext, private)


if __name__ == '__main__':
    main()
