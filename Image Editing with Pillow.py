from PIL import Image

def edit_image(input_path, output_path):
    # Load the image
    with Image.open(input_path) as img:
        # Get image dimensions
        width, height = img.size
        
        # Calculate the left quarter width
        left_quarter = width // 4
        
        # Create a new image to modify
        img = img.copy()
        
        # Iterate over each pixel in the left quarter and set it to black
        for x in range(left_quarter):
            for y in range(height):
                img.putpixel((x, y), (0, 0, 0))  # Set pixel to black
        
        # Save the modified image
        img.save(output_path)
        print(f"Modified image saved to {output_path}")

# Example usage
input_image_path = "input.jpg"  # Replace with your image path
output_image_path = "output.jpg"  # Replace with desired output path
edit_image(input_image_path, output_image_path)