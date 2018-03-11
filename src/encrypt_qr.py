from generate_qr import make_qr_and_save
from simplecrypt import encrypt as en
import os
import sys


def encrypt(message, filename, password, size=3):
	
	try:
		encrypted_message = en(password, message)
		print('\n')
		print('Encrypted message: \n')
		print(encrypted_message)
		make_qr_and_save([encrypted_message], filename, size)
		print('Successfully created encrypted QR code: ' + filename + '.PNG')
	except:
		print('Error in creating encrypted QR code')
		sys.exit(1)

def command_line_exec():
	import sys

	if(len(sys.argv) < 4):
		print('Please provide Message to be encrypted, filename & password\n')
		sys.exit(1)
	message_arg = sys.argv[1]
	filename_arg = sys.argv[2]
	password_arg = sys.argv[3]
	encrypt(message_arg, filename_arg, password_arg)

def main():
	encrypt('Buzz off!','my-qr','My secret')

if __name__=='__main__': command_line_exec()