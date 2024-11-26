# pyFeats Tool

**pyFeats** is a set of Python scripts designed to assist in processing and managing image datasets, specifically for tasks like splitting datasets, moving image files, and performing data augmentation. This tool is helpful for organizing and preparing datasets for training machine learning models, especially in image classification tasks.

## Components

This tool consists of the following Python scripts:

- **move_images.py**: A script for moving images from one folder to another based on specific conditions or directories.
- **split_dataset.py**: A script for splitting a dataset into training and validation sets with a specified ratio.
- **augmentation.py**: A script for performing image augmentation (rotation, flipping, zooming, etc.) to increase the size of a dataset for training.

## Features

### 1. `move_images.py`
- Moves images from one folder to another based on specified criteria (e.g., class-based folders).
- Maintains folder structure when moving images.
- Useful for organizing datasets before performing augmentation or splitting.

### 2. `split_dataset.py`
- Splits dataset into two parts: training and validation sets.
- Maintains class distribution when splitting the dataset (70:30 ratio, by default).
- Outputs separate folders for training and validation sets to facilitate model training and evaluation.

### 3. `augmentation.py`
- Performs data augmentation on the images in the dataset.
- Includes various augmentation techniques such as rotation, zoom, flipping, etc.
- Increases the size and diversity of the dataset for model training.

## Requirements

- Python 3.x or higher
- The following Python libraries:
  - `opencv-python`
  - `numpy`
  - `glob`
  - `os`
  - `shutil`
  - `keras` (for image augmentation)

You can install the required libraries with the following command:

```bash
pip install opencv-python numpy glob2 shutil keras
```

## File Structure

```plaintext
pyFeats/
│
├── move_images.py      # Script to move images based on directory structure
├── split_dataset.py    # Script to split dataset into train and validation sets
├── augmentation.py     # Script to augment images for training
├── README.md           # Documentation for the project
│
├── your_dataset/   # Folder containing the dataset (example)
│   ├── class1/
│   ├── class2/
│   └── ...
└── your_dataset_train/  # Folder containing training data
└── your_dataset_val/    # Folder containing validation data
└── your_dataset_augmentation/  # Folder containing augmented data
```

## How to Use

### 1. `move_images.py`

This script helps you organize and move images between folders.

- **Input**: The path to the source folder and destination folder.
- **Usage**:
  ```bash
  python move_images.py --source /path/to/source/folder --destination /path/to/destination/folder
  ```

### 2. `split_dataset.py`

This script splits your dataset into training and validation sets, maintaining the class distribution.

- **Input**: The path to the dataset folder, the output path, and the split ratio.
- **Usage**:
  ```bash
  python split_dataset.py --dataset /path/to/dataset --output /path/to/output --split_ratio 0.7
  ```

### 3. `augmentation.py`

This script applies augmentation techniques to your images to increase dataset size for model training.

- **Input**: The path to the dataset folder to be augmented.
- **Usage**:
  ```bash
  python augmentation.py --dataset /path/to/dataset --output /path/to/output
  ```

## Example Workflow

1. **Organize images**:
   - Use `move_images.py` to organize images into folders based on class (if needed).
2. **Split dataset**:
   - Use `split_dataset.py` to create separate training and validation datasets.
3. **Augment dataset**:
   - Use `augmentation.py` to generate augmented images for your training set.

## Notes

- The scripts expect the dataset to be organized into class-based subfolders (e.g., `class1`, `class2`, etc.).
- Augmentation techniques can be customized in the `augmentation.py` script if needed.
- The dataset paths in the scripts should be modified to point to the correct directories on your machine or cloud environment.
