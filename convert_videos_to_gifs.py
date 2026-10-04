import os
import cv2
from PIL import Image

videos_dir = r"c:\Users\ASUS\OneDrive\Documents\LibraryManagementSystem\Artix7_LED_Counter\videos"

def mp4_to_gif(mp4_filename, gif_filename, target_width=380, fps=10, max_seconds=6):
    mp4_path = os.path.join(videos_dir, mp4_filename)
    gif_path = os.path.join(videos_dir, gif_filename)
    
    if not os.path.exists(mp4_path):
        print(f"Skipping {mp4_filename}, file not found.")
        return

    cap = cv2.VideoCapture(mp4_path)
    orig_fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    
    sample_interval = max(1, int(orig_fps / fps))
    max_frames = int(max_seconds * orig_fps)
    
    frames = []
    current_frame = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or current_frame > max_frames:
            break
            
        if current_frame % sample_interval == 0:
            h, w = frame.shape[:2]
            target_height = int(h * (target_width / w))
            resized = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_AREA)
            
            rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(rgb)
            
            # Convert to palette mode
            p_img = pil_img.convert('P', palette=Image.Palette.ADAPTIVE, colors=128)
            frames.append(p_img)
            
        current_frame += 1

    cap.release()

    if frames:
        duration_ms = int(1000 / fps)
        frames[0].save(
            gif_path,
            save_all=True,
            append_images=frames[1:],
            optimize=True,
            duration=duration_ms,
            loop=0
        )
        file_size_kb = os.path.getsize(gif_path) / 1024
        print(f"Successfully created {gif_filename} ({len(frames)} frames, {file_size_kb:.1f} KB)")

# Convert all 5 videos
mp4_to_gif("1hz.mp4", "1hz.gif", target_width=380, fps=10, max_seconds=5)
mp4_to_gif("2hz.mp4", "2hz.gif", target_width=380, fps=10, max_seconds=5)
mp4_to_gif("5hz.mp4", "5hz.gif", target_width=380, fps=10, max_seconds=5)
mp4_to_gif("10hz.mp4", "10hz.gif", target_width=380, fps=10, max_seconds=5)
mp4_to_gif("all.mp4", "all.gif", target_width=380, fps=10, max_seconds=8)
