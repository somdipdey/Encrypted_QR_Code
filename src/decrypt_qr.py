from qrtools import qrtools
from PIL import Image
import zbarlight
import os
from rsa_module import decrypt as de

def decrypt(file_name, password):
	keys_directory=os.path.dirname(os.path.abspath(__file__))+'/Keys/'
	private_key_path = keys_directory + '/rsa_private_key.pem'

	if(os.path.exists(private_key_path)):
		output_directory=os.path.dirname(os.path.abspath(__file__))+'/Output/'
		file_path = output_directory + file_name + '.PNG'
		with open(file_path, 'rb') as image_file:
		    image = Image.open(image_file)
		    image.load()
		codes = zbarlight.scan_codes('qrcode', image)
		print(codes)
		print('\n\n')
		decoded_result=codes
		print(decoded_result)
		return de(decoded_result, password)
	else:
		print('No Public key available. Generate Public key and Priavte key first.')
		return None

def command_line_exec():
	import sys

	if(len(sys.argv) < 3):
		print('Please provide QR code filename & password to decrypt the message\n')
		sys.exit(1)
	filename_arg = sys.argv[1]
	password_arg = sys.argv[2]
	encrypt(filename_arg, password_arg)


def main():
	print(decrypt('my-qr','My secret'))

if __name__=='__main__': command_line_exec()