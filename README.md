# Encrypted QR Code

Use this package to encrypt messages and embed in QR code, and decode the message back.

#### Build for Linux and OSX:
[![Build Status](https://travis-ci.org/somdipdey/Scrapping_And_Crawling_FinancialNews.svg?branch=master)](https://travis-ci.org/somdipdey/Scrapping_And_Crawling_FinancialNews_For_Keywords)
[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/somdipdey/Scrapping_And_Crawling_FinancialNews_For_Keywords/blob/master/LICENSE)

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

	git clone https://github.com/somdipdey/Encrypted_QR_Code.git
	cd Encrypted_QR_Code
	[sudo] python setup.py install

Run the encrypt_qr.py to create your qr code with encrypted message.
Run the decrypt_qr.py to decrypt the message from the qr code.

# **Work in progress