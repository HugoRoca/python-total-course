# pip3 install opencv-contrib-python
# For test cv2
# import cv2
# cv2.__version__  (this should return a version number)
# ---
# step 1:  pip3 install pillow
# step 2: pip3 install imutils
# step 3: brew install cmake
# step 4:
# brew install dlib
# or
# pip3 install dlib
# step 5:  pip3 install face_recognition

import cv2
import face_recognition as fr

# upload image
photo_control = fr.load_image_file("employees/FotoD.JPG")
photo_test = fr.load_image_file("employees/FotoC.jpg")

photo_control = cv2.cvtColor(photo_control, cv2.COLOR_BGR2RGB)
photo_test = cv2.cvtColor(photo_test, cv2.COLOR_BGR2RGB)

cv2.imshow('Photo Control', photo_control)
cv2.imshow('Photo test', photo_test)

cv2.waitKey(0)

