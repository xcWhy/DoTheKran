import numpy as np
import cv2

# imgpath = 'C:\\Users\\eli\\PycharmProjects\\kukli_na_konci\\'
imgpath = 'assets\\'

cap = cv2.VideoCapture(0)

# print(h, w)

class img_object():
    def __init__(self, img_file) -> None:
        
        self.img_file = img_file
        
        self.img = cv2.imread(imgpath + self.img_file, 1)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        
        self.h, self.w = self.img.shape

        
    def check(self):
        
        self.result = cv2.matchTemplate(gray, self.img, method)
        self.min_val, self.max_val, self.min_loc, self.max_loc = cv2.minMaxLoc(self.result)
        
        self.location = self.max_loc
        
        self.bottom_right = (self.location[0] + self.w, self.location[1] + self.h)
           
        
        
one_img = img_object('one_pic4.jpg')
two_img = img_object('two_pic2.jpg')
three_img = img_object('three_pic2.jpg')


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

    one_img.check()
    two_img.check()
    three_img.check()

    
    if (one_img.max_val >= 0.6):
        cv2.rectangle(frame, one_img.location, one_img.bottom_right, 255, 5)
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("coords: ", ((one_img.location[1] + one_img.bottom_right[1]) / 2) / 3, "!!!!!")
        
        coords = ((one_img.location[1] + one_img.bottom_right[1]) / 2) / 3
    
    if (two_img.max_val >= 0.6):
        cv2.rectangle(frame, two_img.location, two_img.bottom_right, 128, 5)
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("coords: ", ((two_img.location[1] + two_img.bottom_right[1]) / 2) / 3, "!!!!!")
        
        coords = ((two_img.location[1] + two_img.bottom_right[1]) / 2) / 3
        
    if (three_img.max_val >= 0.6):
        cv2.rectangle(frame, three_img.location, three_img.bottom_right, 0, 5)
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("coords: ", ((three_img.location[1] + three_img.bottom_right[1]) / 2) / 3, "!!!!!")
        
        coords = ((three_img.location[1] + three_img.bottom_right[1]) / 2) / 3

        
        
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()