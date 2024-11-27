import os
import cv2
import numpy as np
from tqdm import tqdm
from albumentations import (
    Compose, HorizontalFlip, VerticalFlip, RandomRotate90, ShiftScaleRotate,
    RandomBrightnessContrast, HueSaturationValue, CLAHE
)
from albumentations.core.transforms_interface import ImageOnlyTransform


# Create a ToRGB class for converting images to RGB.
class ToRGB(ImageOnlyTransform):
    def __init__(self, always_apply=False, p=0.5):
        super(ToRGB, self).__init__(always_apply=always_apply, p=p)

    def apply(self, img, **params):
        if len(img.shape) == 2 or img.shape[2] != 3: # Check if it is grayscale or not RGB
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        return img



# Functions for augmentation
def augment_image(image):
    augmentations = Compose([
        HorizontalFlip(p=0.5),
        VerticalFlip(p=0.5),
        RandomRotate90(p=0.5),
        ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1, rotate_limit=25, p=0.5),
        RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.5),
        HueSaturationValue(hue_shift_limit=10, sat_shift_limit=10, val_shift_limit=10, p=0.5),
        CLAHE(clip_limit=2.0, tile_grid_size=(8, 8), p=0.5),
        ToRGB(p=0.3)  # Add ToRGB and randomly change the image color to RGB.
    ])
    augmented = augmentations(image=image)
    return augmented['image']


# The main function is for adding images to each folder.
def balance_dataset(data_dir, target_count=100):
    for class_folder in tqdm(os.listdir(data_dir), desc="Processing classes"):
        class_path = os.path.join(data_dir, class_folder)
        if not os.path.isdir(class_path):
            continue

        images = [os.path.join(class_path, f) for f in os.listdir(class_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
        image_count = len(images)

        if image_count >= target_count:
            print(f"Class {class_folder} already has {image_count} images.")
            continue

        # Add photos until the desired number is reached.
        while image_count < target_count:
            for img_path in images:
                if image_count >= target_count:
                    break

                # Load images
                image = cv2.imread(img_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                # augmentation
                augmented_image = augment_image(image)

                # Save the augmented image
                save_path = os.path.join(class_path, f"aug_{image_count}.jpg")
                augmented_image = cv2.cvtColor(augmented_image, cv2.COLOR_RGB2BGR)
                cv2.imwrite(save_path, augmented_image)
                image_count += 1


# Set the path of the dataset.
dataset_path = "C:/652110109/Year3/coffee_train"

# call function
balance_dataset(dataset_path, target_count=100)
