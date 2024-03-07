from pynput.keyboard import Key,Controller
import time

keyboard = Controller()

time.sleep(10)
char = "ddddddddd"

keyboard.press(Key.tab)
time.sleep(0.1)
keyboard.release(Key.tab )
for i in range(len(char)):
	keyboard.press(char[i])
	time.sleep(0.1)
	keyboard.release(char[i])
