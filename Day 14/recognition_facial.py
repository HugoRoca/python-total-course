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

# location face
location_face_A = fr.face_locations(photo_control)[0]
face_code_A = fr.face_encodings(photo_control)[0]

location_face_B = fr.face_locations(photo_test)[0]
face_code_B = fr.face_encodings(photo_test)[0]

# Show rectangle
cv2.rectangle(photo_control,
              (location_face_A[3], location_face_A[0]),
              (location_face_A[1], location_face_A[2]),
              (0, 255, 0),
              2)

cv2.rectangle(photo_test,
              (location_face_B[3], location_face_B[0]),
              (location_face_B[1], location_face_B[2]),
              (0, 255, 0),
              2)

# do match
result = fr.compare_faces([face_code_A], face_code_B)

# distance
distance = fr.face_distance([face_code_A], face_code_B)

cv2.putText(photo_test,
            f'{result} {distance.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)

cv2.imshow('Photo Control', photo_control)
cv2.imshow('Photo test', photo_test)

cv2.waitKey(0)

