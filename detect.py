import numpy as np
import cv2 
import imutils
import pytesseract
import pandas as pd
import time
import re

# true_nos = ['DL8CAF5030', 'HR13H0025', 'MH01BR2286', 'MH20EE7598', 'DL7CN5617', 'MH20BN9640', 'AP31BK3339', 'AP05BL6339', 'MH14JE4186', 'KA03MW0400', 'MH13BN8454', 'KL01BT2525', 'ML05S7595', 'MH12DE1433', 'KL18S5577']

def detect_no(image_path):
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        img = imutils.resize(img, width=500)
        #cv2.imshow("Original "+image_path, img)

        # Preprocessing - Add additional enhancements (e.g., contrast)
        lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        cl = clahe.apply(l)
        limg = cv2.merge((cl, a, b))
        img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #cv2.imshow("1 - Grayscale Conversion", gray)

        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        #cv2.imshow("2 - Bilateral Filter", gray)

        edged = cv2.Canny(gray, 170, 200)
        #cv2.imshow("3 - Canny Edges", edged)

        cnts= cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        cnts=sorted(cnts, key = cv2.contourArea, reverse = True)[:30] 
        NumberPlateCnt = None 

        for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.02 * peri, True)
                if len(approx) == 4:  
                        NumberPlateCnt = approx 
                        break

        # Masking the part other than the number plate
        mask = np.zeros(gray.shape,np.uint8)
        # new_image = cv2.drawContours(mask,[NumberPlateCnt],0,255,-1)
        # new_image = cv2.bitwise_and(img,img,mask=mask)
        # cv2.namedWindow("Final_image",cv2.WINDOW_NORMAL)
        # #cv2.imshow("Final_image",new_image)
        if NumberPlateCnt is not None:
                new_image = cv2.drawContours(mask, [NumberPlateCnt], 0, 255, -1)
                new_image = cv2.bitwise_and(img, img, mask=mask)
                cv2.namedWindow("Final_image", cv2.WINDOW_NORMAL)
                # cv2.imshow("Final_image", new_image)
        else:
                print("Number plate contour not found")
                return None  # or handle this condition accordingly

        # Configuration for tesseract
        config = ('-l eng --oem 1 --psm 6')

        # Run tesseract OCR on image
        text = str(pytesseract.image_to_string(new_image, config=config))

        # Print recognized text
        text = text.replace(' ', '').upper().strip()
        alphanumeric_chars = re.findall(r'[a-zA-Z0-9]', text)
        text = ''.join(alphanumeric_chars)
        print(text)
        #cv2.waitKey(0)
        return(text)

# detected_nos = []
# points = 0
# for i in range(15):
#         detected_nos.append(detect_no('./images/' + str(i + 1) + '.jpg'))
#         print(true_nos[i])
#         print()
#         if detected_nos[i] == true_nos[i]:
#                 points += 1
# accuracy = (points * 100) / len(true_nos)
# print(f"Accuracy: {accuracy}%")