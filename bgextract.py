
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import cv2
obj= mpimg.imread('a.jpg')
plt.imshow(obj)
#obj=cv2.cvtColor(obj,cv2.COLOR_BGR2RGB)
#plt.imshow(obj)
#plt.show()
hsv_obj = cv2.cvtColor(obj, cv2.COLOR_RGB2HSV)
light_yellow = (7, 36, 8)
dark_yellow = (0, 0, 0)
from matplotlib.colors import hsv_to_rgb
lo_square = np.full((10, 10, 3), light_yellow, dtype=np.uint8) /255.0
do_square = np.full((10, 10, 3), dark_yellow, dtype=np.uint8) / 255.0
plt.subplot(1, 2, 1)


plt.subplot(1, 2, 2)

mask = cv2.inRange(hsv_obj, light_yellow, dark_yellow)
result = cv2.bitwise_and(obj, obj, mask=mask)
plt.subplot(1, 2, 1)
plt.imshow(mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result)


light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask_white = cv2.inRange(hsv_obj, light_white, dark_white)
result_white = cv2.bitwise_and(obj, obj, mask=mask_white)
plt.subplot(1, 2, 1)
plt.imshow(mask_white, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(result_white)

final_mask = mask + mask_white
final_result = cv2.bitwise_and(obj, obj, mask=final_mask)
plt.subplot(1, 2, 1)
plt.imshow(final_mask, cmap="gray")
plt.subplot(1, 2, 2)
plt.imshow(final_result)
cv2.imwrite("fra.jpg",final_result)