from PIL import Image

# Function to cut out the object and replace the gray background
def cut_out_object(image_path, output_path):
    image = Image.open(image_path)
    image = image.convert("RGB")  # Convert to RGBA to support transparency
    
    # Loop through each pixel and modify the gray background
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            if r > 120 and g > 100 and b > 100:  # Adjust the threshold values as per your images
                image.putpixel((x, y), (255, 255, 255, 0))  # Make gray pixels transparent
            else:
                image.putpixel((x, y), (r, g, b, 255))  # Keep other pixels as they are
    
    # Save the edited image
    image.save(output_path)

# Process all the images in the directory
def process_images(directory):
    import os
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            image_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, "edited_" + filename)
            cut_out_object(image_path, output_path)

# Call the function to process the images in the directory
process_images("input")