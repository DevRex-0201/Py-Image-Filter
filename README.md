# Image Filter Processing Project

## Project Overview

This project utilizes the Python Imaging Library (PIL) to perform image processing tasks. The main functionality includes cutting out objects from images and replacing the gray background with transparency. The project is designed to process all images in a specified directory, making them suitable for applications that require images with transparent backgrounds.

## Requirements

- Python 3.x
- Pillow (PIL fork, supports image processing)

## Setup

1. **Install Dependencies:**
    ```bash
    pip install Pillow
    ```

2. **Image Files:**
    - Place the images you want to process in the "input" directory.

## Running the Script

1. **Run the Script:**
    ```bash
    python script.py
    ```
    The script will process all `.jpg` images in the "input" directory and save the edited images in the same directory with the prefix "edited_".

## Customization

- **Threshold Values:**
    - Adjust the threshold values in the `cut_out_object` function based on the specific color of the background in your images.

- **File Format:**
    - The script is currently set to process `.jpg` files. If your images are in a different format, update the `if filename.endswith(".jpg"):` condition in the `process_images` function.

## Notes

- Ensure that the input images have a gray background for effective processing. Adjust threshold values accordingly.

- The script assumes that the images in the "input" directory are in the JPEG format. Modify the script if your images have a different format.

- This project is a simple example of image processing and can be extended for more complex tasks based on your specific requirements.
