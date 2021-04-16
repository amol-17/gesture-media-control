import handRecog as hr
import cv2
import time
import pyautogui as pag
import pystray
import sys
from PIL import Image
from pystray import Menu, MenuItem
import threading
from plyer import notification as nf

stop_code = 0

def main_code():
    cap = cv2.VideoCapture(0)
    pag.FAILSAFE = False
    
    detector = hr.handDetector(detectionConfi=0.9, maxHands=1, trackConfi=0.9)
    try:
        while True:
            s, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findHandPosition(img, draw=True)
            
            tipIds = [4,8,12,16,20]

            if len(lmList) != 0:

                if lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2]:
                    
                    
                    if lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2] and lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2]:
                                             

                        if lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2] and lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2]:
                           

                            if lmList[tipIds[1]][2] < lmList[tipIds[1] - 2][2] and lmList[tipIds[2]][2] < lmList[tipIds[2] - 2][2] and lmList[tipIds[3]][2] < lmList[tipIds[3] - 2][2] and lmList[tipIds[4]][2] < lmList[tipIds[4] - 2][2]:
                               
                                pag.press("space")
                                time.sleep(1.2)
                                # print("all open ")
                                continue
                            
                            # print("3")
                            pag.press("right")
                            time.sleep(0.4)
                            continue

                        # print("2")
                        pag.press("volumedown")
                        time.sleep(0.1)
                        continue

                    # print("index")     
                    pag.press("volumeup")

                elif lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
                    pag.press("left")
                    # print('palm close')
                    time.sleep(0.4)

                time.sleep(0.1)

            if stop_code == 1:
                cv2.destroyAllWindows()
                cap.release()
                break
    except:
        nf.notify("Error", "There is some error. Please close and run again.")
  
    finally:
        cv2.destroyAllWindows()
        cap.release()
            
       

def exit_action(icon):   
    global stop_code
    icon.visible = False 
    stop_code = 1
    icon.stop()

    
def setup(icon):
    icon.visible = True
    main_code()
    while icon.visible:   
        time.sleep(5)
        
    
    if icon.visible == False:
        sys.exit()


def init_icon():
    icon = pystray.Icon('mon')
    icon.menu = Menu(
        MenuItem('Exit', lambda : exit_action(icon)),
    )
    icon.icon = Image.open('gesture.png')
    icon.title = 'tooltip'

    icon.run(setup)

x = threading.Thread(target=init_icon(), daemon=True)
x.start()    
