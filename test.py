import cv2
import numpy as np

# read image
img = cv2.imread('test2.png')

# read template with alpha
tmplt = cv2.imread('/Find image on screen/images/templates\ModRareKillVoidtouched.png', cv2.IMREAD_UNCHANGED)
hh, ww = tmplt.shape[:2]

# extract template mask as grayscale from alpha channel and make 3 channels
tmplt_mask = tmplt[:,:,3]
tmplt_mask = cv2.merge([tmplt_mask,tmplt_mask,tmplt_mask])

# extract templt2 without alpha channel from tmplt
tmplt2 = tmplt[:,:,0:3]

# do template matching
corrimg = cv2.matchTemplate(img,tmplt2,cv2.TM_CCORR_NORMED, mask=tmplt_mask)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corrimg)
max_val_ncc = '{:.3f}'.format(max_val)
print("correlation match score: " + max_val_ncc)
xx = max_loc[0]
yy = max_loc[1]
print('xmatch =',xx,'ymatch =',yy)

# draw red bounding box to define match location
result = img.copy()
pt1 = (xx,yy)
pt2 = (xx+ww, yy+hh)
cv2.rectangle(result, pt1, pt2, (0,255,255), 1)

cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save results
cv2.imwrite('logo_hat_match2.png', result)