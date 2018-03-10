# Make qr code and return as image.pil.pilimage
def make_qr(data, size=2):
	import qrcode
	import datetime
	import os
	
	qr = qrcode.QRCode(
	    version=size,
	    error_correction=qrcode.constants.ERROR_CORRECT_H,
	    box_size=10,
	    border=2,
	)
	qr.add_data(data)
	qr.make(fit=True)

	img = qr.make_image()
	return img


# Make qr code and save it in /Output/
def make_qr_and_save(data, filename, size=2):
	import qrcode
	import os
	import string
	from PIL import Image
	
	qr = qrcode.QRCode(
	    version=size,
	    error_correction=qrcode.constants.ERROR_CORRECT_H,
	    box_size=10,
	    border=2,
	)
	qr.add_data(data)
	qr.make(fit=True)
	print('::\n')
	print(data)
	img = qr.make_image()

	filename = filename.replace('/', '_')
	filename = filename.replace(' ', '_')
	filename = filename.replace('.', '_')
	filename = filename + '.PNG'

	# Check if directory exists or not
	# Then save the image accordingly
	output_directory=os.path.dirname(os.path.abspath(__file__))+'/Output/'
	if(os.path.exists(output_directory)):
		img.save(output_directory+filename)
		resized = Image.open(output_directory+filename)
		resized = resized.resize((560,560),Image.ANTIALIAS)
		os.remove(output_directory+filename)
		resized.save(output_directory+filename,quality=100)
	else:
		os.mkdir(output_directory)
		img.save(output_directory+filename)

# Make qr code and save it ina specific directory with specific filename
def make_qr_and_save_with_filename(data, size=2, directory_name='bin', filename='output'):
	import qrcode
	import datetime
	import os
	
	qr = qrcode.QRCode(
	    version=size,
	    error_correction=qrcode.constants.ERROR_CORRECT_H,
	    box_size=10,
	    border=2,
	)
	qr.add_data(data)
	qr.make(fit=True)

	img = qr.make_image()

	# Check if directory exists or not
	# Then save the image accordingly
	output_directory=os.path.dirname(os.path.abspath(__file__))+ '/' + directory_name + '/'
	if(os.path.exists(output_directory)):
		img.save(output_directory+filename)
	else:
		os.mkdir(output_directory)
		img.save(output_directory+filename)

def main():
	make_qr_and_save('I will write bullshit here!', 'my-file', 3)

if __name__=='__main__': main()