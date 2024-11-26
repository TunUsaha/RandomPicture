# Random Image Selector from TAR Archive

This Python project extracts a `.tar` archive containing multiple subfolders of images, selects 10 random images from each subfolder, and moves them into a new destination folder while maintaining the subfolder structure.

## Features
- Extracts `.tar` archives.
- Handles images from nested subfolders.
- Selects 10 random images from each subfolder.
- Maintains the subfolder structure in the destination folder.

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
└── coffee_test/       # Destination folder for selected images
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
     destination_folder = "path/to/destination/folder"
     ```
   - Run the script:
     ```bash
     python script.py
     ```

3. **Result**
   - Images from each subfolder will be selected randomly and moved to the `destination_folder` folder, maintaining the original subfolder structure.

## Example Output
After running the script, the `coffee_test` folder will look like this:
```plaintext
coffee_test/
├── folder1/
│   ├── random_image1.jpg
│   └── random_image2.jpg
├── folder2/
│   ├── random_image3.jpg
│   └── random_image4.jpg
└── ...
```

## Notes
- The number of images selected from each folder can be adjusted by modifying the `num_images` parameter in the script.
- Ensure the `.tar` file contains only folders with images for optimal results.

