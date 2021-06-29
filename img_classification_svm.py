
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os
from skimage.transform import resize
from skimage.io import imread

Categories=['fire_images' ,'non_fire_images']
flat_data_arr=[]               #input array

target_arr=[]                  #output array

datadir ='fire_dataset/'     #path which contains all the categories of images

for i in Categories:
  print(f'loading... category : {i}')
  path=os.path.join(datadir,i)
  for img in os.listdir(path):
    img_array=imread(os.path.join(path,img))
    img_resized=resize(img_array,(150,150,3))
    flat_data_arr.append(img_resized.flatten())
    target_arr.append(Categories.index(i))
  print(f'loaded category:{i} successfully')

flat_data=np.array(flat_data_arr)
target=np.array(target_arr)
df=pd.DataFrame(flat_data)
df['Target']=target
x=df.iloc[:,:-1] #input data
y=df.iloc[:,-1] #output data

df

from sklearn import svm
from sklearn.model_selection import GridSearchCV
param_grid={'C':[10,100],'gamma':[0.0001,0.001],'kernel':['rbf','poly']}
svc=svm.SVC(probability=True)
model=GridSearchCV(svc,param_grid)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=1,stratify=y)
print('Splitted Successfully')
model.fit(x_train,y_train)
print('The Model is trained well with the given images')
# model.best_params_ contains the best parameters obtained from GridSearchCV


import pickle
pickle.dump(model,open("model3.pkl","wb"))

