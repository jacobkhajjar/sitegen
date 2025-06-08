import os, shutil

from copy_static import copy_dir
from generate_page import generate_page

root = os.getcwd()
short = len(root)

path_static = os.path.join(root, "static")
path_public = os.path.join(root, "public")

from_path = os.path.join(root, "content", "index.md")
template_path = os.path.join(root, "template.html")
dest_path = os.path.join(root, "public", "index.html")
    

def main():
    print("(~~~~ COPYING STATIC FILES ~~~~)")
    if os.path.exists(f"{path_public}"):
        print(f"deleting old contents found in {path_public[short:]}")
        shutil.rmtree(f"{path_public}")
    os.mkdir(f"{path_public}")
    print(f"creating directory {path_public[short:]}")
    copy_dir(f"{path_static}", f"{path_public}")

    print("(~~~~ GENERATING PAGE ~~~~)")
    print(f"Generating page from {from_path[short:]} to {dest_path[short:]} using {template_path[short:]}:")
    generate_page(from_path, template_path, dest_path)
    

main()