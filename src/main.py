import os, shutil, pathlib, sys

from copy_static import copy_dir
from generate_pages import generate_page, generate_pages_recursive

basepath = sys.argv[0]
path_static = pathlib.Path("./static")
path_public = pathlib.Path("./docs")
path_content = pathlib.Path("./content")
path_template = pathlib.Path("./template.html")
    
def main():
    print("(~~~~ BUILDING PUBLIC DIRECTORY ~~~~)")
    if os.path.exists(f"{path_public}"):
        print(f"- deleting old contents found in {path_public}")
        shutil.rmtree(path_public)
    os.mkdir(path_public)
    print(f"- creating directory {path_public}")
    
    print("(~~~~ COPYING STATIC FILES ~~~~)")
    copy_dir(f"{path_static}", f"{path_public}")

    print("(~~~~ GENERATING PAGES ~~~~)")
    generate_pages_recursive(path_content, path_template, path_public, basepath)

    print("(~~~~ PUSHING TO SERVER PORT 8888 ~~~~)")
    print(f"basepath: {basepath}")
    
main()