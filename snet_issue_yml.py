import os
os.makedirs('_snet-asset', exist_ok=True)
def create_markdown_files(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        
    for i, link in enumerate(lines):
        if len(link) != 0:
            md_content = f"""---
src: {link}
alt: asset-{i+1}
---"""
            with open(os.path.join('_snet-asset', f'asset-{i+1}.md'), 'w') as md_file:
                md_file.write(md_content)

# Run the function with your filename
create_markdown_files("issuelink.txt")




# # List of directories to scan for images
# directories = ["assets/scenarionet/nuplan-1-compressed/", "assets/scenarionet/nuplan-2-compressed/", "assets/scenarionet/waymo-1-compressed/","assets/scenarionet/waymo-2-compressed/"]
# # src_prepend = "https://github.com/Dadaism6/metadriverse-asset/raw/main/"

# # Ensure _images directory exists
# os.makedirs('_snet-asset', exist_ok=True)

# for directory in directories:
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.lower().endswith(('.mp4')):
#                 src = "/" + os.path.join(root, file) 
#                 alt = os.path.splitext(file)[0]  # Use the filename without extension as alt text
#                 filename = os.path.splitext(file)[0] + '.md'  # Markdown filename

#                 # Create Markdown file in _images directory
#                 with open(os.path.join('_snet-asset', filename), 'w') as f:
#                     f.write(f'---\nsrc: {src}\nalt: {alt}\n---\n')
