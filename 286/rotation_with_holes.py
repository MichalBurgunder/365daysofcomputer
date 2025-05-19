import cv2
import numpy as np
import math
# from google.colab.patches import cv2_imshow

A1 = cv2.imread("sushi.jpg", cv2.IMREAD_GRAYSCALE)


h_old = A1.shape[0]
w_old = A1.shape[1]

h_new = A1.shape[0]*2
w_new = A1.shape[1]*2

# here we try to get the "black holes" that come from not interpolating

A_next = np.zeros((h_new,w_new))

theta = -math.pi/6

# translate image centre of A1 to origin
T1 = np.array(
[[1, 0, -h_old/2],
 [0, 1, -w_old/2],
 [0, 0,        1]])

# we rotate by theta
R = np.array(
[[math.cos(theta),-math.sin(theta), 0],
 [math.sin(theta), math.cos(theta), 0],
 [       0,               0,        1]])

# translate origin to image centre of A2
T2 = np.array(
[[1, 0, h_new/2-100],
 [0, 1, w_new/2-100],
 [0,0,1]])

# transformation that rotates A1 by theta about its centre and maps to the
# centre of A2
transformation_matrix = np.matmul(T2,np.matmul(R,T1))

for i in range(0, h_new):
  for j in range(0, w_new):
    # convert point to homegeneous coordinates
    homogenous_point = np.array([i,j,1])

    # transform with matrix A
    q = np.matmul(A,homogenous_point)
    
    # coordinates in A1
    x = round(q[0])
    y = round(q[1])

    # we check if it's inside, and put it in
    if ((x >= 0) and (x < h_new-1) and (y >= 0) and (y < w_new-1)):
      A_next[x,y] = A1[i,j]


# A_next = np.matmul(R,A1)
cv2_imshow(A_next)


