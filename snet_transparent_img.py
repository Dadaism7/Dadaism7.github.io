from PIL import Image

# specify image size
width = 1600
height = 450

# create new image with RGBA (including alpha transparency) mode
image = Image.new('RGBA', (width, height))

# save the image
image.save('transparent_image.png')
from moviepy.editor import ColorClip
from moviepy.video.io.ffmpeg_writer import FFMPEG_VideoWriter

clip = ColorClip((1600, 450), col=(0,0,0,0), duration=1)
fps=24

# Define codec and bitrate
codec = "libx264"
bitrate = "8000k"

with FFMPEG_VideoWriter("transparent_video.mp4", clip.size, fps, codec = codec, bitrate= bitrate) as writer:
    writer.write_frame(clip.make_frame(0))

print("Video file created: transparent_video.mp4")
