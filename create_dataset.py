from sklearn.preprocessing import LabelEncoder

import numpy as np
import mahotas
import cv2
import os
import h5py

train_path       = "dataset/train"
h5_data          = "processing/data.h5"
h5_labels        = "processing/labels.h5"
cropped_size     = tuple((500, 500))
bins             = 8

def hu_moments(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    feature = cv2.HuMoments(cv2.moments(image)).flatten()
    return feature

def haralick_texture(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    haralick = mahotas.features.haralick(gray).mean(axis=0)
    return haralick

def colour_histogram(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist  = cv2.calcHist([image], [0, 1, 2], None, [bins, bins, bins], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist, hist)
    return hist.flatten()

def prepare_data():
    train_labels = os.listdir(train_path)
    train_labels.sort()

    global_features = []
    labels          = []

    for training_name in train_labels:
        dir = os.path.join(train_path, training_name)

        current_label = training_name

        for x in range(1, 80 + 1):
            file = dir + "/" + str(x) + ".jpg"

            image = cv2.imread(file)
            image = cv2.resize(image, cropped_size)

            fv_hu_moments = hu_moments(image)
            fv_haralick   = haralick_texture(image)
            fv_histogram  = colour_histogram(image)

            global_feature = np.hstack([fv_histogram, fv_haralick, fv_hu_moments])

            labels.append(current_label)
            global_features.append(global_feature)

        print(" Processed folder: {}".format(current_label))

    print("\n")
    print("==================================================================")
    print("                      DATASET MODEL DATA        ")
    print(" Feature vector size : {}".format(np.array(global_features).shape))

    print(" Training Labels     : {}".format(np.array(labels).shape))

    le          = LabelEncoder()
    target      = le.fit_transform(labels)

    print(" Target labels shape : {}".format(target.shape))
    print("==================================================================")

    h5_data_1 = h5py.File(h5_data, 'w')
    h5_data_1.create_dataset('dataset_1', data=np.array(global_features))

    h5_label_1 = h5py.File(h5_labels, 'w')
    h5_label_1.create_dataset('dataset_1', data=np.array(target))

    h5_data_1.close()
    h5_label_1.close()