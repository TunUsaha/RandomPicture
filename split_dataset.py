import os
import shutil
import random

# Define the base directory for train data
train_dir = r"C:\652110109\Year3\pyFeats\coffee_extracted"

# Define the target directories for train and val data
train_split_dir = os.path.join(train_dir, "coffee_extracted_train")
val_split_dir = os.path.join(train_dir, "coffee_extracted_val")

# Create the new directories if they don't exist
os.makedirs(train_split_dir, exist_ok=True)
os.makedirs(val_split_dir, exist_ok=True)

# Loop through each class directory in the training data
for class_folder in os.listdir(train_dir):
    class_path = os.path.join(train_dir, class_folder)

    if os.path.isdir(class_path):
        # Create corresponding train and val subdirectories
        train_class_dir = os.path.join(train_split_dir, class_folder)
        val_class_dir = os.path.join(val_split_dir, class_folder)
        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(val_class_dir, exist_ok=True)

        # Get a list of all image files in the class folder
        image_files = [f for f in os.listdir(class_path) if os.path.isfile(os.path.join(class_path, f))]

        # Shuffle the files to get a random split
        random.shuffle(image_files)

        # Calculate the split index (70% train, 30% val)
        split_index = int(0.7 * len(image_files))

        # Get the files for train and validation
        train_files = image_files[:split_index]
        val_files = image_files[split_index:]

        # Move the train files to the corresponding train subdirectory
        for file in train_files:
            shutil.move(os.path.join(class_path, file), os.path.join(train_class_dir, file))

        # Move the val files to the corresponding val subdirectory
        for file in val_files:
            shutil.move(os.path.join(class_path, file), os.path.join(val_class_dir, file))

print("Data split completed!")
