import cv2
import os
import re

img_folder = "/media/sf_shared/datamatrix/sck"
files = [f for f in os.listdir(img_folder) if re.match(r'.*_0.bmp', f)]

i = 1

cv2.namedWindow("image")
for f in files :
	img = cv2.imread(os.path.join(img_folder, f))
	crop_img = img[820:1130, 800:1150]
	cv2.imshow("image", crop_img)
	cv2.waitKey(1000)
	crop_f = "{0}.bmp".format(i)
	i += 1
	cv2.imwrite(os.path.join(img_folder, crop_f), crop_img)
	print(crop_f)
cv2.destroyAllWindows()
