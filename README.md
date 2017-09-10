## Project: Build a Traffic Sign Recognition Program
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

Code Preparation
--
```shell
$ git clone https://github.com/yao-matrix/Traffic-Sign-Classifier.git
```

Data Preparation
--
Download GTSRB(German Traffic Sign Dataset).
```shell
1. $ mkdir data && cd ./data 
2. $ wget http://benchmark.ini.rub.de/Dataset/GTSRB_Final_Training_Images.zip
3. $ wget http://benchmark.ini.rub.de/Dataset/GTSRB_Final_Test_Images.zip
4. $ wget http://benchmark.ini.rub.de/Dataset/GTSRB_Final_Test_GT.zip
5. $ unzip GTSRB_Final_Training_Images.zip && unzip GTSRB_Final_Test_Images.zip
6. $ unzip GTSRB_Final_Test_GT.zip && cp GT-final_test.csv ./GTSRB/Final_Test/Images/
5. $ cd ../
6. $ python prepare_data.py
```

The Project
---
The goals / steps of this project are the following:
* Load the data set
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report

### Dependencies
This lab requires:

* [CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit)

The lab environment can be created with CarND Term1 Starter Kit. Click [here](https://github.com/udacity/CarND-Term1-Starter-Kit/blob/master/README.md) for the details.

### Dataset and Repository

1. Download the data set. The classroom has a link to the data set in the "Project Instructions" content. This is a pickled dataset in which we've already resized the images to 32x32. It contains a training, validation and test set.
2. Clone the project, which contains the Ipython notebook and the writeup template.
```sh
git clone https://github.com/udacity/CarND-Traffic-Sign-Classifier-Project
cd CarND-Traffic-Sign-Classifier-Project
jupyter notebook Traffic_Sign_Classifier.ipynb
```

### Requirements for Submission
Follow the instructions in the `Traffic_Sign_Classifier.ipynb` notebook and write the project report using the writeup template as a guide, `writeup_template.md`. Submit the project code and writeup document.
