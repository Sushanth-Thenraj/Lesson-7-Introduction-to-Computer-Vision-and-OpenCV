import cv2

#Load the image
image=cv2.imread('Test_Image.jpg')

#Resize image to 200x200 pixels
resized_image_200=cv2.resize(image,(200,200))

#Display the resized image
cv2.imshow('Resized Image: ',resized_image_200)

#Save Images
cv2.imwrite('Resized_Image_small.jpg',resized_image_200)

#Wait for key press
cv2.waitKey(0)

#Resize image to 400x400 pixels
resized_image_400=cv2.resize(image,(400,400))

#Display the resized image
cv2.imshow('Resized Image: ',resized_image_400)

#Save Image
cv2.imwrite('Resized_Image_medium.jpg',resized_image_400)

#Wait for key press
cv2.waitKey(0)

#Resize image to 600x600 pixels
resized_image_600=cv2.resize(image,(600,600))

#Display the resized image
cv2.imshow('Resized Image: ',resized_image_600)

#Save Image
cv2.imwrite('Resized_Image_large.jpg',resized_image_600)

#Wait for key press
cv2.waitKey(0)

cv2.destroyAllWindows()
#End of code