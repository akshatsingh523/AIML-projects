import cv2
import os
import numpy as np

#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

image_dir = "C:/Users/aksha/OneDrive/Desktop/Summer Research/images"
output_dir = "C:/Users/aksha/OneDrive/Desktop/Summer Research/Enhanced Images"

images = os.listdir(image_dir)#list all the files in specific directories

for img_name in images:
    img_path = os.path.join(image_dir, img_name)# combine file name and input path
    img = cv2.imread(img_path) #read the image file 
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #BGR to gray 
    img_clahe = clahe.apply(img_gray) #apply clahe 

    # Split the input filename into base and extension
    base_name, ext = os.path.splitext(img_name)

    # Append a suffix to the base name to indicate the enhanced image
    out_name = base_name + '_enhanced' + ext

    out_path = os.path.join(output_dir, out_name)

    cv2.imwrite(out_path, img_clahe)
