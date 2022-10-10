import pyautogui
from pyautogui import PyAutoGUIException
import time
import keyboard

snapchat_send_button = "images/send_snap.png"
snapchat_new_snap_button = "images/new_snap_3.png"
snapchat_reply = "images/reply_button_2.png"
snapchat_back = "images/snap_go_back.png"
the_chat = "images/chat_button.png"

reply_button_x = 930
reply_button_y = 870

send_button_x = 1165
send_button_y = 967

chat_button_x = 700
chat_button_y = 88

replies = int(0)


def send_snap(loc):
    pyautogui.click(loc)
    time.sleep(1)
    print("Sending Snap")
    pyautogui.click(reply_button_x, reply_button_y)
    time.sleep(1)
    pyautogui.click(send_button_x, send_button_y)


while keyboard.is_pressed('F') == False:
    find_go_back_button = pyautogui.locateOnScreen(snapchat_back, grayscale=False, confidence=0.9)
    find_the_chat = pyautogui.locateOnScreen(the_chat, grayscale=False, confidence=0.9)
    find_snap = pyautogui.locateOnScreen(snapchat_send_button, grayscale=False, confidence=0.7)
    find_new_snap = pyautogui.locateOnScreen(snapchat_new_snap_button, grayscale=False, confidence=0.9)
    find_reply_button = pyautogui.locateOnScreen(snapchat_reply, grayscale=False, confidence=0.5)

    # print(find_snap, find_new_snap, find_reply_button)
    if find_go_back_button != None:
        pyautogui.click(find_go_back_button)
        continue
    elif find_the_chat != None:
        pyautogui.click(chat_button_x, chat_button_y)
        continue
    elif find_snap != None:
        replies+=1
        print(f"{replies} New Snap Detected ")
        continue
    elif find_reply_button != None:
        replies+=1
        print(f"{replies} New Reply Found")
        send_snap(find_reply_button)
        continue
    elif find_new_snap != None:
        replies+=1
        print(f"{replies} New Snap Detected")
        pyautogui.click(find_new_snap)
        time.sleep(1)
        pyautogui.leftClick()
        continue
