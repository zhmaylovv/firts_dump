import cv2
import numpy as np
import os


def get_img_list(directory=''):
    files = os.listdir(directory)
    return [i for i in filter(lambda x: x.endswith('.jpg'), files)]


from time import sleep

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create();


def find_face(img_list):
    """
    :param img_list:
    :return: list of face image
    """
    #Код добавления прямоугольника
    #for (x, y, w, h) in face:
     #       cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0),2)
    face_list = []
    for image in img_list:

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        face = faceCascade.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))

        if str(type(face)) == "<class 'numpy.ndarray'>":

            for (x, y, w, h) in face:
                face_list.append(gray_image[y:y+h, x:x+w])



    return face_list



image_list = [cv2.imread("Vasya" + str(i) + ".jpg") for i in range(3,26)]

face_list = find_face(image_list)

rr = [cv2.imread("IMG8.jpg")]

sravnenit = find_face(rr)
cv2.imshow("Image", sravnenit[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
ff = [1 for i in range(18)]

ttt = recognizer.train(face_list, np.array(ff))
recognizer.write('1.yml')
recognizer.read('1.yml')
id, ver = recognizer.predict(sravnenit[0])

ver = 100 - ver
print(id, ver)





#cv2.resize(image, (0,0), fx=0.5, fy=0.5)
'''for image in face_list:

    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''