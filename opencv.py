import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import pytesseract
import matplotlib.image as mpimg
import cv2 
from matplotlib.colors import hsv_to_rgb
import math
def FrameCapture(path): 
    vidObj = cv2.VideoCapture(path) 
    frameRate = vidObj.get(5)
    count=0
    c1=0
    success = 1
    while success: 
        frameId=vidObj.get(1)
        success, image = vidObj.read() 
        if frameRate!=0:
            if (frameId % math.floor(frameRate) == 0):
                if count%10==0:
                    c=str(count)
                    img="frame"+c+".jpg"
                    cv2.imwrite("frame%d.jpg" % count, image) 
                    obj= mpimg.imread(img)          
                  

                    hsv_obj = cv2.cvtColor(obj, cv2.COLOR_RGB2HSV)
                    light_yellow = (7, 36, 8)
                    dark_yellow = (0, 0, 0)
                    lo_square = np.full((10, 10, 3), light_yellow, dtype=np.uint8) /255.0
                    do_square = np.full((10, 10, 3), dark_yellow, dtype=np.uint8) / 255.0
                    plt.subplot(1, 2, 1)
                   
                    plt.subplot(1, 2, 2)
                    
                    
                    mask = cv2.inRange(hsv_obj, light_yellow, dark_yellow)
                    result = cv2.bitwise_and(obj, obj, mask=mask)
                    plt.subplot(1, 2, 1)
                    
                    plt.subplot(1, 2, 2)
                    
                   
                    
                    light_white = (0, 0, 200)
                    dark_white = (145, 60, 255)
                    mask_white = cv2.inRange(hsv_obj, light_white, dark_white)
                    result_white = cv2.bitwise_and(obj, obj, mask=mask_white)
                    plt.subplot(1, 2, 1)
                    
                    plt.subplot(1, 2, 2)
                    
                   
                    print("complete:")
                    final_mask = mask + mask_white
                    final_result = cv2.bitwise_and(obj, obj, mask=final_mask)
                    plt.subplot(1, 2, 1)
                    plt.imshow(final_mask, cmap="gray")
                    plt.subplot(1, 2, 2)
                    plt.imshow(final_result)
                   
                    cv2.imwrite("cam1-fr%d.jpg" %c1,final_result)
                    path="cam1-fr"+str(c1)+".jpg"
                    images=Image.open(path)
                    c1+=1
                    str1=pytesseract.image_to_string(images)
                    print("output text:\t"+str1)
                count += 1
            
if __name__ == '__main__': 
  
    # Calling the function 
    FrameCapture("sample1.mp4") 
