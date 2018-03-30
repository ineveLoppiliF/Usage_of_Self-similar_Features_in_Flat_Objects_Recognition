## Import libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

## Equalize both template and rectified image, and plot them
def equalize_template_and_rectified_scene(template_image, rect_test_image):
    
    ## Equalize both template and rectified image
    equalized_template_image = histogram_equalize(template_image)
    equalized_rect_test_image = histogram_equalize(rect_test_image)
    
    equalized_rect_stacked_image = np.hstack((equalized_rect_test_image, equalized_template_image))
    plt.imshow(cv2.cvtColor(equalized_rect_stacked_image , cv2.COLOR_BGR2RGB)), plt.title('Equalized template and object image'), plt.show()
    
    return equalized_template_image, equalized_rect_test_image

## Equalize RGB image
def histogram_equalize(img):
    b, g, r = cv2.split(img)
    red = cv2.equalizeHist(r)
    green = cv2.equalizeHist(g)
    blue = cv2.equalizeHist(b)
    return cv2.merge((blue, green, red))