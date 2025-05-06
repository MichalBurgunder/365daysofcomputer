import cv2
import numpy as np

def apply_color_filter(image_path, output_path, the_filter):
    # Load the image
    image = cv2.imread(image_path)

    # Apply the filter
    filtered_image = cv2.transform(image, the_filter)
    # Save the output image
    cv2.imwrite(output_path, filtered_image)

matrix_filter = np.array([[0.8946, 0, 0], # blue
                              [0, 1.27, 0], # green
                              [0, 0, 0.8946]]) # red
# matrix_filter = np.array([[0.63, 0, 0], # blue
#                               [0, 0.85, 0], # green
#                               [0, 0, 0.63]]) # red

mexico_filter = np.array([[0.7, 0, 0], # blue
                              [0, 1.3, 0], # green
                              [0, 0, 1.6]]) # red

# Example usage
apply_color_filter("vierwaldstättersee.jpg", "mexico_vierwaldstättersee.jpg", mexico_filter)
apply_color_filter('city.jpg', 'matrix_city.jpg', matrix_filter)