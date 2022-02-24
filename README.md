## Boss detector using facial recognition

Change your monitor screen when your boss is coming towards you!

[![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

<br/>

```mermaid
flowchart TD
	A[Get face image from camera] --> B{Is it your boss?};
	B -- Yes --> C[Change monitor screen!];
	C -- No --> A;
```

A program that detects when your boss is approaching and changes the computer screen instantly. It uses the classical LBPH algorithm for facial recognition. Initially the system is training with the boss's face. When boss is detected, the interface changes the computer screen. It is a fun way to implement facial recognition! Video demo [here](https://www.youtube.com/watch?v=17ElyWwVVdk).


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
- Python 3.6
- OpenCV 3+

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

* Delete contents inside the data folder to make new changes if any.

## Video Demo
Click [here](https://www.youtube.com/watch?v=17ElyWwVVdk&feature=youtu.be) for the demo.

## Contributing
There is still scope of improvement in this project. Most welcome to send pull requests. All the the best, being a good employee!
## License
[MIT](https://github.com/hasibzunair/boss-detector/blob/master/LICENSE)

## Author
[Hasib Zunair](http://hasibzunair.github.io/)

