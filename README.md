# Fire_detection_svm

This project is all about fire detection using svm algorithm. Here, we had developed a model and trained that model with several images. User have to upload an image and model will able to distinguish whether image contains fire or not with accuracy rate of 80%.
Tkinter is used for login/register purpose and for popping the message. <strong>Flask</strong>  webframework is also used in this project.

<h3><u>About SVM Alogorithm </u></h3>
Support vector machine is supervised learning algorithm for classification problems. In this algorithm, we separate the two classes with hyperplane. We have to choose maximal margin hyperplane, so this means that our optimal hyperplane will be the one who has maximum margin. 
In Svm , Kernel function basically convert data from low dimensions to high dimensions. Support Vector Machine draws a hyperplane in n dimensional space such that it maximizes the margin between classification groups.

<h3><u> About Model</u> </h3>

First of all, download the dataset and save it in the current directory.In this model we are going to train the model with some images. So for that first we need to resize all the image into a fixed dimension and then create a dataframe . After that 
, we are importing SVM model and here we are doing GridSearchCV for finding best value of 'C' and 'Gamma' and 'Kernel'. <br>

--- Low Gamma value means for selecting the hyperplane all points will be considered.<br>
--- High Gamma value means for selecting the hyperplane only nearby points will be considered.<br>

Regularization Parameter (C):<br>
It means adding some value to error function to improve the result.Basically value of C tells SVM , how much misclassification to avoid.<br>

--- High value of C is preferred because it gives us more accurate result.<br>

After that we will train the model , save it using pickle. 


