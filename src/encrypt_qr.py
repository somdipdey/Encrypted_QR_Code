from generate_qr import make_qr_and_save
from simplecrypt import encrypt as en
import os
import sys
from binascii import hexlify


def encrypt(message, filename, password, size=3):
	# Encrypt the passed message using Simple-crypt	
	try:
		encrypted_message = en(password, message)
		print('\n')
		print('Encrypted message in hex: \n')
		hexed_encrypted_meesage = hexlify(encrypted_message)
		print(hexed_encrypted_meesage)
		# Embed the encrypted message in the QR code with aforementioned filename
		# The QR code is generated in the /Output/ folder
		make_qr_and_save(hexed_encrypted_meesage, filename, size)
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

if __name__=='__main__': command_line_exec()