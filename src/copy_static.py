import os, shutil

def copy_dir(source, destination):
    for item in os.listdir(source):
        path_source = os.path.join(source, item)
        path_destination = os.path.join(destination, item)
        if os.path.isfile(path_source):
            print(f"- copying file: {path_source}")
            shutil.copy(path_source, destination)
        else:
            print(f"- copying directory: {path_source}")
            os.mkdir(f"{path_destination}")
            copy_dir(path_source, path_destination)