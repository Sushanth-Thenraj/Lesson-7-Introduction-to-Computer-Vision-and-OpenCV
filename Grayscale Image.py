import cv2

#Upload Image
opencv_image = cv2.imread('Image.jpg')

#Convert to Grayscale
gray_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)

#Resize Grayscale Image
resized_image= cv2.resize(gray_image, (224, 224))

#Display Grayscale Image
cv2.imshow('Grayscale Image', resized_image)

#Wait for a key press
key= cv2.waitKey(0)

#Check if S key was pressed
if key== ord('s'):
    #Save the image
    cv2.imwrite('Grayscale_Image.jpg', resized_image)
    print("Image saved as Grayscale_Image.jpg")
else:
    print("Image not saved")

#Close all windows
cv2.destroyAllWindows()

#Print image properties
print("Image dimensions:", resized_image.shape)  # (height, width)