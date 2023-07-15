import os
import re

# the path to the directories containing your mp4 files
directories = [
    "assets/scenarionet/script-waymo-output-newcompressed/",
    "assets/scenarionet/script-nuplan-output-newcompressed/"
]

# the paths to your text files containing links
links_files_paths = {
    "assets/scenarionet/script-waymo-output-newcompressed/": "/Users/duanchenda/Desktop/gitplay/Dadaism7.github.io/issuelink_waymo.txt",
    "assets/scenarionet/script-nuplan-output-newcompressed/": "/Users/duanchenda/Desktop/gitplay/Dadaism7.github.io/issuelink_nuplan.txt"
}
# regex pattern for extracting the id from the filename
pattern = re.compile(r"(\w+)_(\d+)\.mp4")

# Ensure _images directory exists
os.makedirs('_snet-asset', exist_ok=True)

# Create a dictionary to store the current order for each directory
orders = {directory: 0 for directory in directories}

for directory in directories:
    print("For dir {}".format(directory))
    # read all links into a list, skipping blank lines
    with open(links_files_paths[directory], 'r') as file:
        links = [line.strip() for line in file if line.strip() != '']

    # create a dictionary where keys are the ids and values are the filenames
    video_files = {}
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            tag, id = match.groups()
            video_files[int(id)] = os.path.join(directory, filename)

    # sort video_files by id
    video_files = dict(sorted(video_files.items()))

    # ensure the number of links matches the number of videos
    if len(links) != len(video_files):
        print(f"Error: the number of links ({len(links)}) does not match the number of videos ({len(video_files)}).")
        exit(1)

    for i, (id, file_path) in enumerate(video_files.items()):
        filename = os.path.basename(file_path)
        alt = os.path.splitext(filename)[0]  # Use the filename without extension as alt text
        md_filename = alt + '.md'  # Markdown filename

        # Create Markdown file in _snet-asset directory
        with open(os.path.join('_snet-asset', md_filename), 'w') as f:
            f.write(f'---\nsrc: {links[i]}\nalt: {alt}\ntag: {tag}\nvid: {id}\norder: {orders[directory]}\n---\n')

        # Increase the order by the number of directories
        orders[directory] += len(directories)





# import os
# os.makedirs('_snet-asset', exist_ok=True)
# def create_markdown_files(filename):
#     with open(filename, 'r') as f:
#         lines = f.read().splitlines()
        
#     for i, link in enumerate(lines):
#         if len(link) != 0:
#             md_content = f"""---
# src: {link}
# alt: asset-{i+1}
# ---"""
#             with open(os.path.join('_snet-asset', f'asset-{i+1}.md'), 'w') as md_file:
#                 md_file.write(md_content)

# # Run the function with your filename
# create_markdown_files("issuelink.txt")




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
