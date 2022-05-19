Python 3.10.3 (tags/v3.10.3:a342a49, Mar 16 2022, 13:07:40) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import numpy
import numpy as np
import cv2 as cv
img = cv.imread('yang.jpg')
cv.imshow("FERRY",img)
img.item(350,350,1)
138
img.item(350,350,2)
137
img.item(350,350,0)
130
img.itemset((350,350,0),255)
img[350,350]
array([255, 138, 137], dtype=uint8)
cv.show("FERRY",img)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    cv.show("FERRY",img)
AttributeError: module 'cv2' has no attribute 'show'
cv.imshow("FERRY",img)
print(img)
[[[ 92 100 107]
  [ 86  94 101]
  [ 87  97 104]
  ...
  [122 137 133]
  [122 137 133]
  [122 137 133]]

 [[156 162 169]
  [148 157 161]
  [150 158 165]
  ...
  [140 155 151]
  [138 153 149]
  [137 152 148]]

 [[180 184 189]
  [172 179 182]
  [173 179 184]
  ...
  [138 155 151]
  [138 155 151]
  [137 154 150]]

 ...

 [[160 166 161]
  [162 168 163]
  [161 167 162]
  ...
  [213 210 202]
  [218 215 207]
  [225 222 214]]

 [[150 156 151]
  [154 160 155]
  [155 161 156]
  ...
  [214 210 205]
  [217 213 208]
  [221 217 212]]

 [[142 148 143]
  [150 156 151]
  [154 160 155]
  ...
  [214 210 205]
  [213 209 204]
  [210 206 201]]]
sample = img[500:600, 1000:1500]
cv.imshow("FERRY",sample)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    cv.imshow("FERRY",sample)
cv2.error: OpenCV(4.5.5) D:\a\opencv-python\opencv-python\opencv\modules\imgproc\src\color.cpp:182: error: (-215:Assertion failed) !_src.empty() in function 'cv::cvtColor'

sampleRoi = img[100:200, 200:400]
cv.imshow("",sampleRoi)
print(sampleRoi)
[[[207 202 193]
  [208 206 196]
  [213 208 199]
  ...
  [207 204 199]
  [207 204 200]
  [209 206 202]]

 [[219 214 205]
  [213 209 198]
  [211 206 197]
  ...
  [211 208 203]
  [210 207 202]
  [211 208 203]]

 [[225 219 208]
  [218 212 199]
  [215 209 198]
  ...
  [206 204 196]
  [204 202 194]
  [204 201 196]]

 ...

 [[211 209 198]
  [211 209 198]
  [215 213 202]
  ...
  [203 200 195]
  [201 198 193]
  [206 203 198]]

 [[213 211 200]
  [208 206 195]
  [211 209 198]
  ...
  [204 201 196]
  [202 199 194]
  [207 204 199]]

 [[211 209 198]
  [202 202 190]
  [208 206 195]
  ...
  [208 205 200]
  [202 199 194]
  [203 200 195]]]
img.size
2764800
img.dtype
dtype('uint8')
v
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    v
NameError: name 'v' is not defined. Did you mean: 'cv'?
cv.imshow("FERRY",img)
