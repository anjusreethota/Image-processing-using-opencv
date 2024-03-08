import cv2
fname=input("Enter the path of the image to display: ")
img_arr=cv2.imread(fname)
height,width,channel=img_arr.shape
print(f"Size of the image : {height}x{width}x{channel}")
