#Use the IDLE. Each line is a prompt in python.
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")
f.decrypt(token)
'my deep dark secret'

#To see the encrypted message. type the following:
token
'gAAAAABXF6mwHdjig_kRIhbrq16IgG6stjfoXZgJMW5ndwu7riTf7ruW61PpF1rBtWuUKPTpHKL-SvXGbwKPz2znd2AXgX0s8lGBnfjZa9imT0M_FPtyOKE='
