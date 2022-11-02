import os
from time import sleep

import numpy
import cv2
import face_recognition as fr

route = 'employees'
my_images = []
employee_names = []
employee_list = os.listdir(route)

for name in employee_list:
    current_image = cv2.imread(f'{route}/{name}')
    my_images.append(current_image)
    employee_names.append(os.path.splitext(name)[0])

print(employee_names)


def encode(images):
    encode_list = []

    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encoded = fr.face_encodings(image)[0]
        encode_list.append(encoded)

    return encode_list


encoded_employees_list = encode(my_images)

# take image from webcam
capture = cv2.VideoCapture(0)
sleep(2)
# read image of webcam
successfully, image_capture = capture.read()

if not successfully:
    print("Sorry, we don't take image")
else:
    face_capture = fr.face_locations(image_capture)
    face_capture_encoded = fr.face_encodings(image_capture, face_capture)

    for face_encoded, face_loc in zip(face_capture_encoded, face_capture):
        match = fr.compare_faces(encoded_employees_list, face_encoded)
        distance = fr.face_distance(encoded_employees_list, face_encoded)

        print(distance)

        match_index = numpy.argmin(distance)

        if distance[match_index] > 0.6:
            print("Don't match in database")
        else:
            print("Welcome")

