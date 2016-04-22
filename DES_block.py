Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # -*- coding: cp1252 -*-
#Let’s look at one of the block cipher: DES. The key size used by this
#cipher is 8 bytes and the block of data it works with is 8 bytes long.
#The simplest mode for this block cipher is the electronic code book mode
#where each block is
#encrypted independently to form the encrypted text.

#Source : http://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/
>>> from Crypto.Cipher import DES
>>> des = DES.new('01234567', DES.MODE_ECB)
>>> text = 'abcdefgh'
>>> cipher_text = des.encrypt(text)
>>> cipher_text
'\xec\xc2\x9e\xd9] a\xd0'
>>> des.decrypt(cipher_text)

'abcdefgh'
>>> 
