import pyautogui
import time
#project code dala3
#zone where take to screenshot to detect the cactus  
detectionZone = (530,150, 20, 200) 

while True:
	s = pyautogui.screenshot(region=detectionZone)
	signature = sum(list( s.convert('1').getdata()))
	if signature < 960940 :
		print('jump')
		print(signature)
		pyautogui.keyDown("space")
		time.sleep(0.3)
		pyautogui.keyUp("space")