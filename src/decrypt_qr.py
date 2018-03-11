from qrtools import qrtools
from PIL import Image
import zbarlight
import os
from simplecrypt import decrypt as de
import sys
from binascii import unhexlify

def decrypt(file_name, password):

	output_directory=os.path.dirname(os.path.abspath(__file__))+'/Output/'
	file_path = output_directory + file_name + '.PNG'
	with open(file_path, 'rb') as image_file:
	    image = Image.open(image_file)
	    image.load()
	codes = zbarlight.scan_codes('qrcode', image)

	decoded_result=codes[0].decode('utf-8')
	ciphertext = unhexlify(decoded_result)
	print('Decoded::')
	print(ciphertext)
	return de(password, ciphertext)

def command_line_exec():

	if(len(sys.argv) < 3):
		print('Please provide QR code filename & password to decrypt the message\n')
		sys.exit(1)
	filename_arg = sys.argv[1]
	password_arg = sys.argv[2]
	message = decrypt(filename_arg, password_arg)
	print(message.decode('utf-8'))


def main():
	print(decrypt('my-qr','My secret'))

if __name__=='__main__': command_line_exec()