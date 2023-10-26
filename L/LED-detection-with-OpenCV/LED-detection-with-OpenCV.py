# import the necessary packages
from imutils import contours
# from skimage import measure
import numpy as np
import imutils
import cv2

# load the image, 
image = cv2.imread('sample.jpg', 1)

# convert it to grayscale, and blur it
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale_image.jpg', gray_image)   #This is done to create a greyscale image of the sample image file

image2 = cv2.imread('grayscale_image.jpg', 1)  
blurred_image = cv2.GaussianBlur(image2, (15, 15),10)
cv2.imwrite('blurred_image_after_greyscale.jpg', blurred_image) 

# threshold the image to reveal light regions in the blurred image
image3=cv2.imread('blurred_image_after_greyscale.jpg',1)
ret,threshold_image= cv2.threshold(image3,127,255,cv2.THRESH_BINARY) #Any thresholfd values less than 127 is set to 0 and any value set above 255 is set as 1
cv2.imwrite('threshold_image.jpg', threshold_image)    #An image file is being saved here for further processing


# perform a series of erosions and dilations to remove any small blobs of noise from the thresholded image
image4= cv2.imread('threshold_image.jpg',1)
kernel =np.ones((3,3), np.uint8)
eroded_image = cv2.erode(image4, kernel, iterations= 3)
dilated_image = cv2.dilate(eroded_image, kernel, iterations =4)
cv2.imwrite('Processed_image_after_dilution&erosion.jpg', dilated_image)


# perform a connected component analysis on the thresholded image, then initialize a mask to store only the "large" components
image5 = cv2.imread('Processed_image_after_dilution&erosion.jpg',cv2.IMREAD_COLOR)
image5_grayscale = cv2.cvtColor(image5, cv2.COLOR_BGR2GRAY)
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(image5_grayscale, connectivity=8)
mask = np.zeros_like(image5_grayscale, dtype="uint8") #This is done to create a mask of the image
for label in range(1, num_labels):
    component_size= stats[label, cv2.CC_STAT_AREA] #This is done to filter the components based on the size of the component
    if component_size >= 100:
        mask[labels == label] = 200
cv2.imwrite('large_component_mask.jpg', mask)  #here the components are being filtered based on the size of the component
	
# find the contours in the mask, then sort them from left to right
mask_image= cv2.imread('large_component_mask.jpg',1)
mask_image_grayscale = cv2.cvtColor(mask_image, cv2.COLOR_BGR2GRAY)
cnts = cv2.findContours(mask_image_grayscale.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(cnts[0], key=lambda x: cv2.boundingRect(x)[0]) #This is done to sort the contours from left to right

centroid_coordinates=[]
areas=[] # Initialising lists to store centroid coordinates adn area

# Loop over the contours
for contour in contours:
    # Calculate the area of the contour
    area= cv2.contourArea(contour)
    M=cv2.moments(contour) #calculating the centroid of the contour
    if M['m00'] != 0:
        cx = int(M["m10"] / M["m00"]) 
        cy = int(M["m01"] / M["m00"])
    else:
        cx,cy=0,0

    # Draw the bright spot on the image
    cv2.drawContours(mask_image,[contour],-1,(0,255,0),2)
    cv2.circle(mask_image, (cx,cy), 5,(0,0,255),-1)


    # Append centroid coordinates and area to the respective lists
    centroid_coordinates.append((cx,cy))
    areas.append(area)


cv2.imwrite('led_detection_results.png',mask_image) # Save the output image as a PNG file

# # Open a text file for writing
with open("led_detection_results.txt", "w") as file:
    file.write(f"No. of LEDs detected: {len(centroid_coordinates)}\n") # Write the number of LEDs detected to the file
#     # Loop over the contours
    for i,(centroid,area) in enumerate(zip(centroid_coordinates,areas)):
    
        # Write centroid coordinates and area for each LED to the file
        file.write(f"Centroid #{i + 1}: {centroid}\nArea #{i + 1}: {area}\n")