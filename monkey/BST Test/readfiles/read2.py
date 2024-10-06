import shutil
import os
import re

source_dir = "./source"
destination_dir = "./destination"

for filename in os.listdir(source_dir):
    if filename.endswith(".pdf"):
        # Apply filename changes (example: replace spaces with underscores)
        new_filename = re.sub(r"\s+", "_", filename)

        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, new_filename)

        shutil.copy2(source_path, destination_path)  # copy2 preserves metadata 