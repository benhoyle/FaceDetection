from SimpleCV import Camera, Display, HaarCascade
from datetime import datetime
import time

cam = Camera()
face_cascade = HaarCascade("/home/pi/Code/SimpleCV/SimpleCV/Features/HaarCascades/face.xml")


#disp = Display([320,240])
while True:
	img = cam.getImage()
	#img.resize(320,240)
	# Look for a face
	faces = img.findHaarFeatures(face_cascade)
	if faces.count() > 0:
		print "Found a face!\N"
		# Get the largest face
		faces = faces.sortArea()
		bigFace = faces[-1]
		# Draw a green box around the face
		bigFaceImg = bigFace.crop()
		
		bigFaceImg.save("/home/pi/Faces/"+str(datetime.now())+".jpeg")
		time.sleep(30)
