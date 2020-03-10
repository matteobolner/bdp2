# -*- coding: utf-8 -*-
import os
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray

#edit this with the complete path
IMAGE_DIR = "/shared_volume/input"
OUTPUT_DIR = "/shared_volume/output"

def convert(filename, name_only):
   # convert an image to its B/W equivalent
   # it creates a pdf with the orginal name + "_bw"
   #final_name, ext = os.path.splitext(filename)
   read_name = filename
   #print(read_name)
   noext_name, useless_ext = os.path.splitext(name_only)
   final_name = noext_name + "_bw.pdf"

   original = io.imread(read_name)
   grayscale = rgb2gray(original)
   fig, axes = plt.subplots(1, 2, figsize=(8, 4))
   ax = axes.ravel()

   ax[0].imshow(original)
   ax[0].set_title("Original")
   ax[1].imshow(grayscale, cmap=plt.cm.gray)
   ax[1].set_title("Grayscale")

   fig.tight_layout()
   plt.savefig(os.path.join(OUTPUT_DIR, final_name))
   plt.cla()
   plt.close()

start = time.time()
for root, dirs, files in os.walk(IMAGE_DIR):
    for name_only in files:
        name, extension = os.path.splitext(name_only)
        if os.path.isfile(os.path.join(OUTPUT_DIR, name + "_bw.pdf")):
            print(name + " already converted")
            continue
        else:
            #print(os.path.join(root, name_only))
            convert(os.path.join(root, name_only),name_only)
            
end = time.time()
print(end-start)

