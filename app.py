import cv2 as cv 


# Read Image
img = cv.imread('photos/f16.jpg')

# # Resize Image (changes resolution)
# img_resized = cv.resize(img, (800,600))

# # Draw a Rectangle to an Image
# cv.rectangle(img_resized, (20,30), (700,540), thickness=2, color=(200,200,12))
# cv.imshow('F-4', img_resized)

# # Gray Scale 
# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Grayscale", img_gray)

# # Blur
# img_blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", img_blur)

# # Edge 
# img_edge = cv.Canny(img_blur, 125, 175)
# cv.imshow("Edges",img_edge)


print(type(img))



cv.waitKey(0)



