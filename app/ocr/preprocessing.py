import cv2
import numpy as np
import os

def enhance_image(image_path,doc_type):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Enhance the image using CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(image)
    
    # Denoise the image using median blur
    denoised_image = cv2.medianBlur(enhanced_image, 5)
    
    # Find the angle to rotate the image to correct any skew
    """coords = np.column_stack(np.where(denoised_image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    
    # Rotate the image to correct skew
    (h, w) = denoised_image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(denoised_image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    """
    # Define the processed image path
    processed_image_dir = f"processed_images\\{doc_type}"
    processed_image_name = "processed_" + os.path.basename(image_path)
    processed_image_path = os.path.join(processed_image_dir, processed_image_name)

    # Ensure the processed images directory exists
    if not os.path.exists(processed_image_dir):
        os.makedirs(processed_image_dir)

    # Save the processed image
    cv2.imwrite(processed_image_path, denoised_image)
    
    return processed_image_path
