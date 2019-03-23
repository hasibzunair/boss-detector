import cv2                  
import numpy                 
from os import path, walk, listdir, makedirs 
from __config__ import *     


face_detector = cv2.CascadeClassifier(CASCADE_FILE)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# build dataset for face recognizer
def build():
    face_name = input("enter face name:")
    if not face_name:
        exit()
    id_file = path.join(DATASETS_DIR, face_name + ".txt")
    if path.isfile(id_file):
        id_file = open(id_file)
        face_id = int(id_file.read())
        id_file.close()

    else:
        id_dirs = listdir(DATASETS_DIR)
        face_id = len([d for d in id_dirs if path.isdir(path.join(DATASETS_DIR, d))])
        id_file = open(id_file, "w")
        id_file.write(str(face_id))
        id_file.close()
    print("face_name:%s\n  face_id:%s" % (face_name, face_id))
    face_dir = path.join(DATASETS_DIR, str(face_id)) 
    makedirs(face_dir, exist_ok=True)

    counter = 0
    start = len(listdir(face_dir))
    cam = cv2.VideoCapture(0)
    while True:
        
        _, frame = cam.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray_frame, SCALE, NEARBY)
        
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow(WINDOW_TITLE, frame)
            counter += 1
            sample_file = str(counter+start) + '.jpg'
            cv2.imwrite(path.join(face_dir, sample_file), gray_frame[y:y+h, x:x+w])
        if cv2.waitKey(5) == STOP_KEYCODE or counter >= TRAINING_SAMPLE_COUNT:
            break

    cam.release()
    cv2.destroyAllWindows()


# train face recognizer
def train():
    face_data = []
    face_ids = []
    face_dirs = list(walk(DATASETS_DIR))[0][1]
    face_dirs = list(map(lambda d:path.join(DATASETS_DIR, d), face_dirs))
    print("training... this will take a while.")
    for face_dir in face_dirs:
        face_id = int(path.basename(face_dir))
        id_imgs = list(walk(face_dir))[0][2]
        img_files = list(map(lambda f:path.join(face_dir, f), id_imgs))
        for img_file in img_files:
            frame = cv2.imread(img_file)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray_frame)
            for (x, y, w, h) in faces:
                face_data.append(gray_frame[y:y+h, x:x+w])
                face_ids.append(face_id)

    face_recognizer.train(face_data, numpy.array(face_ids))
    face_recognizer.save(TRAINED_DATA)


print("building...")
build()
print("training...")
train()
print("done...")