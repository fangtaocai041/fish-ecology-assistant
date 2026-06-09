"""
make_video.py — 将长图渲染为纵向滚屏视频 + 未闻花名BGM
输出: MP4 H.264, 1080x1920, 30fps
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from moviepy import VideoClip, AudioFileClip, afx
import numpy as np
from PIL import Image
import os

IMG_PATH   = r"D:\Reasonix\docs\THREE_PROJECTS_EVOLUTION_warm.png"
AUDIO_PATH = r"D:\Reasonix\docs\secret_base.mp3"
OUT_PATH   = r"D:\Reasonix\docs\THREE_PROJECTS_EVOLUTION_视频_warm.mp4"

VIEWPORT_W, VIEWPORT_H, FPS = 1080, 1920, 30
VIDEO_DURATION = 90

print("[1/4] Loading image...")
pil_img = Image.open(IMG_PATH)
orig_w, orig_h = pil_img.size
print(f"      Original: {orig_w}x{orig_h}")

new_w = VIEWPORT_W
new_h = int(orig_h * new_w / orig_w)
pil_img = pil_img.resize((new_w, new_h), Image.LANCZOS)
img_array = np.array(pil_img)
scroll_max = new_h - VIEWPORT_H
scroll_speed = scroll_max / VIDEO_DURATION
print(f"      Scaled: {new_w}x{new_h}, scroll {scroll_max}px @ {scroll_speed:.1f} px/s")

print("[2/4] Loading audio...")
audio = AudioFileClip(AUDIO_PATH)
print(f"      Duration: {audio.duration:.1f}s")

print("[3/4] Generating frames...")
def make_frame(t):
    y = int(t * scroll_speed)
    y = max(0, min(y, scroll_max))
    return img_array[y:y+VIEWPORT_H, 0:VIEWPORT_W, :3]

clip = VideoClip(make_frame, duration=VIDEO_DURATION).with_fps(FPS)

bgm = audio.subclipped(0, VIDEO_DURATION)
bgm = bgm.with_effects([afx.AudioFadeOut(duration=3)])
clip = clip.with_audio(bgm)

print(f"[4/4] Encoding MP4 -> {OUT_PATH}")
clip.write_videofile(
    OUT_PATH, codec="libx264", fps=FPS, preset="medium",
    bitrate="5000k", audio_codec="aac", audio_bitrate="192k", threads=4,
)
size_mb = os.path.getsize(OUT_PATH) / (1024*1024)
print(f"\nDone! {OUT_PATH}  |  {size_mb:.1f} MB  |  {VIEWPORT_W}x{VIEWPORT_H}  |  {VIDEO_DURATION}s")
