import cv2
import numpy as np

img_rbg=cv2.imread("C:/Users/ssnar/Desktop/Jerry.jpg")
print(img_rbg.shape)  #To print the dimensions

img_rbg= cv2.resize(img_rbg,(800,800))  #Resize it 

img_color=img_rbg
for i in range(2):                          #Downsmaple the image
    img_color = cv2.pyrDown(img_color)

for i in range(7):                            #Apply Bilaterl filter
    img_color=cv2.bilateralFilter(img_color, d=9, sigmaColor=9, sigmaSpace=7)
    
for i in range(2):                                 #Upsample the image
    img_color=cv2.pyrUp(img_color)
    
img_gray=cv2.cvtColor(img_rbg, cv2.COLOR_RGB2GRAY)      #Convert original image to grayscale
img_blur=cv2.medianBlur(img_gray, 3)                      #Make it blur
img_edge=cv2.adaptiveThreshold(img_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blockSize = 9, C=2 )  #Create an edge mask

img_edge= cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)  #Convert the image back to Color
img_cartoon=cv2.bitwise_and(img_color, img_edge)      #Perform bitwise AND on bilateraled image and Edged image

stack=np.hstack([img_rbg,img_cartoon]) #Store old and new image in stack
cv2.imshow('Done!!!!', stack)        #Show the images
img_cartoon=cv2.resize(img_color,(1080,2280))
cv2.imwrite("C:/Users/ssnar/Desktop/vedika2.jpg",img_cartoon)
    
cv2.waitKey(0)
