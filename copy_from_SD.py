# Author: VAkena (https://github.com/VAkena)
# Description: This script copies photos from your SD card to your local machine

import shutil
import re
import logging
import os

# Configure logging to file
logging.basicConfig(level=logging.DEBUG, filename="log.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - Line number: %(lineno)d - %(message)s', filemode='w')

# Only copy these two formats
COPY_IMAGES = re.compile(".*\.(JPG|ARW)")


def copy_files(src_dir, dest_dir):
    for dirpath, dirnames, filenames in os.walk(src_dir):
        for file_name in filenames:
            if COPY_IMAGES.match(file_name):
                src_path = os.path.join(dirpath, file_name)
                # Move all JPGs into a new subfolder
                if file_name.endswith(".JPG"):
                    dest_path = os.path.join(dest_dir, "JPGs", file_name)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                # Move all ARWs into a new subfolder
                elif file_name.endswith(".ARW"):
                    dest_path = os.path.join(dest_dir, "RAW", file_name)
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    logging.info(
                        "Successfully moved %s to Pictures on C Drive", file_name)
                shutil.copy2(src_path, dest_path)


# Only counts the RAW files found
def get_file_count(src_dir):
    count = 0
    for dirpath, dirnames, filenames in os.walk(src_dir):
        for file_name in filenames:
            if file_name.endswith(".ARW"):
                count += 1
                logging.info("Found %d RAW files", count)


def main():
    # SD Card root location - can be different depending on amount of drives connected
    source_dir = "D:\\"

    # Test destination
    destination_dir = "C:\\Users\\test\\Pictures\\test\\"
    copy_files(source_dir, destination_dir)

    # Scans the root directory of both JPG and RAW subfolders
    get_file_count(destination_dir)


if __name__ == "__main__":
    main()
