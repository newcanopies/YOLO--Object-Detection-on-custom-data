#### Creator: OJAS JOSHI ####

README file for phone detection model 

Darknet Reference: YOLO V2 https://pjreddie.com/darknet/yolo/

SETUP, REQUIREMENTS, APPROACH and COMMENTS
-----------------------------------------------------------------------------------------------------
REQUIREMENTS

1) Python2 and compatible OpenCV
2) CUDA 8.1 or above
3) subprocess, os, glob

-----------------------------------------------------------------------------------------------------
SETUP
The default setup is configured assuming GPU access during runtime for both training and testing.

(optional) Only for CPU use
1) cd darknet
2) set all params to 0
3) make

(all other required config files are written in the wrappers)

-----------------------------------------------------------------------------------------------------
TRAINING:

1) Download pretrained YOLO weights for Imagenet in the same directory as darknet.exe:
	wget https://pjreddie.com/media/files/darknet19_448.conv.23 (for linux)
	curl -O https://pjreddie.com/media/files/darknet19_448.conv.23 (for mac)

(optional) 
Depending on the available computation, change batch size and subdivisions in line 3,4 cfg/yolo-obj.cfg (lesser the faster)

2) Run from /utility_functions

> python train_phone_finder.py <path-to-train-dir> 
> cd ../darknet
> ./darknet detector train cfg/obj.data cfg/yolo-obj.cfg darknet19_448.conv.23


(optional)
** NOTE: To run training without live display**
> python train_phone_finder.py <path-to-file> train

-----------------------------------------------------------------------------------------------------
TESTING: (please do step 2 of training to setup configuration files before testing)

Trained weight file can be downloaded from: 
https://drive.google.com/file/d/1P2Zb6gXLXlffHtgx3tsr_a3TaN5nrO68/view?usp=sharing

1)Run from /utility functions

> python find_phone.py <path-to-testfile> 


** NOTE: For custom weight file use:
> python find_phone.py <path-to-testfile> <path-to-weightfile>

(result also stored in darknet/results/test.txt and predicted image saved as prediction.png)

-----------------------------------------------------------------------------------------------------
APPROACH:

"bounding_box.py" and "preprocess.py" contain required functions for data preprocessing. 

Two parser functions parse through the labels.txt file to collect the training data in required format. Using the data, a 40x40 crop of the image is cut, centered at each indivitual center points of the phone, based on the centers of the images given in labels.txt. Using image smoothing and edge detection, a selective search is done on the crop to find the closest bounding contour around the phone. Each bounding box is amplified 1.2x times in width and height to correct the image processing errors. The widths and heights of these bounding boxes are stored as training labels in the YOLO V2 format. 
Preprocessing program creates the two more text files for the locations of the training data in YOLO V2 format. It contains a parameter to keep out a percentage of data as validation dataset.

"make_cfg.py" creates the required configuration files for the YOLO V2 training 

"train_phone_finder.py"
Wraps all the functions and calls ./darknet executable with required arguments to train with the given dataset

"find_phone.py"
Calls ./darknet executable with required arguments on the given custom weight file

----------------------------------------------------------------------------------------------------
COMMENTS: 

The algorithm in this setting was trained for 50 min on Nvidia 1080x for 500 iterations (batch size 64) using partly pretrained(ImageNet) YOLO V2 architechture. Based on the training procedure, the validation accuracy (considering error margin of 0.05) was 80% and the training accuracy was 95%. Using YOLO V2 had following advantages:

1) Uses data augmentation: Considering that the training data was very small, data augmentation could have helped the model
2) Dropout: YOLO V2 is very good to avoid overfitting to the data, which could have been easily possible given small amount of training dataset
3) Faster: YOLO V2 is one of the fastest object detection algorithm for training as well as test time
4) Accuracy: Although YOLO V2 gives lesser accuracy compared to Faster RCNN, given that the target test error was expected around 0.5, YOLO V2 seemed a good choice
5) Transfer Learning: With very less amount of training data, using pretrained models can heavily improve the model performance (although have to always look for overfitting)


Considering very less training data, it would be interesting to check performance of Siamese Networks such as those implemented by "Weakly Supervised One-Shot Detection with Attention Siamese Networks, Gil Keren et al"

-----------------------------------------------------------------------------------------------------

The folder contains 2 subfolders:

1)	utility_functions: 
 all wrapper/utility functions and train_phone_finder.py and find_phone.py

2)	darknet: 
 reference: https://pjreddie.com/darknet/yolo/

Note: Modifications done in detector.h, detector.c, darknet.c functions to adapt the necessary requirements of the given problem
 
** Note: darknet folder contains a folder "trained" which has validation and train image names used during training

