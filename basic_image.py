import os
import cv2


current_path = os.path.dirname(os.path.abspath(__file__))

img_path = os.path.join(current_path, 'cat.jpg')

img_read = cv2.imread(img_path, cv2.IMREAD_COLOR)


# resized_img = cv2.resize(img_read, (400, 200))
# resized_img = cv2.resize(img_read, (0,0), fx=0.5, fy=0.5)

cropped_img = img_read[81:336, 179:399]

saved_path = os.path.join(current_path, 'img_saved', 'saved_cat.jpg')
cv2.imwrite(saved_path, cropped_img)

# cv2.imshow('the image', cropped_img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()