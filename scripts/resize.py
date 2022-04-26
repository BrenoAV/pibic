import os
import sys
import cv2

PATH_ORIGEM = sys.argv[1]
PATH_DESTINO = sys.argv[2]
WIDTH = int(sys.argv[3])
HEIGHT = int(sys.argv[4])


for file in os.listdir(PATH_ORIGEM):
    img = cv2.imread(os.path.join(PATH_ORIGEM, file))
    img = cv2.resize(img, (WIDTH, HEIGHT))
    cv2.imwrite(os.path.join(PATH_DESTINO, file), img)
