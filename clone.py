import csv
import cv2
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split #importing all libraries

samples=[]
with open('./data/driving_log.csv') as f:
    reader=csv.reader(f)
    for line in reader:
        samples.append(line)             #samples for generation
samples=samples[1:]                      #excluding the first line consistingof the headings
train_samples,validation_samples=train_test_split(samples,test_size=0.2) #splitting the test and validation sets
correction=0.15 #steering correction for side images
def generator(samples,batch_size): #defining generator
    num_samples=len(samples)
    while 1:
        for offset in range(0,num_samples,batch_size):
            batch_samples=samples[offset:offset+batch_size]
            images=[]
            measurements=[]
            for batch_sample in batch_samples:
                source_path=batch_sample[0]
                filename=source_path.split('/')[-1]
                current_path='./data/IMG/'+filename
                image=cv2.imread(current_path)
                images.append(image)
                image_flip=cv2.flip(image,1) #flipping the images
                images.append(image_flip)
                measurement=float(batch_sample[3])
                measurements.append(measurement)
                measure_flip=float(measurement*-1.0)  #flipping the angles
                measurements.append(measure_flip)
            for batch_sample in batch_samples:
                source_path=batch_sample[1]
                filename=source_path.split('/')[-1]
                current_path='./data/IMG/'+filename
                image=cv2.imread(current_path)
                images.append(image)
                measurement=float(batch_sample[3])+correction #for the left side images
                measurements.append(measurement)
            for batch_sample in batch_samples:
                source_path=line[2]
                filename=source_path.split('/')[-1]
                current_path='./data/IMG/'+filename
                image=cv2.imread(current_path)
                images.append(image)
                measurement=float(batch_sample[3])-correction   #for the right side images
                measurements.append(measurement)
            X_train=np.array(images)
            y_train=np.array(measurements)
            yield sklearn.utils.shuffle(X_train,y_train)   #shuffling the data

train_generator=generator(train_samples,batch_size=32)
validation_generator=generator(validation_samples,batch_size=32)

from keras.models import Sequential
from keras.layers import Dense,Flatten,Lambda,Convolution2D,Cropping2D
from keras.layers.pooling import MaxPooling2D

model=Sequential() #defining the sequential model
model.add(Cropping2D(cropping=((70,25),(0,0)),input_shape=(160,320,3)))
model.add(Lambda(lambda x:x/255.0-0.5))
model.add(Convolution2D(24,5,5,subsample=(2,2),activation='relu'))
model.add(Convolution2D(36,5,5,subsample=(2,2),activation='relu'))
model.add(Convolution2D(48,5,5,subsample=(2,2),activation='relu'))
model.add(Convolution2D(64,3,3,activation='relu'))
model.add(Convolution2D(64,3,3,activation='relu'))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))

model.compile(loss='mse',optimizer='adam') 
model.fit_generator(train_generator,samples_per_epoch=len(train_samples),validation_data=validation_generator,nb_val_samples=len(validation_samples),nb_epoch=7) #training data

model.save('model.h5')