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

if __name__ == "__main__":
    input_video = "123.mp4"  # Укажите путь к вашему видеофайлу
    output_prefix = "prefix"  # Префикс для имен выходных файлов

    split_video(input_video, output_prefix)
