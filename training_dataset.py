from sklearn.model_selection import train_test_split
from create_dataset import *

import h5py
import numpy as np
import os
import glob
import cv2
import matplotlib.pyplot as plt

train_path = "dataset/train"
test_path  = "dataset/test"
h5_data    = "processing/data.h5"
h5_labels  = "processing/labels.h5"
test_size  = 0.10
seed       = 9

def train_model(tree):
    h5_data_1  = h5py.File(h5_data, 'r')
    h5f_label_1 = h5py.File(h5_labels, 'r')

    global_features_string = h5_data_1['dataset_1']
    global_labels_string   = h5f_label_1['dataset_1']

    global_features = np.array(global_features_string)
    global_labels   = np.array(global_labels_string)

    h5_data_1.close()
    h5f_label_1.close()
    print("==================================================================")
    print("                      TRAINING MODEL DATA        ")
    print(" Features shape : {}".format(global_features.shape))
    print(" Labels shape   : {}".format(global_labels.shape))
    print("\n")

    (trainDataGlobal, testDataGlobal, trainLabelsGlobal, testLabelsGlobal) = train_test_split(np.array(global_features), np.array(global_labels), test_size=test_size, random_state=seed)
    print(" Train data     : {}".format(trainDataGlobal.shape))
    print(" Test data      : {}".format(testDataGlobal.shape))
    print("\n")
    print(" Train labels   : {}".format(trainLabelsGlobal.shape))
    print(" Test labels    : {}".format(testLabelsGlobal.shape))

    tree.fit(trainDataGlobal, trainLabelsGlobal)

    print(" Accuracy       : {:.2f}%".format(100 * tree.score(testDataGlobal, testLabelsGlobal)))
    print("==================================================================")

def test_model(tree):
    train_labels = os.listdir(train_path)
    train_labels.sort()

    if not os.path.exists(test_path):
        os.makedirs(test_path)

    for file in glob.glob(test_path + "/*.jpg"):
        image = cv2.imread(file)
        image = cv2.resize(image, cropped_size)

        hu_moments_1 = hu_moments(image)
        haralick_texture_1   = haralick_texture(image)
        colour_histogram_1  = colour_histogram(image)

        global_feature = np.hstack([colour_histogram_1, haralick_texture_1, hu_moments_1])

        classification = tree.predict(global_feature.reshape(1,-1))[0]

        cv2.putText(image, train_labels[classification], (40,480), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,255,0), 5)

        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.show()