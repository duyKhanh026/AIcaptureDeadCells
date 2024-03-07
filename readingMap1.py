import cv2 as cv
import numpy as np
import cv2
from mss import mss
from PIL import Image
import os

# PyTorch Hub
import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='bestRM.pt', force_reload=True)

sct = mss()

while 1:
	w, h = 620, 400
	monitor = {'top': 180, 'left': 320, 'width': w, 'height': h}
	img = Image.frombytes('RGB', (w, h), sct.grab(monitor).rgb)
	screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
	# set the model use the screen
	result = model(screen)

	for i in range(len(result.xyxy[0])):
		if (result.xyxy[0][i][5] == 0):
			print("x:" + str(result.xyxy[0][i][0].numpy()) + ", y:" + str(result.xyxy[0][i][1].numpy()))
		#elif (result.xyxy[0][i][5] == 1):

	cv2.imshow('Screen', result.render()[0])


	if cv2.waitKey(1) == 27:
		cv2.destroyAllWindows()
		break