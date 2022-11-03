import os
from time import sleep
from datetime import datetime
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


# register
def register_assistance(person):
    file = open('assistance.csv', 'r+')
    data_list = file.readlines()
    names = []

    for line in data_list:
        input_line = line.split(',')
        names.append(input_line[0])

    if person not in names:
        now = datetime.now()
        string_now = now.strftime('%H:%M:%S')
        file.writelines(f'\n{person}, {string_now}')


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
            name = employee_names[match_index]
            # get coordinate
            y1, x2, y2, x1 = face_loc
            cv2.rectangle(image_capture, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(image_capture, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(image_capture, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            register_assistance(name)

            cv2.imshow('Web image', image_capture)
            cv2.waitKey(0)
