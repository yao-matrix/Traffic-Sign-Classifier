## Project: Build a Traffic Sign Recognition

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

