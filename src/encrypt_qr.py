from generate_qr import make_qr_and_save
from rsa_module import encrypt as en
from rsa_module import generate_keys
import os

def encrypt(message, filename, password, size=3):
	generate_keys(password)
	keys_directory=os.path.dirname(os.path.abspath(__file__))+'/Keys/'
	public_key_path = keys_directory + '/rsa_public_key.pem'
	
	if(os.path.exists(public_key_path)):
		encrypted_message = en(message)
		print('\n')
		print('Encrypted message: \n')
		print(encrypted_message)
		make_qr_and_save(encrypted_message, filename, size)
	else:
		print('No Public key available. Generate Public key and Priavte key first.')
		return None

def main():
	encrypt('Buzz off!','my-qr','My secret')

if __name__=='__main__': main()