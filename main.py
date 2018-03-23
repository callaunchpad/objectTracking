import os
import cv2
import time
import argparse
import multiprocessing
import numpy as np
import tensorflow as tf

#NOTE currently multiprocessing imports are unused
from multiprocessing import Queue, Pool


from utils import *
import clustering

CWD_PATH = os.getcwd()

#NUMWORKERS = 2
FILENAME = ''

IMAGE_WIDTH = 144
IMAGE = 144
FRAME_GAP = 2
BUFFER_SIZE = 4

'''
CONSTANTS THAT NEED TO BE FILLED OUT
'''
MODEL_NAME = "" #TODO
PATH_TO_CKPT = "" #TODO
PATH_TO_LABELS = "" #TODO
NUM_CLASSES = "" #TODO


'''
Loading label map
'''
#Load model into memory

detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


#INIT global objects List
global OBJECTS_LIST
OBJECTS_LIST = []

#TODO Fill out actual main items
if __name__ == '__main__':
    print("Running main")

    cap = cv2.VideoCapture(FILENAME)
    frame_num = 0
    image_buffer = []

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            while(cap.isOpened()):
                ret, frame = cap.read()
                if frame is None:
                    break
                if frame_num % frame_gap == 0:
                    ## THIS IS WHERE WE DO SHIT
                    image_buffer.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                if len(image_buffer) == BUFFER_SIZE:
                    print("pushing buffer")
                    #THIS IS WHERE WE DO STUFF WITH A FULL BUFFER

                    #EMPTY BUFFER
                    image_buffer = []

                frame_num += 1

    cap.release()
