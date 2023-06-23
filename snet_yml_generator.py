import os
import urllib.parse

# List of directories to scan for images
directories = ["assets/scenarionet/nuplan-1-compressed/", "assets/scenarionet/nuplan-2-compressed/", "assets/scenarionet/waymo-1-compressed/","assets/scenarionet/waymo-2-compressed/"]
# src_prepend = "https://github.com/Dadaism6/metadriverse-asset/raw/main/"

# Ensure _images directory exists
os.makedirs('_snet-asset', exist_ok=True)

for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mp4')):
                src = "/" + os.path.join(root, file) 
                alt = os.path.splitext(file)[0]  # Use the filename without extension as alt text
                filename = os.path.splitext(file)[0] + '.md'  # Markdown filename

                # Create Markdown file in _images directory
                with open(os.path.join('_snet-asset', filename), 'w') as f:
                    f.write(f'---\nsrc: {src}\nalt: {alt}\n---\n')





# # List of directories to scan for images
# directories = ["/Users/duanchenda/Downloads/scenarionet/nuplan-1/"]
# # src_prepend = "https://github.com/Dadaism6/metadriverse-asset/raw/main/"

# # Ensure _images directory exists
# os.makedirs('_images', exist_ok=True)

# for directory in directories:
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.lower().endswith(('.mp4')):
#                 src = urllib.parse.quote(file)  # URL-encode the filename
#                 alt = os.path.splitext(file)[0]  # Use the filename without extension as alt text
#                 filename = os.path.splitext(file)[0] + '.md'  # Markdown filename

#                 # Create Markdown file in _images directory
#                 with open(os.path.join('_images', filename), 'w') as f:
#                     f.write(f'---\nsrc: {src_prepend}{src}\nalt: {alt}\n---\n')


# # List of directories to scan for images
# directories = ["/Users/duanchenda/Downloads/scenarionet/nuplan-1/"]

# # Ensure _images directory exists
# os.makedirs('_images', exist_ok=True)

# for directory in directories:
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
#                 src = "/" + os.path.join(root, file) 
#                 alt = os.path.splitext(file)[0]  # Use the filename without extension as alt text
#                 filename = os.path.splitext(file)[0] + '.md'  # Markdown filename

#                 # Create Markdown file in _images directory
#                 with open(os.path.join('_images', filename), 'w') as f:
#                     f.write(f'---\nsrc: {src}\nalt: {alt}\n---\n')

# import os
# import yaml

# # List the folders you want to scan for images
# rootDirs = ["assets/img/nuplan/new", 
#            "assets/img/pg/new", 
#            "assets/img/waymo/new"]

# images = []

# for rootDir in rootDirs:
#     for dirName, subdirList, fileList in os.walk(rootDir):
#         for fname in fileList:
#             # check if file is an image by its extension
#             if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
#                 # construct the full path
#                 fullPath = os.path.join(dirName, fname)
#                 # append the image to the list
#                 images.append({
#                     'src': fullPath,
#                     'alt': fname
#                 })

# # write the list to a YAML file
# with open('images.yml', 'w') as outfile:
#     yaml.dump(images, outfile, default_flow_style=False)
