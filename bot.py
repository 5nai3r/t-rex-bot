import pyautogui
import time
from tkinter import *
import threading
#project code dala3
#zone where take to screenshot to detect the cactus  
detectionZone = (476,176, 20, 200) 
#enable variable for the loop
BotEnable = False 
exitLoop = False

def checkLoop():
	while not exitLoop:
		if BotEnable :
			s = pyautogui.screenshot(region=detectionZone)
			signature = sum(list( s.convert('1').getdata()))
			if signature < 960940 :
				print('jump')
				print(signature)
				pyautogui.keyDown("space")
				time.sleep(0.3)
				pyautogui.keyUp("space")
	return

x = threading.Thread(target=checkLoop)
x.start()
	
BotWindow = Tk()
BotWindow.wm_attributes('-alpha',0.2)

w = Canvas(BotWindow, width=200, height=250)
w.pack()
w.create_rectangle(50, 25, 20, 200, fill="blue")
def click():
    global detectionZone
    detectionZone = (BotWindow.winfo_x()+50, BotWindow.winfo_y()+25,20,200)

def toggleEnable():
    global BotEnable
    BotEnable = not BotEnable
    enbBtn['bg']="green" if BotEnable else "red"

def onClose():
	global exitLoop
	BotWindow.destroy()
	exitLoop = True
	
posBtn = Button(BotWindow,text="Update position", command=click)
enbBtn = Button(BotWindow, text='Toggle',command=toggleEnable)
posBtn.pack()
enbBtn.pack()

BotWindow.protocol("WM_DELETE_WINDOW", onClose)
BotWindow.mainloop()