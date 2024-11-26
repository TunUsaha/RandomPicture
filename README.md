# pyFeats_Project_tool

This Python project extracts a `.tar` archive containing multiple subfolders of images, selects random images from each subfolder, splits the dataset into a training and validation set, and moves them into new destination folders while maintaining the subfolder structure.

## Features
- Extracts `.tar` archives.
- Handles images from nested subfolders.
- Selects random images from each subfolder.
- Splits images into training and validation sets (70:30).
- Maintains the subfolder structure in the destination folders for both training and validation sets.
- Allows users to adjust the number of images selected from each subfolder.

## Requirements
- Python 3.6 or higher
- The following Python libraries:
  - `os`
  - `random`
  - `shutil`
  - `tarfile`

## File Structure
```plaintext
project/
│
├── script.py          # Main Python script
├── README.md          # Documentation for the project
│
├── coffee.tar         # Input TAR archive (example)
│
├── coffee_extracted/  # Temporary folder for extracted contents
│   ├── folder1/
│   ├── folder2/
│   └── ...
│
├── coffee_extracted_train/  # Destination folder for training set
│   ├── folder1/
│   │   ├── random_image1.jpg
│   │   └── random_image2.jpg
│   ├── folder2/
│   └── ...
│
└── coffee_extracted_val/    # Destination folder for validation set
    ├── folder1/
    │   ├── random_image1.jpg
    │   └── random_image2.jpg
    ├── folder2/
    └── ...
```

## How to Use

1. **Setup Environment**
   - Ensure Python is installed on your system.
   - Place your `.tar` file (e.g., `coffee.tar`) in the project folder.

2. **Run the Script**
   - Update the paths for the `.tar` file and destination folders in the script:
     ```python
     tar_path = "path/to/your/coffee.tar"
     extracted_folder = "path/to/extracted/folder"
     train_folder = "path/to/coffee_extracted_train"
     val_folder = "path/to/coffee_extracted_val"
     ```
   - Run the script:
     ```bash
     python script.py
     ```

3. **Result**
   - Images from each subfolder will be selected randomly and split into two sets: 
     - 70% will be moved to the `coffee_extracted_train` folder.
     - 30% will be moved to the `coffee_extracted_val` folder.
   - The original subfolder structure will be maintained in both `train` and `val` folders.

4. **Optional: Adjust the Split Ratio**
   - You can adjust the ratio of the training and validation sets by modifying the `split_ratio` parameter in the script (default is 70:30).

## Example Output
After running the script, the `coffee_extracted_train` and `coffee_extracted_val` folders will look like this:

```plaintext
coffee_extracted_train/
├── folder1/
│   ├── random_image1.jpg
│   └── random_image2.jpg
├── folder2/
│   ├── random_image3.jpg
│   └── random_image4.jpg
└── ...

coffee_extracted_val/
├── folder1/
│   ├── random_image5.jpg
│   └── random_image6.jpg
├── folder2/
│   ├── random_image7.jpg
│   └── random_image8.jpg
└── ...
```

## Notes
- The number of images selected from each folder can be adjusted by modifying the `num_images` parameter in the script.
- The `.tar` file should contain only folders with images for optimal results.
- Ensure that the extracted images are organized in subfolders inside the `coffee_extracted` folder for proper processing.
