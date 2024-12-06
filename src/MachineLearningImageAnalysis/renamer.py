import os

def add_prefix_to_files(folder_path, prefix):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, f"{prefix}_{filename}")

            os.rename(old_path, new_path)

prefix = "1"
add_prefix_to_files("images", prefix)
add_prefix_to_files("labels", prefix)