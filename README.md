# Behaviorial Cloning Project

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

Overview
---
This repository contains the files for the Behavioral Cloning Project. The project involves development and implementation of a Deep Learning Architecture for the car to drive autonomously around the test track. The deep learning architecture is trained by driving the car around the track and after several laps of training, is allowed to drive autonomously. The project uses a software simulator to simulate a real car for the model.

In this project, I have used deep neural networks and convolutional neural networks to clone driving behavior. I have trained, validated and tested a model using Keras. The model output a steering angle to the autonomous vehicle.

I was provided a simulator where I could steer a car around a track for data collection. I have used image data and steering angles to train a neural network and then used this model to drive the car autonomously around the track.

I have also created a detailed writeup of the project. Check out the [writeup report](https://github.com/akashmod/Self_Driving_Car_Behavioral_Cloning/blob/master/writeup-report.ipynb) for this project. It is a markdown file.

The project consists of five files: 
* clone.py (script used to create and train the model)
* drive.py (script to drive the car)
* model.h5 (a trained Keras model)
* writeup_report.md (markdown file)
* Code_implemented_Final_Run_Video.mp4 (a video recording of the vehicle driving autonomously around the track for one full lap)

The Writeup
---
The writeup includes the [rubric points](https://review.udacity.com/#!/rubrics/432/view) as well as a description of how I addressed each point.  I have included a detailed description of the code used (with line-number references and code snippets where necessary), and links to other supporting documents or external references.  I have included images in the writeup to demonstrate how my code works with examples.  

The Project
---
The goals / steps of this project are the following:
* Used the simulator to collect data of good driving behavior 
* Designed, trained and validated a model that predicts a steering angle from image data
* Used the model to drive the vehicle autonomously around the first track in the simulator. The vehicle remained on the road for an entire loop around the track.
* Summarized the results with a written report

### Dependencies
This lab required:

* [CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit)

The lab enviroment can be created with CarND Term1 Starter Kit. Click [here](https://github.com/udacity/CarND-Term1-Starter-Kit/blob/master/README.md) for the details.

The following resources can be found in this github repository:
* clone.py
* drive.py
* video.py
* model.h5
* writeup_report.md

The simulator could not be uploaded in the repository because of the data limit by github. However, the codes can be accessed using jupyter notebook and the video file shows the final result of the car driving around the track.

## Details About Files In This Directory

### `drive.py`

For using `drive.py` it is required that you have saved the trained model as an h5 file, i.e. `model.h5` using the following commands.
```sh
model.save(filepath)
```

Once the model has been saved, it can be used with drive.py using this command:

```sh
python drive.py model.h5
```

The above command will load the trained model and use the model to make predictions on individual images in real-time and send the predicted angle back to the server via a websocket connection.

Note: There is known local system's setting issue with replacing "," with "." when using drive.py. When this happens it can make predicted steering values clipped to max/min values. If this occurs, a known fix for this is to add "export LANG=en_US.utf8" to the bashrc file.

#### Saving a video of the autonomous agent

```sh
python drive.py model.h5 run1
```

The fourth argument, `run1`, is the directory in which to save the images seen by the agent. If the directory already exists, it'll be overwritten.

```sh
ls run1

[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_424.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_451.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_477.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_528.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_573.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_618.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_697.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_723.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_749.jpg
[2017-01-09 16:10:23 EST]  12KiB 2017_01_09_21_10_23_817.jpg
...
```

The image file name is a timestamp of when the image was seen. This information is used by `video.py` to create a chronological video of the agent driving.

### `video.py`

```sh
python video.py run1
```

Creates a video based on images found in the `run1` directory. The name of the video will be the name of the directory followed by `'.mp4'`, so, in this case the video will be `run1.mp4`.

Optionally, one can specify the FPS (frames per second) of the video:

```sh
python video.py run1 --fps 48
```

Will run the video at 48 FPS. The default FPS is 60.

#### Why a video is provided

1. It's been noted the simulator might perform differently based on the hardware. So if the model drives successfully on a machine it might not on another machine. The video serves as a solid backup and a proof of successful code implementation in case this happens.
2. It helped in troubleshooting of the codes.


