from SimpleCV import Camera, Display

cam = Camera()

disp = Display([320,240])
while disp.isNotDone():
	img = cam.getImage()
	img.resize(320,240)
	# Look for a face
	faces = img.findHaarFeatures('face')
	if faces is not None:
		# Get the largest face
		faces = faces.sortArea()
		bigFace = faces[-1]
		# Draw a green box around the face
		bigFaceImg = bigFace.crop()
		
		
		#pos - an (x,y) position tuple of the top left corner of img on this image. 
		img = img.blit(bigFaceImg.rotate(180), pos=bigFace.topLeftCorner())
		
	img.save(disp)
