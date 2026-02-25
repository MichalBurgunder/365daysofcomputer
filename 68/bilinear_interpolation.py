# BILINEAR INTERPOLATION

# This work was primarily taken from one of my assignments for my Master's
# degree, hence the difference in style. Given that code made much more sense when I wrote it many years ago, I have left it as is.
import cv2
import numpy as np
import math

def resize(image, x, y,fill):
  new_image = np.full((x,y), fill)
  o_x, o_y = image.shape[0], image.shape[1]

  for i in range(0,o_x):
    for j in range(0,o_y):
      new_image[i][j] = A1[i][j]

  return new_image

def translate_image(A1, x, y,fill):
  centered_image = np.full((A1.shape[0], A1.shape[1]), fill)

  for i in range(0, A1.shape[0]): # m1
    for j in range(0, A1.shape[1]): # N1
      nx = (i+x) % A1.shape[0]
      ny = (j+y) % A1.shape[1]
      centered_image[nx][ny] = A1[i][j] # centered_image[i+x][j+y] = A1[i][j]

  return centered_image


def ShearMAT(angle,rad=1):
  if rad==0 :
    theta = angle * np.pi/180
    lam=-np.tan(theta/2)
    mu=np.sin(theta)
  else:
    theta = angle
    lam=-np.tan(theta/2)
    mu=np.sin(theta)


  Sh = np.array([[1, lam], [0, 1]])
  Sv = np.array([[1, 0], [mu, 1] ])

  return Sh , Sv

def shear(image, shear_matrix,fill):
  x, y = image.shape[0], image.shape[1]

  raw_image = np.full((x,y,2), fill)
  new_image = np.full((x,y), fill)

  for i in range(x):
    for j in range(y):
       res = shear_matrix @ [[i], [j]]

       nx = round(res[0][0]) % x
       ny = round(res[1][0]) % y

       raw_image[i][j][0] = res[0][0]
       raw_image[i][j][1] = res[1][0]
       new_image[i][j] = image[nx][ny]
      #  new_image[i][j] = bilinear_interpolation(res, image, i, j, 1)

  return new_image, raw_image




def bilinear_interpolation(sheared_image, raw_image, direction,fill):
    new_image = np.full(sheared_image.shape, fill)

    if direction == 1: # up down
      u = 0
    else: # right left
      v = 0


    x, y = sheared_image.shape[0], sheared_image.shape[1]

    for i in range(x):
      for j in range(y):
        if direction == 1:
          v = raw_image[i][0][1] % 1
        else:
          u = raw_image[j][0][0] % 1


        a_up = 0 if i == 0 else sheared_image[i-1][j]
        a_down = 0 if i == x-1 else sheared_image[i+1][j]

        a_left = 0 if j == 0 else sheared_image[i][j-1]
        a_right = 0 if j == y-1 else sheared_image[i][j+1]



        p1vm1 = (1-v)*((1-u)*a_up)
        p2vm1 = (1-v)*(u*a_down)
        p1v = v*((1-u)*a_left)
        p2v = v*(u*a_right)

        new_image[i][j] = round(p1vm1 + p2vm1 + p1v + p2v)

    return new_image


# from google.colab.patches import cv2_imshow

A1 = cv2.imread("sushi.jpg", cv2.IMREAD_GRAYSCALE)
# print (np.shape(A1) )
# cv2_imshow(A1)

# # the original shape of the image
M1 = A1.shape[0]
N1 = A1.shape[1]

# # the shape of the new, resized image, to fit in the rotation
# M2= A1.shape[0]*2
# N2 = A1.shape[1]*2

# filling = 0
# A2 = resize(A1,M2,N2,filling)
# A3 = translate_image(A2,int(M1/2),int(N1/2),filling)

# Sh,Sv = ShearMAT(math.pi/6)

# #First Shear
# A4_shear1,A4_raw1 = shear(A3,Sh,fill=filling)
# A4_s1f = bilinear_interpolation(A4_shear1, A4_raw1, 1,filling)
#cv2_imshow(A4_s1f)

#Second Shear
# A4_shear2, A4_raw2 = shear(A4_shear1, Sv,fill=filling)
# Trans = translate_image(A4_shear2, -int(M2/4), int(M2/4),filling)
# A4_s2f = bilinear_interpolation(Trans, A4_raw2, 0,filling)
#cv2_imshow(A4_s2f)

#Third Shear
# A4_shear3, A4_raw3 = shear(A4_s2f, Sh,fill=filling)
# A4_s3f = bilinear_interpolation(A4_shear3, A4_raw3, 1,filling)
# cv2_imshow(A4_shear2)


# Set height and width of target image
A2 = np.zeros((M1*2,N1*2))
# Set default intensity to white
# A2[:,:] = 0

A3 = np.zeros((M1*2, N1*2))
# A3[:,:] = 0

# Translate image centre of A1 to origin
T1 = np.array(
[[1,0,-M1/2-27],
 [0,1,-N1/2-74],
 [0,0,1]])

# Rotate about origin by 25 degrees
theta = -math.pi/6
c = math.cos(theta)
s = math.sin(theta)
R = np.array(
[[c,-s, 0],
 [s, c, 0],
 [0, 0, 1]])

# Translate origin to image centre of A2
T2 = np.array(
[[1,0,M2/2],
 [0,1,N2/2],
 [0,0,1]])

# Transformation that rotates A1 by theta about its centre
# and maps to the centre of A2
A = np.matmul(T2,np.matmul(R,T1))

# Invert A
A = np.linalg.inv(A)

# Transformation with inverse mapping and bilinear interpolation
for i in range(0,M2):
  for j in range(0,N2):
    # coordinates of the (i,j)-th pixel in A2
    x = i + 0.5
    y = j + 0.5
    # convert to homegeneous coordinates
    p = np.array([x,y,1])
    # transform with matrix A
    q = np.matmul(A,p)
    # coordinates in A1
    x = q[0]
    y = q[1]
    # bilinear interpolation
    k = round(x) - 1
    l = round(y) - 1
    u = x - k - 0.5
    v = y - l - 0.5
    if ((k >= 0) and (k < M1-1) and (l >= 0) and (l < N1-1)):
      A3[i,j] = A1[k,l]
      A2[i,j] = round((1-v) * ( (1-u)*A1[k,l] + u*A1[k+1,l] ) + v*((1-u)*A1[k,l+1] + u*A1[k+1,l+1]))





