import cv
import numpy as np
import matplotlib.pyplot as plt

# Load image in grayscale
image = cv.imread("image.png", cv.IMREAD_GRAYSCALE)

# Ensure image dimensions are divisible by 3 (crop if needed)
h, w = image.shape
h_new, w_new = (h // 3) * 3, (w // 3) * 3  # Find nearest multiple of 3
image = image[:h_new, :w_new]  # Crop excess pixels

# Function to apply explicit 3x3 max pooling
def max_pooling(img, pool_size=3):
    h, w = img.shape
    new_h, new_w = h // pool_size, w // pool_size
    pooled_image = np.zeros((new_h, new_w), dtype=np.uint8)

    for i in range(new_h):
        for j in range(new_w):
            pooled_image[i, j] = np.max(img[i*pool_size:(i+1)*pool_size, j*pool_size:(j+1)*pool_size])
    
    return pooled_image

# Apply 3x3 pooling
pooled_image = max_pooling(image)

# Save output image
cv2.imwrite("pooled_image.png", pooled_image)

# Display Original vs Pooled Image
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray', interpolation='nearest')

plt.subplot(1, 2, 2)
plt.title("3x3 Max Pooled Image")
plt.imshow(pooled_image, cmap='gray', interpolation='nearest')

plt.show()
