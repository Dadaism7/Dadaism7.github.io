import os
import urllib.parse


directories = ["assets/scenarionet/nuplan-1-compressed/",]
src_prepend = "https://github.com/Dadaism6/metadriverse-asset/releases/download/assetsv1.0.1/"

# Ensure _images directory exists
os.makedirs('_snet-asset', exist_ok=True)

for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mp4')):
                # src = "/" + os.path.join(root, file) 
                src = file
                alt = os.path.splitext(file)[0]  # Use the filename without extension as alt text
                filename = os.path.splitext(file)[0] + '.md'  # Markdown filename

                # Create Markdown file in _images directory
                with open(os.path.join('_snet-asset', filename), 'w') as f:
                    f.write(f'---\nsrc: {src_prepend}{src}\nalt: {alt}\n---\n')



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
