import os
import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
from moviepy.editor import VideoFileClip

def split_video(input_file, output_prefix, chunk_duration=15):
    video_clip = VideoFileClip(input_file)
    duration = video_clip.duration
    num_chunks = int(duration / chunk_duration) + 1

    for i in range(num_chunks):
        start_time = i * chunk_duration
        end_time = min((i + 1) * chunk_duration, duration)

        chunk_clip = video_clip.subclip(start_time, end_time)
        output_file = f"{output_prefix}_part{i + 1}.mp4"
        chunk_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

def on_drop(event):
    input_file = event.data
    output_prefix = os.path.splitext(os.path.basename(input_file))[0] + "_output"
    split_video(input_file, output_prefix)
    status_var.set(f"Видео успешно нарезано: {output_prefix}")

app = TkinterDnD.Tk()
app.geometry("400x200")  # Изменение размера окна

status_var = tk.StringVar()
status_label = tk.Label(app, textvariable=status_var, wraplength=300)
status_label.pack(pady=10)

status_var.set("Перетащите видеофайл сюда для нарезки.")

app.drop_target_register(DND_FILES)
app.dnd_bind('<<Drop>>', on_drop)

app.mainloop()
