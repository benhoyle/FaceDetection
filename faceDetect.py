from SimpleCV import Camera, Display

cam = Camera()

disp = Display(cam.getImage().size())
while disp.isNotDone():
	img = cam.getImage()
	# Look for a face
	faces = img.findHaarFeatures('face')
	if faces is not None:
		# Get the largest face
		faces = faces.sortArea()
		bigFace = faces[-1]
		# Draw a green box around the face
		bigFace.draw()
	img.save(disp)
