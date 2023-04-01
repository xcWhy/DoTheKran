import numpy as np
import cv2
from pyfirmata import Arduino, SERVO, util
from time import sleep

port = 'COM5'
pin = 10 # 360
pin2 = 11 # 180
board = Arduino(port)

board.digital[pin].mode = SERVO
board.digital[pin2].mode = SERVO

# imgpath = 'C:\\Users\\eli\\PycharmProjects\\kukli_na_konci\\'
imgpath = 'D:\\Desktop\\uch 10g\\VMKS\\OpenCV-Tutorials-main\\assets\\'

cap = cv2.VideoCapture(0)

one_img = cv2.imread(imgpath + 'one_pic4.jpg', 1)
one_img = cv2.cvtColor(one_img, cv2.COLOR_BGR2GRAY)

two_img = cv2.imread(imgpath + 'two_pic2.jpg', 1)
two_img = cv2.cvtColor(two_img, cv2.COLOR_BGR2GRAY)

three_img = cv2.imread(imgpath + 'three_pic2.jpg', 1)
three_img = cv2.cvtColor(three_img, cv2.COLOR_BGR2GRAY)

# one_img = cv2.resize(cap, (200, 200))
h, w = one_img.shape
h2, w2 = two_img.shape
h3, w3 = three_img.shape

imgs_list = [one_img, two_img, three_img]

# print(h, w)

method = cv2.TM_CCOEFF_NORMED



def rotateservo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)

rotateservo(pin, 90)
    
    
while True:
    
    rotateservo(pin, 90)
    
    ret, frame = cap.read()
    # print(ret)
    # print(frame.shape)

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # frame = cv2.resize(frame, (0, 0), fx=2.8, fy=2.1)

    height, width, channel = frame.shape
    screen = width, height # 640, 480
    # print ("screen: ", screen)


    result = cv2.matchTemplate(gray, one_img, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # result2 = cv2.matchTemplate(gray, two_img, method)
    # min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result)

    location = max_loc
    
    # location2 = max_loc2

    # h, w = img.shape

    bottom_right = (location[0] + w, location[1] + h)
    
    # bottom_right2 = (location2[0] + w2, location2[1] + h2)
    
    # print ("location: ",location)
    # print ("bottom right: ", bottom_right)
    
    if (max_val >= 0.6):
        cv2.rectangle(frame, location, bottom_right, 255, 5)
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("location: ",location)
        print ("bottom right: ", bottom_right)
        print ("=======s")
        print ("coords: ", ((location[1] + bottom_right[1]) / 2) / 3, "!!!!!q")
        coords_y = ((location[1] + bottom_right[1]) / 2) / 3
        
        coords_x = ((location[0] + bottom_right[0]) / 2) / 4
        
        rotateservo(pin, coords_y)
        rotateservo(pin2, coords_x)
        
    # if (max_val2 >= 0.6):
    #     cv2.rectangle(frame, location2, bottom_right2, 255, 5)
    #     print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #     print ("location: ",location)
    #     print ("bottom right: ", bottom_right)
    #     print ("=======s")
    #     print ("coords: ", ((location[1] + bottom_right[1]) / 2) / 3, "!!!!!")
    #     coords = ((location[1] + bottom_right[1]) / 2) / 3
    #     rotateservo(pin, coords)
    

        
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()