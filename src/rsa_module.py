from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os

def generate_keys(secret_code):
	key = RSA.generate(2048)
	encrypted_key = key.exportKey(passphrase=secret_code, pkcs=8,
	                              protection="scryptAndAES128-CBC")

	output_directory=os.path.dirname(os.path.abspath(__file__))+'/Keys/'
	if(os.path.exists(output_directory)):
		# Save encrypted private key
		file_out = open(output_directory + "/rsa_private_key.pem", "wb")
		file_out.write(encrypted_key)
		# Save public key
		file_out = open(output_directory + "/rsa_public_key.pem", "wb")
		file_out.write(key.publickey().exportKey())
	else:
		os.mkdir(output_directory)
		# Save encrypted private key
		file_out = open(output_directory + "/rsa_private_key.pem", "wb")
		file_out.write(encrypted_key)
		# Save public key
		file_out = open(output_directory + "/rsa_public_key.pem", "wb")
		file_out.write(key.publickey().exportKey())

def encrypt_file(message):
	output_directory=os.path.dirname(os.path.abspath(__file__))+'/Keys/'
	with open('encrypted_data.txt', 'wb') as out_file:
		recipient_key = RSA.import_key(
		open(output_directory + '/rsa_public_key.pem').read())
		session_key = get_random_bytes(16)
		cipher_rsa = PKCS1_OAEP.new(recipient_key)
		out_file.write(cipher_rsa.encrypt(session_key))
		cipher_aes = AES.new(session_key, AES.MODE_EAX)
		encoded = message.encode("latin-1")
		data = encoded
		ciphertext, tag = cipher_aes.encrypt_and_digest(data)
		out_file.write(cipher_aes.nonce)
		out_file.write(tag)
		out_file.write(ciphertext)
	with open('encrypted_data.txt', 'rb') as fobj:
		print(fobj.read())

def encrypt(message):
	output_directory=os.path.dirname(os.path.abspath(__file__))+'/Keys/'

	with open('encrypted_data.txt', 'wb') as out_file:
		recipient_key = RSA.import_key(
		open(output_directory + '/rsa_public_key.pem').read())
		session_key = get_random_bytes(16)
		cipher_rsa = PKCS1_OAEP.new(recipient_key)
		out_file.write(cipher_rsa.encrypt(session_key))

		cipher_aes = AES.new(session_key, AES.MODE_EAX)
		encoded = message.encode("latin-1")
		data = encoded
		ciphertext, tag = cipher_aes.encrypt_and_digest(data)
		out_file.write(cipher_aes.nonce)

		out_file.write(tag)

		out_file.write(ciphertext)

	with open('encrypted_data.txt', 'rb') as fobj:
		output = [l for l in fobj.readlines()]
	os.remove('encrypted_data.txt')
	return output

def decrypt_file(secret_code):
	code = secret_code
	output_directory=os.path.dirname(os.path.abspath(__file__))+'/Keys/'
	with open('encrypted_data.txt', 'rb') as fobj:
		private_key = RSA.import_key(
		open(output_directory + '/rsa_private_key.pem').read(),
		passphrase=code)
		enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
		for x in (private_key.size_in_bytes(), 
		16, 16, -1) ]
		cipher_rsa = PKCS1_OAEP.new(private_key)
		session_key = cipher_rsa.decrypt(enc_session_key)
		cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
		data = cipher_aes.decrypt_and_verify(ciphertext, tag)
	return data.decode("utf-8")

def decrypt(encrypted_message, secret_code):
	code = secret_code
	output_directory=os.path.dirname(os.path.abspath(__file__))+'/Keys/'

	with open('encrypted_data.txt', 'wb') as temp_file:
		for item in (encrypted_message):
			temp_file.write(item)
	with open('encrypted_data.txt', 'rb') as fobj:
		private_key = RSA.import_key(
		open(output_directory + '/rsa_private_key.pem').read(),
		passphrase=code)
		enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
		for x in (private_key.size_in_bytes(), 
		16, 16, -1) ]
		cipher_rsa = PKCS1_OAEP.new(private_key)
		session_key = cipher_rsa.decrypt(enc_session_key)
		cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
		data = cipher_aes.decrypt_and_verify(ciphertext, tag)

	os.remove('encrypted_data.txt')
	return data.decode('utf8')

def decrypt2(encrypted_message, secret_code):
	code = secret_code
	output_directory=os.path.dirname(os.path.abspath(__file__))+'/Keys/'

	with open('encrypted_data.txt', 'wb') as temp_file:
		for item in (encrypted_message):
			temp_file.write(item)
	with open('encrypted_data.txt', 'rb') as fobj:
		private_key = RSA.import_key(
		open(output_directory + '/rsa_private_key.pem').read(),
		passphrase=code)
		enc_session_key, nonce, tag, ciphertext = [ fobj.read(x) 
		for x in (private_key.size_in_bytes(), 
		16, 16, -1) ]
		cipher_rsa = PKCS1_OAEP.new(private_key)
		session_key = cipher_rsa.decrypt(enc_session_key)
		cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
		data = cipher_aes.decrypt_and_verify(ciphertext, tag)

	os.remove('encrypted_data.txt')
	return data.decode('utf8')

def main():
	generate_keys('My secret')
	encrypted = encrypt('blah blah blah blo')
	#encrypt_file('blah blah blah blo')
	print('Encryption Complete!')
	print('Decrypting message now....')
	print(encrypted)
	print(decrypt(encrypted, 'My secret'))
	#decrypt_file('secret one')

if __name__=='__main__': main()