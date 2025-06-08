import os, shutil
from copy_static import copy_dir

root = os.getcwd()
short = len(root)
path_static = os.path.join(root, "static")
path_public = os.path.join(root, "public")
    

def main():
    if os.path.exists(f"{path_public}"):
        print(f"deleting old contents found in {path_public[short:]}")
        shutil.rmtree(f"{path_public}")
    os.mkdir(f"{path_public}")
    print(f"creating directory {path_public[short:]}")
    copy_dir(f"{path_static}", f"{path_public}")

main()