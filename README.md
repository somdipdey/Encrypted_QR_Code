# Encrypted QR Code

Use this package to encrypt messages and embed in QR code, and decode the message back.

#### Build for Linux and OSX:
[![Build Status](https://travis-ci.org/somdipdey/Encrypted_QR_Code.svg?branch=master)](https://travis-ci.org/somdipdey/Encrypted_QR_Code)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/somdipdey/Encrypted_QR_Code/blob/master/LICENSE)

## Dependencies

	$[sudo] pip install qrcode
	$[sudo] pip install pycryptodome
	$[sudo] pip install pypng
	$[sudo] pip install zbar
	$[sudo] pip install pillow

### Note:

If you are using Python3.X and not Python2 then you would receive an error while installing zbar. In that case install pypng and pillow packages and then for zbar follow these steps:

	$ brew install zbar
	$ export LDFLAGS="-L$(brew --prefix zbar)/lib"
	$ export CFLAGS="-I$(brew --prefix zbar)/include"
	$ pip install zbarlight

The aformentioned steps would install zbarlight. For more information consult their webpage: https://github.com/Polyconseil/zbarlight 

## Installation

	$git clone https://github.com/somdipdey/Encrypted_QR_Code.git
	$cd Encrypted_QR_Code
	$[sudo] python setup.py install

## Usage

### Encryption

To encrypt a meesage and then embed it in the QR code just type the following command in the command prompt:

	$python encrypt_qr.py {message} {qr_file_name} {password}

For example::

	$python encrypt_qr.py 'my hobby is everything' hello 'My Secret'

If you use the following command, you will see a QR code with name 'hello.PNG' is generated in the /Output/ folder. Upon inspection, you can see the QR code holds the encrypted message, i.e. 'my hobby is everything'.

#### hello.PNG QR code with embedded encrypted meesage::

<img width="350" alt="hello.PNG QR code with embedded encrypted meesage" src="https://github.com/somdipdey/Encrypted_QR_Code/blob/master/src/Output/hello.PNG">

### Decryption

To decrypt the message from the QR code just type the following command in the command prompt:

	$python decrypt_qr.py {qr_file_name} {password}

For example::

	$python decrypt_qr.py hello 'My Secret'


# **Work in progress

The decryption part is still being worked on and is not ready yet.