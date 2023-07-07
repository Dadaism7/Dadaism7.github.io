import os
import urllib.parse

directories = ["assets/scenarionet/script-waymo-output-newcompressed/", "assets/scenarionet/script-nuplan-output-newcompressed/"]
src_prepend = {
    "assets/scenarionet/script-waymo-output-newcompressed/": "https://github.com/Dadaism6/metadriverse-asset/releases/download/assetsv1.0.3/",
    "assets/scenarionet/script-nuplan-output-newcompressed/": "https://github.com/Dadaism6/metadriverse-asset/releases/download/assetsv1.0.4/"
}

# Ensure _images directory exists
os.makedirs('_snet-asset', exist_ok=True)

# Create a dictionary to store the current order for each directory
orders = {}
for directory in directories:
    orders[directory] = 0

for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.mp4')):
                # src = "/" + os.path.join(root, file)
                src = file
                alt = os.path.splitext(file)[0]  # Use the filename without extension as alt text
                filename = os.path.splitext(file)[0] + '.md'  # Markdown filename

                # Split the filename into tag and id
                split_name = os.path.splitext(file)[0].split("_")
                tag = split_name[0]
                video_id = split_name[1]

                # Create Markdown file in _images directory
                with open(os.path.join('_snet-asset', filename), 'w') as f:
                    f.write(f'---\nsrc: {src_prepend[directory]}{src}\nalt: {alt}\ntag: {tag}\nvid: {video_id}\norder: {orders[directory]}\n---\n')

                # Increase the order by the number of directories
                orders[directory] += len(directories)




# directories = ["assets/scenarionet/nuplan-1-newcompressed/", "assets/scenarionet/nuplan-2-newcompressed/", "assets/scenarionet/waymo-1-newcompressed/","assets/scenarionet/waymo-2-newcompressed/"]
# src_prepend = "https://github.com/Dadaism6/metadriverse-asset/releases/download/assetsv1.0.2/"

# # Ensure _images directory exists
# os.makedirs('_snet-asset', exist_ok=True)

# for directory in directories:
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.lower().endswith(('.mp4')):
#                 # src = "/" + os.path.join(root, file) 
#                 src = file
#                 alt = os.path.splitext(file)[0]  # Use the filename without extension as alt text
#                 filename = os.path.splitext(file)[0] + '.md'  # Markdown filename
                
#                 # Split the filename into tag and id
#                 split_name = os.path.splitext(file)[0].split("_") 
#                 tag = split_name[0]
#                 video_id = split_name[1]

#                 # Create Markdown file in _images directory
#                 with open(os.path.join('_snet-asset', filename), 'w') as f:
#                     f.write(f'---\nsrc: {src_prepend}{src}\nalt: {alt}\ntag: {tag}\nvid: {video_id}\n---\n')



# directories = ["assets/scenarionet/nuplan-1-compressed/", "assets/scenarionet/nuplan-2-compressed/", "assets/scenarionet/waymo-1-compressed/","assets/scenarionet/waymo-2-compressed/"]
# src_prepend = "https://github.com/Dadaism6/metadriverse-asset/releases/download/assetsv1.0.1/"

# # Ensure _images directory exists
# os.makedirs('_snet-asset', exist_ok=True)

# for directory in directories:
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.lower().endswith(('.mp4')):
#                 # src = "/" + os.path.join(root, file) 
#                 src = file
#                 alt = os.path.splitext(file)[0]  # Use the filename without extension as alt text
#                 filename = os.path.splitext(file)[0] + '.md'  # Markdown filename

#                 # Create Markdown file in _images directory
#                 with open(os.path.join('_snet-asset', filename), 'w') as f:
#                     f.write(f'---\nsrc: {src_prepend}{src}\nalt: {alt}\n---\n')



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
