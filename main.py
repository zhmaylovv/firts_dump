from imageai.Detection import ObjectDetection

import os
import glob
import numpy as np
import cv2
import tensorflow as tf
from fr_utils import *
from inception_blocks_v2 import *
from keras import backend as K




import json

def write_json (data, file_name):
	with open(file_name, 'w', encoding="utf-8") as file:
		json.dump(data, file, indent=2, ensure_ascii= False)
	pass

if __name__ == '__main__':
    print ('wow lets START')
    K.set_image_data_format('channels_first')
    FRmodel = faceRecoModel(input_shape=(3, 96, 96))
    def triplet_loss (y_true, y_pred, alpha=0.3):
        anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
        pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)), axis=-1)
        neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)), axis=-1)
        basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
        loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
        return loss
    FRmodel.compile(optimizer='adam', loss=triplet_loss, metrics=['accuracy'])
    load_weights_from_FaceNet(FRmodel)


    def prepare_database():
        database = {}
        for file in glob.glob("images/*"):
            identity = os.path.splitext(os.path.basename(file))[0]
            database[identity] = img_to_encoding('images/' + file, FRmodel) #функция из ак_гешд
        return database


    def who_is_it(image, database, model):
        encoding = img_to_encoding(image, model)

        min_dist = 100
        identity = None

        # Loop over the database dictionary's names and encodings.
        for (name, db_enc) in database.items():
            dist = np.linalg.norm(db_enc - encoding)
            print('distance for %s is %s' % (name, dist))
            if dist < min_dist:
                min_dist = dist
                identity = name

        if min_dist > 0.52:
            return None
        else:
            return identity

    img = cv2.imread("Vasya21.jpg")
    database = prepare_database()
    result = who_is_it(img,database, FRmodel)
    print(result)

    ''' Рабочий код распознования картинки 
    objecs_list = []
    exec_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(exec_path, 'resnet50_coco_best_v2.0.1.h5'))
    detector.loadModel()

    list = detector.detectObjectsFromImage(
        input_image=os.path.join(exec_path, 'objects.jpg'),
        output_image_path=os.path.join(exec_path, 'new_objects.jpg'),


    )
    write_json(list, 'list_object_finded.json')

'''


    ''' рабочий код распознования видео добавить в импорт Video
    
    execution_path = os.getcwd()

    detector = VideoObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
    detector.loadModel()

    video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "traffic.mp4"),
                                                 output_file_path=os.path.join(execution_path, "traffic_detected")
                                                 , frames_per_second=20, log_progress=True)

    print(video_path)
'''
    '''
    Рабочий код распознования фото
    exec_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(exec_path, 'resnet50_coco_best_v2.0.1.h5'))
    detector.loadModel()

    list = detector.detectObjectsFromImage(
        input_image=os.path.join(exec_path, 'objects.jpg'),
        output_image_path=os.path.join(exec_path, 'new_objects.jpg')
    )
'''