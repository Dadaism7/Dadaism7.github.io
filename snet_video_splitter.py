import cv2
import numpy as np
import os

def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])
    return err

def downsample(image, scale_percent = 30):  # Decrease the scale_percent
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

# your video file
video_file = 'videos/waymo/MetaDrive v0.3.0.1 2023-06-15 12-38-14.mp4'

# Open the video file
cap = cv2.VideoCapture(video_file)

# Get the frame rate
fps = cap.get(cv2.CAP_PROP_FPS)

# The duration in seconds for which the last frame of each small video doesn't change
last_frame_duration = 20  # Increase the last_frame_duration

# The number of frames for which the last frame of each small video doesn't change
frame_change = int(last_frame_duration * fps)

frame_count = 0
is_same_frame = False
last_frame = None

# Create directory to save the small videos if it doesn't exist
if not os.path.exists("small_videos"):
    os.makedirs("small_videos")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("small_videos/output_0.mp4", fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break

    frame_downsampled = downsample(frame)

    if last_frame is not None:
        if mse(frame_downsampled, last_frame) < 50:  # Increase the threshold for MSE
            if not is_same_frame:
                frame_count = 0
                is_same_frame = True
        else:
            if is_same_frame and frame_count >= frame_change:
                is_same_frame = False
                out.release()
                out = cv2.VideoWriter(f"small_videos/output_{int(cap.get(cv2.CAP_PROP_POS_FRAMES))}.mp4", fourcc, fps, (int(cap.get(3)), int(cap.get(4))))
            out.write(frame)

    last_frame = frame_downsampled
    if is_same_frame:
        frame_count += 1

cap.release()
out.release()
cv2.destroyAllWindows()





# def cut_video_segment(input_video, start_time, end_time, output_video):
#     command = ['ffmpeg', '-i', input_video, '-ss', str(start_time), '-to', str(end_time), '-c', 'copy', output_video]
#     subprocess.run(command)

# def get_segments(input_video, similarity_threshold=0.99, freeze_frame_threshold=90, min_segment_length=1.0):
#     cap = cv2.VideoCapture(input_video)
    
#     if not cap.isOpened():
#         print(f"Failed to open the video file: {input_video}")
#         return []

#     fps = cap.get(cv2.CAP_PROP_FPS)
#     print(f"Video FPS: {fps}")

#     last_frame = None
#     freeze_frames = 0
#     segments = []
#     start_time = 0.0
#     freeze_flag = False

#     while(cap.isOpened()):
#         ret, frame = cap.read()
#         if not ret:
#             break

#         gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

#         if last_frame is not None:
#             similarity = np.sum(gray_frame == last_frame) / (gray_frame.shape[0] * gray_frame.shape[1])

#             if similarity > similarity_threshold:
#                 freeze_frames += 1
#                 if freeze_frames > freeze_frame_threshold and not freeze_flag:
#                     end_time = (cap.get(cv2.CAP_PROP_POS_MSEC) / 1000) - (freeze_frames / fps)
#                     if end_time - start_time >= min_segment_length:
#                         segments.append((start_time, end_time))
#                     freeze_flag = True
#             else:
#                 if freeze_flag:
#                     start_time = (cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
#                 freeze_frames = 0
#                 freeze_flag = False

#         last_frame = gray_frame

#     cap.release()

#     print(f"Number of segments: {len(segments)}")
#     return segments

# input_video = 'videos/nuplan/MetaDrive v0.3.0.1 2023-06-15 09-28-30.mp4'
# video_segments = get_segments(input_video, freeze_frame_threshold=9*10)

# for i, (start_time, end_time) in enumerate(video_segments):
#     output_video = f'videos/nuplan/1/segment_{i+1}.mp4'
#     cut_video_segment(input_video, start_time, end_time, output_video)
