import cv2
fname=input("Enter the path of the image to display: ")
img_arr=cv2.imread(fname)
grayscale_img_arr=cv2.cvtColor(img_arr,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale Image",grayscale_img_arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
