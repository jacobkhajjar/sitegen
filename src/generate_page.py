import os
from markdown_to_html import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    with open(from_path) as f:
        markdown = f.read()

    with open(template_path) as f:
        template = f.read()

    content = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", extract_title(markdown))
    template = template.replace("{{ Content }}", content)

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
