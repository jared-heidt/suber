import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread('../img/2022-04-20.jpg', 0)

def simple_edge_detection(image): 
    edges_detected = cv.Canny(image , 100, 200) 
    images = [image , edges_detected]
    location = [121, 122] 
    for loc, edge_image in zip(location, images): 
        plt.subplot(loc) 
        plt.imshow(edge_image, cmap='gray')
        cv.imwrite('../plot/edge_detected.png', edges_detected) 
        plt.savefig('../plot/edge_plot.png') 
        plt.show()

def main():
    simple_edge_detection(img)

if __name__ == "__main__":
    main()