import cv2 as cv
import numpy as np
import cv2
from mss import mss
from PIL import Image
import os

# PyTorch Hub
import torch

# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt', force_reload=True)
model1 = torch.hub.load('ultralytics/yolov5', 'custom', path='bestRM.pt', force_reload=True)

sct = mss()


w, h = 1300, 700
monitor = {'top': 30, 'left': 20, 'width': w, 'height': h}
img = Image.open("E1_fs (367).png")
screen = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
# set the model use the screen
result = model(screen)
result1 = model1(screen)

print(result.xyxy[0][0][1])
print(result.xyxy[0][0][1].numpy())
if (result.xyxy[0][0][1].numpy() > 300):
	print("thỏa dk")
#img_half = cv2.resize(result.render()[0], (new_width, new_height))

cv2.imshow('Screen', result1.render()[0])
cv2.waitKey(0)