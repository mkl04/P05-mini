from imutils.video import VideoStream
import imutils
import time

import cv2
from utils.aux_functions2 import *

vs = VideoStream(src=0).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:

    frame = vs.read()
    frame = imutils.resize(frame, width=400) # (300,400)

    masked_image = mask_from_image(frame)
    if len(masked_image) > 0:
        cv2.imshow("With mask", masked_image[0])

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()
