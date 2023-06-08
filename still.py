import cv2.cv2 as cv2
import numpy as np
img = cv2.imread('image.jpg')
img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
img = cv2.cvtColor(img,cv2.COLOR_HSV2RGB)
m = np.ones(img.shape,dtype="uint8") * 100
h,w = img.shape[:2]
og  = img

kernel_3x3 = np.ones((9,9),np.float32) / 100
sharp_kernel = np.array([[-1,-1,-1],
                         [-1,9,-1],
                         [-1,-1,-1]
                         ])

img = cv2.filter2D(img,-1,sharp_kernel)
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

erkernel =np.ones((5,5),np.uint8)

#print(img[0])
def makeBit(img,thresh=255/2):
    inxi = 0
    for i in img:
        inxj = 0
        for j in i:
            if j >= thresh:
                img[inxi][inxj] = 255
            else:
                img[inxi][inxj] = 0

            inxj+=1
        inxi+=1
    return img
cv2.imshow("Image",makeBit(img))
cv2.imshow("iroded",cv2.dilate(makeBit(img,100),erkernel))

cv2.waitKey(0)