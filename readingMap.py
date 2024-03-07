import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
from pynput.keyboard import Key, Controller
import time
import os

keyboard = Controller()
#keyboard.press(key)
#keyboard.release(key)

def pressKey(key):
	keyboard.press(key)
	time.sleep(0.1)
	keyboard.release(key)
	time.sleep(0.1)
def searchMap():

	keypressResult = ""

	needle_img = [None] * 8
	image2copy = [None] * 8
	grayscale2_image = [None] * 8
	needle_img[0] = cv2.imread('mappic/RmapValue (1).png', cv2.IMREAD_UNCHANGED)   #dáng đứng 1 phải
	image2copy[0] = np.uint8(needle_img[0]) 
	grayscale2_image[0]  = cv2.cvtColor(image2copy[0], cv2.COLOR_BGR2GRAY)
	###########
	needle_img[1] = cv2.imread('mappic/RmapValue (2).png', cv2.IMREAD_UNCHANGED)
	image2copy[1] = np.uint8(needle_img[1])
	grayscale2_image[1]  = cv2.cvtColor(image2copy[1], cv2.COLOR_BGR2GRAY)
	###########
	needle_img[2] = cv2.imread('mappic/RmapValue (3).png', cv2.IMREAD_UNCHANGED)
	image2copy[2] = np.uint8(needle_img[2])
	grayscale2_image[2]  = cv2.cvtColor(image2copy[2], cv2.COLOR_BGR2GRAY)
	###########
	needle_img[3] = cv2.imread('mappic/RmapValue (4).png', cv2.IMREAD_UNCHANGED)
	image2copy[3] = np.uint8(needle_img[3])
	grayscale2_image[3]  = cv2.cvtColor(image2copy[3], cv2.COLOR_BGR2GRAY)
	###########
	needle_img[4] = cv2.imread('mappic/RmapValue (1).png', cv2.IMREAD_UNCHANGED)     #dáng đứng 1 trái
	image2copy[4] = np.uint8(needle_img[4])
	grayscale2_image[4]  = cv2.cvtColor(image2copy[4], cv2.COLOR_BGR2GRAY)
	###########
	needle_img[5] = cv2.imread('mappic/RmapValue (1).png', cv2.IMREAD_UNCHANGED) #dáng đứng 2 phải
	image2copy[5] = np.uint8(needle_img[5])
	grayscale2_image[5]  = cv2.cvtColor(image2copy[5], cv2.COLOR_BGR2GRAY)
	###########
	needle_img[6] = cv2.imread('mappic/RmapValue (1).png', cv2.IMREAD_UNCHANGED)   #dáng đứng 2 trái
	image2copy[6] = np.uint8(needle_img[6])
	grayscale2_image[6]  = cv2.cvtColor(image2copy[6], cv2.COLOR_BGR2GRAY)
	###########
	needle_img[7] = cv2.imread('mappic/RmapValue (1).png', cv2.IMREAD_UNCHANGED) #dáng chạy phải  
	image2copy[7] = np.uint8(needle_img[7])
	grayscale2_image[7]  = cv2.cvtColor(image2copy[7], cv2.COLOR_BGR2GRAY)
	###########

	chrm = ''
	count = 0;
	vitri = [None] * 4
	find = False
	cap_arr = None
	while True:
		cap = ImageGrab.grab(bbox=(380,230, 880,600)) #500:370

		cap_arr = np.array(cap)
		image1copy = np.uint8(cap_arr)
		grayscale1_image  = cv2.cvtColor(image1copy, cv2.COLOR_BGR2GRAY)

		result = [None] * 8

		looop = 1

		for i in range(looop):
			result[i] = cv2.matchTemplate(grayscale1_image, grayscale2_image[i], cv2.TM_CCOEFF_NORMED)


		min_val = [None] * 8
		max_val = [None] * 8
		min_loc = [None] * 8 
		max_loc = [None] * 8
		for i in range(looop):
			min_val[i], max_val[i], min_loc[i], max_loc[i] = cv2.minMaxLoc(result[i])
			#print(result[i])

		#print('Best match top left position: %s' %  str(max_loc))
		#print('Best match confidence: %s' %  max_val)

		threshold = 0.7
		for i in range(looop):
			cv2.putText(cap_arr, str(max_val[i]), (50,50 + (35 * i)), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(0,255,0), thickness=2, lineType=cv2.LINE_4)
			if max_val[i] >= threshold:
				#print('Found needle.')

				needle_w = needle_img[i].shape[1]
				needle_h = needle_img[i].shape[0]

				top_left = max_loc[i]
				bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

				print( str(top_left[0]) +', ' + str(top_left[1]) + ', ' + str(needle_w) + ', ' + str(needle_h))
				cv2.rectangle(cap_arr, top_left, bottom_right,
					color=(0,255,0), thickness=1, lineType=cv2.LINE_4)
				derp = 'Post ' + str(i) +'.'
				#cv2.putText(cap_arr, derp, (top_left[0],top_left[1]-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color=(0,255,0), thickness=2, lineType=cv2.LINE_4)
				#print("post needle_img ", i ,'.')
				
				vitri[0] = needle_w
				vitri[1] = needle_h
				vitri[2] = bottom_right[0]
				vitri[3] = bottom_right[1]
				find = True;
				break;
				
			else:
				#print('Needle not found ' , count, '. ')
				count += 1
		# Detect points that form a line
		cv2.imshow('Result', cap_arr)
		if cv2.waitKey(1) == 27 or find == True:
			print("found the mc point")
			break
		time.sleep(0.1)
		if count >= 15 :
			if count % 2 == 0:
				print("Cant found 2")
				pressKey(Key.tab)
				pressKey('a')
				pressKey(Key.tab)
				pressKey('o')
			else: 
				print("Cant found 1")
				pressKey(Key.tab)
				pressKey('d')
				pressKey(Key.tab)
				pressKey('o')

	lineDraw = 0
	needle_img[0] = cv2.imread('mappic/Line.png', cv2.IMREAD_UNCHANGED)   #dáng đứng 1 phải
	image2copy[0] = np.uint8(needle_img[0]) 
	grayscale2_image[0]  = cv2.cvtColor(image2copy[0], cv2.COLOR_BGR2GRAY)
	###########
	needle_img[1] = cv2.imread('mappic/Line1.png', cv2.IMREAD_UNCHANGED)
	image2copy[1] = np.uint8(needle_img[1])
	grayscale2_image[1]  = cv2.cvtColor(image2copy[1], cv2.COLOR_BGR2GRAY)
	###########
	threshold = 0.45

	bandau = [None] * 4
	bandau = vitri
	vong = 12
	cantGo = 0

	while vong > 0:
		crop = [None] * 4
		crop[0] = cap_arr[vitri[3] - vitri[1]:vitri[3], vitri[2]:vitri[2] + 35]  
		crop[1] = cap_arr[vitri[3]:vitri[3] + 35, vitri[2] - vitri[0]:vitri[2]]  
		crop[2] = cap_arr[vitri[3] - vitri[1]:vitri[3], vitri[2] - 35 - vitri[0]:vitri[2] - vitri[0]] 
		crop[3] = cap_arr[vitri[3] - 55:vitri[3] - vitri[1], vitri[2] - vitri[0]:vitri[2]]  
		grayscale1_image = [None] * 4
		for i in range(4):	
			crop[i] = np.array(crop[i])
			image1copy = np.uint8(crop[i])
			grayscale1_image[i] = cv2.cvtColor(image1copy, cv2.COLOR_BGR2GRAY)
		result = [None] * 4
		result[0] = cv2.matchTemplate(grayscale1_image[0], grayscale2_image[0], cv2.TM_CCOEFF_NORMED)
		result[1] = cv2.matchTemplate(grayscale1_image[1], grayscale2_image[1], cv2.TM_CCOEFF_NORMED)
		result[2] = cv2.matchTemplate(grayscale1_image[2], grayscale2_image[0], cv2.TM_CCOEFF_NORMED)
		result[3] = cv2.matchTemplate(grayscale1_image[3], grayscale2_image[1], cv2.TM_CCOEFF_NORMED)
		
		min_val = [None] * 4
		max_val = [None] * 4
		min_loc = [None] * 4 
		max_loc = [None] * 4
		for i in range(4):
			min_val[i], max_val[i], min_loc[i], max_loc[i] = cv2.minMaxLoc(result[i])
			if max_val[i] < threshold:
				if i == 3 :
					cv2.line(cap_arr, (vitri[2],vitri[3] - vitri[1]), (vitri[2],vitri[3] - 55), (0, 255, 0), thickness=2)
					vitri[3] = vitri[3] - 55
					cv2.line(cap_arr, (vitri[2],vitri[3] - 3), (vitri[2],vitri[3]), (0, 255, 0), thickness=4)
					#print("go up")
					keypressResult += "ww"
				elif i == 1 :
					cv2.line(cap_arr, (vitri[2],vitri[3] - vitri[1] +6), (vitri[2],vitri[3] + 35 - vitri[1] ), (0, 255, 0), thickness=2)
					vitri[3] = vitri[3] + 35 - 6
					cv2.line(cap_arr, (vitri[2],vitri[3] - vitri[1]  + 6), (vitri[2],vitri[3] - vitri[1]), (0, 255, 0), thickness=4)
					#print("go down")
					keypressResult += "s"
				elif i == 0 :
					cv2.line(cap_arr, (vitri[2],vitri[3] - vitri[1] + 6), (vitri[2]  + 35,vitri[3] - vitri[1] + 6), (0, 255, 0), thickness=2)
					vitri[2] = vitri[2] + 35
					cv2.line(cap_arr, (vitri[2] - 4,vitri[3] - vitri[1] + 6), (vitri[2] - 2,vitri[3] - vitri[1] + 6), (0, 255, 0), thickness=4)
					#print("go right")
					keypressResult += "ddd"
				elif i == 2 :
					cv2.line(cap_arr, (vitri[2] - vitri[0],vitri[3] - vitri[1] + 6), (vitri[2] - 35,vitri[3] - vitri[1] + 6), (0, 255, 0), thickness=2)
					vitri[2] = vitri[2] - 35
					cv2.line(cap_arr, (vitri[2] + 4,vitri[3] - vitri[1] + 6), (vitri[2] + 2 ,vitri[3] - vitri[1] + 6), (0, 255, 0), thickness=4)
					#print("go left")
					keypressResult += "aaa"
				#else :
					#print("cant")
				break
		print('vong: ' + str(vong))
		if vitri[2] + 35 >= 500 or vitri[2] - 35 <= 0:
			break
		elif vitri[3] + 35 >= 370 or vitri[3] - 35 <= 0:
			break
		#cv2.imshow('Crop', crop[0])
		#cv2.imshow('Crop 1', crop[1])
		#cv2.imshow('Crop 2', crop[2])
		#cv2.imshow('Crop 3', crop[3])
		cv2.imshow('Result', cap_arr)
		
		if cv2.waitKey(1) == 27:
			break
		time.sleep(0.1)
		vong -= 1

	#cv2.destroyAllWindows()
	#cv2.waitKey(0)
	if keypressResult == '':
		keypressResult = 'aaa'
	return keypressResult


#print(searchMap())
