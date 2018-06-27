# Boss-detector
Change your computer screen when your boss is coming.

# Demo

Video Link : https://www.youtube.com/watch?v=17ElyWwVVdk&feature=youtu.be

Boss is approaching. Here, I am the boss, since my boss is out of the country, literally!

![alt text](https://github.com/hasibzunair/boss-detector/blob/master/boss_is_nearby.png)

As he is approaches, the program fetches face images and classifies the image.

![alt text](https://github.com/hasibzunair/boss-detector/blob/master/boss_face_classified.png)

If the image is classified as the Boss, it will change the computer screen.

![alt text](https://github.com/hasibzunair/boss-detector/blob/master/fake_screen.png)

That's how you become employee of the month!

## PREREQUISITES
- Python 3(32bit)
- msvc++ 2015 redist

# Packages and dependencies
* virtualenv
* cv2
* numpy
* PIL (pillow)
* tkinter

# Usage

Firstly, setup the virtual environment and train the program for your boss.
```
$ venv\Scripts\activate.bat
$ python boss_train.py
```
Second, start the boss detector.
```
$ python boss-detector.py
```

# Contributing

There is still scope of improvement in this project. Most welcome to send pull requests. All the the best, being a good employee!


