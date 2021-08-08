import cv2
import os

path = r'D://2021/chulih/21-08-08/'

height = 1080

for p in os.listdir(path):
    if p.startswith('resized'):
        continue
    img = cv2.imread(path+p)
    hei, wid, _ = img.shape
    img = cv2.resize(img, None, fx=1.3 * height/hei, fy=height/hei)
    cv2.imwrite(path+'resized_'+p, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    print(f'{p} processed.')
