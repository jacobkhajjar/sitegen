import os
from pathlib import Path
from markdown_to_html import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    files = os.listdir(dir_path_content)
    for f in files:
        dir_path = os.path.join(dir_path_content, f)
        destination = os.path.join(dest_dir_path, f)
        if os.path.isfile(dir_path) and f[-3:] == ".md":
            destination = Path(destination).with_suffix(".html")
            print(f"- generating page {dir_path} -> {destination} using {template_path}")
            generate_page(dir_path, template_path, destination)
        elif os.path.isdir(dir_path):
            generate_pages_recursive(dir_path, template_path, destination, basepath)

def generate_page(from_path, template_path, dest_path, basepath="/"):
    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    content = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", extract_title(markdown))
    template = template.replace("{{ Content }}", content)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as f:
        f.write(template)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.lstrip("#").strip()
    raise ValueError("no valid heading in source md file")