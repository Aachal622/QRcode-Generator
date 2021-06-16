import qrcode		//library that you have to import for qrcode generator

features = qrcode.QRCode(version=1,box_size=10,border=3)	//size of qrcode box,border and version

features.add_data('https://github.com/Aachal622/aachal_ml')	//provide link or string data for qrcode genration
features.make(fit=True)
generate_image = features.make_image(fill_color="black",back_color="white")	//color provided
generate_image.save('image.png')		//that image holds your link or string data as qrcode