from PIL import Image, PngImagePlugin
import sys
import os
import shutil

def copy_pnginfo_and_image(source_path, target_path):
    # Extract the file base name and extension of the target image
    base, ext = os.path.splitext(target_path)
    # Define the output path for the new image with updated metadata
    output_path = f"{base}-pnginfo{ext}"

    # Open the source image to extract 'Parameters' metadata
    with Image.open(source_path) as source_img:
        source_info = source_img.info.get("parameters", None)
        # Check if 'Parameters' metadata is present in the source image
        if source_info is None:
            print(f"'Parameters' not found in {source_path}")
            return

    # Copy the binary data of the target image to the output file
    with open(target_path, 'rb') as target_file:
        with open(output_path, 'wb') as output_file:
            shutil.copyfileobj(target_file, output_file)

    # Update the metadata (Parameters) in the output file
    with Image.open(output_path) as output_img:
        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", source_info)
        output_img.save(output_path, "PNG", pnginfo=pnginfo)

    print(f"Updated the 'Parameters' metadata in {output_path}")

def main():
    if len(sys.argv) < 3:
        print("Usage: cppnginfo <source_path> <target_path>")
        sys.exit(1)

    # Get the source and target image paths from command-line arguments
    source_path = sys.argv[1]
    target_path = sys.argv[2]

    # Call the function to copy metadata and update the image
    copy_pnginfo_and_image(source_path, target_path)

if __name__ == '__main__':
    # Call the main function when the script is executed
    main()
