import cv2
fname=input("Enter the path of the image to display: ")
img_arr=cv2.imread(fname)
cv2.imshow("Displaying Image",img_arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
