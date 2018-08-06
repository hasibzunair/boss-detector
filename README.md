 
<p align="center">
  <a href="#"><img src="https://github.com/hasibzunair/boss-detector/blob/master/demo%20pictures/strategy.png" height=100/></a>
</p>

<h1 align="center">
  Boss Detector using Facial Recognition
</h1>
<p align="center">
 
[![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

  Change your computer screen when your boss is coming.
</p>
<br/>

<p align="center">
  <a href="#"><img src="https://github.com/hasibzunair/boss-detector/blob/master/demo%20pictures/process.png" height=100/></a>
</p>
<h2 align="center">
  How it works?
</h2>
<p align="center">
  A program that detects when your boss is approaching and changes the computer screen instantly. It uses the classical LBPHFaceRecognizer algorithm for facial recognition. Upon detecting the boss, the interface changes the computer screen. It is a fun way to implement facial recognition.
</p>
<br/>







## Demo

Boss is approaching. Here, I am the boss, since my boss is out of the country, literally!

![alt text center](https://github.com/hasibzunair/boss-detector/blob/master/demo%20pictures/boss_is_nearby.png)

As he is approaches, the program fetches face images and classifies the image.

![alt text](https://github.com/hasibzunair/boss-detector/blob/master/demo%20pictures/boss_face_classified.png)

If the image is classified as the Boss, it will change the computer screen.

![alt text](https://github.com/hasibzunair/boss-detector/blob/master/demo%20pictures/fake-screen.png)

That's how you become employee of the month!

## PREREQUISITES
- Python 3(32bit)
- msvc++ 2015 redist

## Packages and dependencies
* virtualenv
* cv
* numpy
* PIL (pillow)
* tkinter

## Usage

Firstly, setup the virtual environment and train the program for your boss.
```
$ venv\Scripts\activate.bat
$ python boss_train.py
```
Second, start the boss detector.
```
$ python boss-detector.py
```
## Takeaways

* To use this, place your webcam at a position where you know your boss will come in that region. Works well even when boss is six to seven feet away from the camera

* Double check training images, xml file path(s) before running the program

## Video Link 
https://www.youtube.com/watch?v=17ElyWwVVdk&feature=youtu.be

## Contributing
There is still scope of improvement in this project. Most welcome to send pull requests. All the the best, being a good employee!
## License
[MIT](https://github.com/hasibzunair/boss-detector/blob/master/LICENSE)

## Author
[Hasib Zunair](http://hasibzunair.github.io/)

