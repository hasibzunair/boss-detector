import cv2                
import time               
from os import path, walk 
from __config__ import *
import time
import sys 
from PIL import Image, ImageTk
import tkinter

face_detector = cv2.CascadeClassifier(CASCADE_FILE)
face_recognizer = cv2.face.LBPHFaceRecognizer_create() 
face_recognizer.read(TRAINED_DATA)

names = {}
name_files = list(walk(DATASETS_DIR))[0][2]

for name_file in name_files:
    name_file = path.join(DATASETS_DIR, name_file)
    name = path.basename(name_file).split('.')[0]
    name_id = int(open(name_file).read())
    names[name_id] = name


font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(0)

def showPIL(pilImage):
    
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root, width=w, height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w / imgWidth, h / imgHeight)
        imgWidth = int(imgWidth * ratio)
        imgHeight = int(imgHeight * ratio)
        pilImage = pilImage.resize((imgWidth, imgHeight), Image.ANTIALIAS)

    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w / 2, h / 2, image=image)
    root.mainloop()


while True:
    _, frame = cam.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray_frame, SCALE, NEARBY)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 4)
        face_id = face_recognizer.predict(gray_frame[y:y+h, x:x+w])
        cv2.rectangle(frame, (x-2, y-20), (x+w+2, y+20), (255, 0, 0), -1)
        face_name = str(names[face_id[0]])
        
        if face_name == "Boss":
            pilImage = Image.open("fake_screen.png")
            showPIL(pilImage)
            cam.release()
            cv2.destroyAllWindows()
        else:
            print("NULL")
        cv2.putText(frame, face_name, (x, y+10), font, 0.7, (255, 255, 255), 1)
    
    cv2.imshow(WINDOW_TITLE, frame)
    if cv2.waitKey(5) == STOP_KEYCODE:
        break

