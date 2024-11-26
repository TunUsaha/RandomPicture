import cv2
import os
import glob
import numpy as np
import random
from shutil import copyfile

# Define the path to your dataset folder
dataset_path = r"C:\652110109\Year3\pyFeats\coffee_extracted_train"


# Create a function to perform random image augmentations
def random_flip(img):
    """Randomly flip the image horizontally or vertically."""
    if random.random() > 0.5:
        img = cv2.flip(img, 0)  # Flip vertically
    if random.random() > 0.5:
        img = cv2.flip(img, 1)  # Flip horizontally
    return img


def random_rotation(img):
    """Randomly rotate the image."""
    angle = random.randint(-30, 30)  # Random angle between -30 and 30 degrees
    (h, w) = img.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_img = cv2.warpAffine(img, rotation_matrix, (w, h))
    return rotated_img


def adjust_brightness(img):
    """Randomly adjust the brightness of the image."""
    factor = random.uniform(0.5, 1.5)  # Random factor between 0.5 and 1.5
    img = cv2.convertScaleAbs(img, alpha=factor, beta=0)
    return img


def random_crop(img, target_size=(500, 500)):
    """Randomly crop the image to the target size."""
    h, w = img.shape[:2]
    crop_h, crop_w = target_size
    x = random.randint(0, w - crop_w)
    y = random.randint(0, h - crop_h)
    cropped_img = img[y:y + crop_h, x:x + crop_w]
    return cropped_img


def augment_image(img):
    """Apply random augmentation to the image."""
    img = random_flip(img)
    img = random_rotation(img)
    img = adjust_brightness(img)
    img = random_crop(img)
    return img


# Iterate through each class folder
class_folders = sorted(
    [os.path.join(dataset_path, d) for d in os.listdir(dataset_path) if os.path.isdir(os.path.join(dataset_path, d))])

# Iterate through each class folder and perform augmentation
for class_folder in class_folders:
    class_name = os.path.basename(class_folder)
    augmented_folder = f"{class_folder}_augmentation"

    # Create a new folder to store augmented images
    if not os.path.exists(augmented_folder):
        os.makedirs(augmented_folder)

    # Get all image files in the current class folder
    image_files = sorted(glob.glob(os.path.join(class_folder, "*")))

    for image_file in image_files:
        # Read the image
        img = cv2.imread(image_file)

        if img is not None:
            # Perform augmentation
            augmented_img = augment_image(img)

            # Save the augmented image to the new folder
            base_name = os.path.basename(image_file)
            augmented_image_path = os.path.join(augmented_folder, base_name)
            cv2.imwrite(augmented_image_path, augmented_img)

            # Optional: Save the original image in the augmented folder as well (if needed)
            # copyfile(image_file, augmented_image_path)

print("Augmentation completed successfully!")
