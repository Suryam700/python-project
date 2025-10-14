import cv2

# Configrable parameter
source = input("Enter your image name like 'image.jpg'... : ")
destination = input("Enter your resize image name like 'new_image.jpg'... : ")
scale_percent_for_width = int(input("Enter how much dimension you required for width: "))
scale_percent_for_height = int(input("Enter how much dimension you required for height: "))

image = cv2.imread(source, cv2.IMREAD_UNCHANGED)
# cv2.imshow("title", image)  no need in the last

# Calculate the 50% of original dimension
new_width = int((image.shape[1] * scale_percent_for_width) / 100)
new_height = int((image.shape[0] * scale_percent_for_height) / 100)

#                             __________________
# Resize image               |                  |--> input as a tuple
output = cv2.resize(image, (new_width, new_height))

cv2.imwrite(destination, output)
# cv2.waitKey(0) this run when we have imshow().
print("Your resize is generated.")