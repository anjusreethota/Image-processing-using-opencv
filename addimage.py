import cv2

fname = input("Enter the path of the image - 1: ")
img_arr = cv2.imread(fname)
cv2.imshow("Image - 1", img_arr)
fname2 = input("Enter the path of the image - 2: ")
img_arr_2 = cv2.imread(fname2)

img_arr_2 = cv2.resize(img_arr_2, img_arr.shape[:2][::-1])
cv2.imshow("Image - 2 after resizing", img_arr_2)
add_arr = cv2.add(img_arr, img_arr_2)
cv2.imshow("Image - 1 + Image - 2", add_arr)
cv2.waitKey(0)
cv2.destroyAllWindows()
