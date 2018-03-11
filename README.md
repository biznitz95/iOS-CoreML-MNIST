# Machine Learning on iOS with Keras and CoreML

This is the implementation of Number recognition using Keras-MNIST model on Apple's CoreML Framework.

The app fetches image from your hand writing and perform number recognition in real-time right on the device.

## Requirements

- Xcode 9 
- iOS 11
- For training: Python 3.6 (install keras, h5py, tensorflow and coremltools)


## Training the model

```
(coreml) $ pip install tensorflow keras h5py coremltools
(coreml) $ sudo python create_cnn_model.py
(coreml) $ sudo python convert_mode.py
```

## Running the app

To use this app, open **iOS-CoreML-MNIST.xcodeproj** in Xcode 9 and run it on a device with iOS 11. (You can also use simulator)

## Companion article

If you are interested in training your custom MNIST model from scratch, a **step-by-step tutorial** is available at - [**Link**](https://sriraghu.com/2017/07/06/computer-vision-in-ios-coremlkerasmnist/)

You can find the companion article [here](http://itywik.org/2018/03/11/machine-learning-on-ios-with-keras-and-coreml/)

## YouTube Video

You can watch my YouTube video on this topic [here](https://youtu.be/FKDaFXZ0q1M)

## Results

These are the results of the app when tested on iPhone 7. 

<img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0016.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0017.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0018.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0019.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0020.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0021.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0022.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0023.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0024.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0025.PNG" alt="Result 1" width="280"> <img src="https://github.com/r4ghu/iOS-CoreML-MNIST/blob/master/Screenshots/IMG_0026.PNG" alt="Result 1" width="280">

## Thanks

Thanks to Sri Raghu Malireddi / [@r4ghu](https://sriraghu.com) whose app I cloned for this tutorial.
