import cv2
import os
import sys
from string import Template
from glob import glob

# first argument is the haarcascades path
face_cascade_path = 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(os.path.expanduser(face_cascade_path))

scale_factor = 1.1
min_neighbors = 3
min_size = (30, 30)
flags = cv2.cv.CV_HAAR_SCALE_IMAGE


def extract_faces(path):
    print "faces"
    full_path = path + '/*.jpg'
    print full_path
    images = glob(full_path)
    # print images
    for infname in images:
        image_path = os.path.expanduser(infname)
        image = cv2.imread(image_path)
        # print image
        faces = face_cascade.detectMultiScale(image, scaleFactor=scale_factor, minNeighbors=min_neighbors,
                                              minSize=min_size, flags=flags)
        for (x, y, w, h) in faces:
            if(w > 200 and h > 200):
                #cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
                outfname = "/CS/covers/outfaces/%s" % os.path.basename(infname)
                print x, y, w, h
                print image.shape
                image = image[x:w+75, y:h+75]
                print image.shape
                # print outfname
                cv2.imwrite(os.path.expanduser(outfname), image)


extract_faces('faces')