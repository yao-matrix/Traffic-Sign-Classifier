# The German Traffic Sign Recognition Benchmark
#
# sample code for reading the traffic sign images and the
# corresponding labels
#
# example:
#            
# trainImages, trainLabels = readTrafficSigns('GTSRB/Training')
# print len(trainLabels), len(trainImages)
# plt.imshow(trainImages[42])
# plt.show()
#
# have fun, Christian
# YAO Matrix

import matplotlib.pyplot as plt
import csv
from sklearn.model_selection import train_test_split
import pickle

def readTrafficSigns(rootpath):
    '''Reads traffic sign data for German Traffic Sign Recognition Benchmark.

    Arguments: path to the traffic sign data
    Returns:   list of images, list of corresponding labels'''
    images = [] # images
    labels = [] # corresponding labels
    # loop over all 43 classes
    for c in range(0, 43):
        prefix = rootpath + '/' + format(c, '05d') + '/' # subdirectory for each class
        gtFile = open(prefix + 'GT-'+ format(c, '05d') + '.csv') # annotations file
        gtReader = csv.reader(gtFile, delimiter=';') # csv parser for annotations file
        gtReader.next()
        # loop over all images in current annotations file
        for row in gtReader:
            images.append(plt.imread(prefix + row[0])) # the 1th column is the filename
            labels.append(row[7]) # the 8th column is the label
        gtFile.close()
    return images, labels

def readTestTrafficSigns(rootpath):
    '''Reads test traffic sign data for German Traffic Sign Recognition Benchmark.

    Arguments: path to the test traffic sign data
    Returns:   list of images, list of corresponding labels'''
    images = [] # images
    labels = [] # corresponding labels

    prefix = rootpath + '/'
    gtFile = open(prefix + 'GT-final_test.csv') # annotations file
    gtReader = csv.reader(gtFile, delimiter=';') # csv parser for annotations file
    gtReader.next()
    # loop over all images in current annotations file
    for row in gtReader:
        images.append(plt.imread(prefix + row[0])) # the 1th column is the filename
        labels.append(row[7]) # the 8th column is the label
    gtFile.close()
    
    return images, labels

if __name__ == "__main__":
  images, labels = readTrafficSigns("./data/GTSRB/Final_Training/Images")

  train = {}
  val = {}
  test = {}

  train["features"], val["features"], train["labels"], val["labels"] = train_test_split(images, labels, test_size=0.1, random_state=6)

  train_file = open('./data/gtsrb_train.pkl', 'wb')
  pickle.dump(train, train_file)

  val_file = open('./data/gtsrb_val.pkl', 'wb')
  pickle.dump(val, val_file)

  test["features"], test["labels"] = readTestTrafficSigns("./data/GTSRB/Final_Test/Images")
  test_file = open('./data/gtsrb_test.pkl', 'wb')
  pickle.dump(test, test_file)

  print("Data Preparation Done")
