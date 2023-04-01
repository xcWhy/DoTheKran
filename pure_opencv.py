import numpy as np
import cv2


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
    
    
while True:
    
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

    location = max_loc

    # h, w = img.shape

    bottom_right = (location[0] + w, location[1] + h)
    
    # print ("location: ",location)
    # print ("bottom right: ", bottom_right)
    
    if (max_val >= 0.6):
        cv2.rectangle(frame, location, bottom_right, 255, 5)
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("location: ",location)
        print ("bottom right: ", bottom_right)
        print ("=======s")
        print ("coords: ", ((location[1] + bottom_right[1]) / 2) / 3, "!!!!!")
        coords = ((location[1] + bottom_right[1]) / 2) / 3
        
    else:
        ...
    

        
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()