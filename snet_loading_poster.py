import cv2
import numpy as np

# Create a blank 1600x450 white image
image = np.ones((450,1600,3), np.uint8) * 255

# Set some parameters
font                   = cv2.FONT_HERSHEY_SIMPLEX
fontScale              = 3
fontColor              = (0,0,0)
lineType               = 5

# Get the text size
text = 'Loading...'
textsize = cv2.getTextSize(text, font, fontScale, lineType)[0]

# Get the center of the image
textX = (image.shape[1] - textsize[0]) // 2
textY = (image.shape[0] + textsize[1]) // 2

# Put text on image
cv2.putText(image, text, 
    (textX, textY), 
    font, 
    fontScale,
    fontColor,
    lineType)
# Save the image
cv2.imwrite('/Users/duanchenda/Desktop/gitplay/Dadaism7.github.io/poster.png',image)





