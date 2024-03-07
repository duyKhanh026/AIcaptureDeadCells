import numpy as np
import cv2
from mss import mss
from PIL import Image
import os
import torch
from pynput.keyboard import Key,Controller
import time

from readingMap import searchMap

keyboard = Controller()

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)

sct = mss()
countd = 300
countSearch = 30
charPress = ''
charPressStr = ''
charlenght = 0
charCount = 0
while countd > 0:
	w, h = 1300, 700
	monitor = {'top': 30, 'left': 20, 'width': w, 'height': h}
	img = Image.frombytes('RGB', (w, h), sct.grab(monitor).rgb)
	screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
	# set the model use the screen
	result = model(screen)

	new_width = int(w/2)
	new_height = int(h/2)
	for i in range(len(result.xyxy[0])):
		if (result.xyxy[0][i][5] == 0):
			print("x:" + str(result.xyxy[0][i][0].numpy()) + ", y:" + str(result.xyxy[0][i][1].numpy()) + 'time: ' + str(countd))
		#elif (result.xyxy[0][i][5] == 1):
	


	if charPress != '':
		keyboard.release(charPress)
		charPress = ''
		print(str(charCount) + ' ' + str(charlenght) + ' ' + charPress)
		
	if charCount < charlenght:
		charPress = charPressStr[charCount]
		if charPress == 's':
			keyboard.press(charPress)
			time.sleep(0.1)
			keyboard.press(' ')
			time.sleep(0.1)
			keyboard.release(' ')
			keyboard.release(charPress)
		else:
			keyboard.press(charPress)
		charCount += 1
		if charCount == charlenght:
			charCount = 0
			charlenght = 0
	#else :
		#charPress = '1'
		#keyboard.press(charPress)
	if countSearch <= 0:
		if charPress != '':
			keyboard.release(charPress)
		charPress = Key.tab
		keyboard.press(charPress)
		time.sleep(0.1)
		keyboard.release(charPress)
		time.sleep(0.05)
		charPress = 'o'
		keyboard.press(charPress)
		countSearch = 50
		charPressStr = searchMap()
		print(charPressStr)
		charPress = Key.tab
		keyboard.press(charPress) 
		charlenght = len(charPressStr)

	

	img_half = cv2.resize(result.render()[0], (new_width, new_height))

	cv2.imshow('Screen', img_half)


	if cv2.waitKey(1) == 27:
		#cv2.destroyAllWindows()
		break

	time.sleep(0.01)
	countd -= 1
	if countd <= 0 and charPress != '':
		keyboard.release(charPress)
		charPress = ''
	countSearch -= 1