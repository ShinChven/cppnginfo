#!/bin/bash

# this bash script is used to auto fix the png~ files created by Krita

# Function to process a single file
process_file() {
    local SOURCE_FILE="$1"

    # Check if the source file ends with .png~
    if [[ ! "$SOURCE_FILE" =~ \.png~$ ]]; then
        echo "Error: Source file '$SOURCE_FILE' does not have the correct extension (.png~)."
        return
    fi

    # Derive the target file path by removing the ~ before .png~
    local TARGET_FILE="${SOURCE_FILE/.png~/.png}"

    # Print source and target file paths for debugging
    echo "Source: $SOURCE_FILE"
    echo "Target: $TARGET_FILE"

    # Run the custom command
    cppnginfo "$SOURCE_FILE" "$TARGET_FILE"
}

# Check if the user provided an input
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <source_image.png~ or directory>"
    exit 1
fi

INPUT="$1"

if [ -d "$INPUT" ]; then
    # Input is a directory
    find "$INPUT" -type f -name "*.png~" | while read -r file; do
        process_file "$file"
    done
elif [ -f "$INPUT" ]; then
    # Input is a single file
    process_file "$INPUT"
else
    echo "Error: Provided path is neither a valid .png~ file nor a directory."
    exit 1
fi
