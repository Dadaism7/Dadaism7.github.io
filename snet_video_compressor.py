import os
import ffmpeg

# Source and destination directories
src_dir = '/Users/duanchenda/Downloads/scenarionet/nuplan-1'
dest_dir = src_dir+"-newcompressed"
base_name = "nuplan-1"
# Make sure the destination directory exists
os.makedirs(dest_dir, exist_ok=True)

# New id counter
new_id = 1

# Iterate through every file in source directory
for filename in os.listdir(src_dir):
    if filename.endswith('.mp4'):  # We're only interested in mp4 files
        # Source and destination paths
        src_path = os.path.join(src_dir, filename)

        # Remove old id from filename and add new id
        new_filename = f'{base_name}_{new_id}.mp4'  # Add new id to the base name
        dest_path = os.path.join(dest_dir, new_filename)

        # Load the video, resize it, compress it, and save it
        ffmpeg.input(src_path).output(dest_path, vf='scale=-1:720', vcodec='libx264', crf='42').run()

        # Increase the new id for the next file
        new_id += 1

