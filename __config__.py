import os.path

CASCADE_FILE = os.path.expandvars(".\\res\\haarcascade_frontalface_default.xml")
DATASETS_DIR = os.path.expandvars('.\\data')
TRAINED_DATA = os.path.expandvars('.\\training\\trainer.yml')
STOP_KEYCODE = 27
TRAINING_SAMPLE_COUNT = 100

SCALE = 1.2
NEARBY = 6

WINDOW_TITLE = "cv2.imshow()  # ESC to stop"