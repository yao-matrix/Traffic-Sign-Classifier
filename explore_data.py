import pickle
import tensorflow as tf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
import cv2
import matplotlib.pyplot as plt

from sklearn.utils import shuffle
from collections import defaultdict
import time

RESIZED_IMG_SIZE = 32

if __name__ == "__main__":
  # load data
  datasets_path = "./data/"

  training_file = datasets_path + 'gtsrb_train.pkl'
  validation_file= datasets_path + 'gtsrb_val.pkl'
  testing_file = datasets_path + 'gtsrb_test.pkl'

  with open(training_file, mode='rb') as f:
    train = pickle.load(f)
  with open(validation_file, mode='rb') as f:
    valid = pickle.load(f)
  with open(testing_file, mode='rb') as f:
    test = pickle.load(f)

  # image size statistics
  # size_dict = defaultdict(int)
  # for img in train['features']:
  #   size_dict[img.shape] += 1
  # idx = np.arange(len(size_dict))
  # plt.bar(idx, size_dict.values(), align='center', width=0.5)
  # plt.xticks(idx, size_dict.keys())
  # ymax = max(size_dict.values()) + 1
  # plt.ylim(0, ymax)
  # plt.show()

  X_train = np.concatenate([cv2.resize(arr, (RESIZED_IMG_SIZE, RESIZED_IMG_SIZE), interpolation=cv2.INTER_CUBIC)[np.newaxis] for arr in train['features']])
  y_train = np.array(train['labels'])
  X_valid = np.concatenate([cv2.resize(arr, (RESIZED_IMG_SIZE, RESIZED_IMG_SIZE), interpolation=cv2.INTER_CUBIC)[np.newaxis] for arr in valid['features']])
  y_valid = valid['labels']
  X_test = np.concatenate([cv2.resize(arr, (RESIZED_IMG_SIZE, RESIZED_IMG_SIZE), interpolation=cv2.INTER_CUBIC)[np.newaxis] for arr in test['features']])
  y_test = test['labels']

  # get basic datset information
  ## Number of training examples
  n_train = X_train.shape[0]

  ## Number of validation examples
  n_validation = X_valid.shape[0]

  ## Number of testing examples
  n_test = X_test.shape[0]

  ## Shape of an traffic sign image?
  image_shape = X_train.shape[1:]

  ## How many unique classes/labels there are in the dataset.
  n_classes = len(set(y_train))

  print("Number of training examples = ", n_train)
  print("Number of validation examples = ", n_validation)
  print("Number of testing examples = ", n_test)
  print("Image data shape = ", image_shape)
  print("Number of classes = ", n_classes)
