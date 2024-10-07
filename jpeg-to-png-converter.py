from PIL import Image
import os

def is_jpeg(file_path):
    """Check if the file is a JPEG image."""
    try:
        # Check file extension
        if not file_path.lower().endswith(('.jpg', '.jpeg')):
            return False
        
        # Try to open the image to verify it's a valid JPEG
        with Image.open(file_path) as img:
            return img.format == 'JPEG'
    except Exception:
        return False

def convert_jpeg_to_png(input_path, output_path):
    """Convert JPEG image to PNG format."""
    try:
        with Image.open(input_path) as img:
            img.save(output_path, 'PNG')
        return True
    except Exception as e:
        print(f"Conversion error: {str(e)}")
        return False

def main():
    print("JPEG to PNG Converter")
    print("--------------------")
    
    while True:
        # Get input file path
        input_path = input("\nEnter the path to your JPEG file (or 'q' to quit): ")
        
        if input_path.lower() == 'q':
            print("Goodbye!")
            break
        
        # Check if file is a valid JPEG
        if not is_jpeg(input_path):
            print("Error: The file is not a valid JPEG image. Please try again.")
            continue
        
        # Generate output path
        output_path = os.path.splitext(input_path)[0] + '.png'
        
        print("Converting JPEG to PNG...")
        
        # Convert image
        if convert_jpeg_to_png(input_path, output_path):
            print(f"Conversion successful! PNG image saved as: {output_path}")
        else:
            print("Error: Conversion failed. Please try again with a different image.")

if __name__ == "__main__":
    main()
