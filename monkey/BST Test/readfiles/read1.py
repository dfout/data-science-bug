import shutil
import os
import re

def copy_and_rename_pdfs(source_dir, destination_dir):
  """Copies PDFs from source to destination, renaming them."""

  for filename in os.listdir(source_dir):
    if filename.lower().endswith(".pdf"):
        source_path = os.path.join(source_dir, filename)
        
        # Example renaming logic (customize as needed)
        new_filename = re.sub(r"[^a-zA-Z0-9]", "_", filename)  # Replace non-alphanumeric with _
        new_filename = new_filename.lower() 
        destination_path = os.path.join(destination_dir, new_filename)

        try:
            shutil.copy2(source_path, destination_path)  # copy2 preserves metadata
            print(f"Copied and renamed: {filename} -> {new_filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")


if __name__ == "__main__":
  source_dir = "./source"
  destination_dir = "./destination"
  copy_and_rename_pdfs(source_dir, destination_dir)
