import pygame
import pygame.camera as camera
import time
import pygame.image as im
from PIL import Image
from itertools import izip
import os
import argparse

camera.init()
cam = camera.Camera(camera.list_cameras()[0],(640,480))
cam.start()
size = cam.get_size()

	def check_images(i1,i2,n,t,d):
		i1 = im.tostring(i1,"RGB")
		i1 = Image.frombytes("RGB",(600,480),i1)
		

		i2 = im.tostring(i2,"RGB")
		i2 = Image.frombytes("RGB",(600,480),i2)
		
		pairs = izip(i1.getdata(), i2.getdata())
		if len(i1.getbands()) == 1:
			dif = sum(abs(p1 - p2) for p1,p2 in pairs)
		else:
			dif = sum(abs(c1 - c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

		ncomponents = i1.size[0] * i1.size[1] * 3

		return (dif / 255.0 * 100) / ncomponents

		while 1:
			i1 = cam.get_image()
			time.sleep(1)
			i2 = cam.get_image()
			dif = check_images(i1,i2)

			if dif > 2.5:
				for x in range(0,n):
					timestamp = time.strftime("%Y-%m-%d--%H:%M:%S")
					
					im.save(cam.get_image(), d+timestamp + ".jpg")
					time.sleep(0.5)
		
		time.sleep(1)
	def main(self):
		parser = argparse.ArgumentParser(usage="-h for full usage")
	    parser.add_argument('-n', dest="Number of images", help='Number of Images',required=True)
	    parser.add_argument('-d', dest="destdir", help='Destination Directory',required=True)
	    parser.add_argument('-s', dest="", help='email subject',required=True)
	    args = parser.parse_args()