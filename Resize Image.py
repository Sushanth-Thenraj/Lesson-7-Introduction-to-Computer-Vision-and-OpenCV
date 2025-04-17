import cv2

#Upload Image
opencv_image = cv2.imread('Image.jpg')

#Resize Window without resizing image
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)#Allows window to be resized
cv2.resizeWindow('Image', 800, 600)#Resizes window to 800x600

#Display image in resized window
cv2.imshow('Image', opencv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Print image properties
print("Image dimesions:", opencv_image.shape)  # (height, width, channels)