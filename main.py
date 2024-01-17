from moviepy.editor import VideoFileClip

def split_video(input_file, output_prefix, chunk_size_mb=25):
    video_clip = VideoFileClip(input_file)
    duration = video_clip.duration
    chunk_size_bytes = chunk_size_mb * 1024 * 1024
    num_chunks = int(duration / chunk_size_mb) + 1

    for i in range(num_chunks):
        start_time = i * chunk_size_mb
        end_time = min((i + 1) * chunk_size_mb, duration)

        chunk_clip = video_clip.subclip(start_time, end_time)
        output_file = f"{output_prefix}_part{i + 1}.mp4"
        chunk_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

if __name__ == "__main__":
    input_video = "ваше_видео.mp4"  # Укажите путь к вашему видеофайлу
    output_prefix = "output_video_chunk"  # Префикс для имен выходных файлов

    split_video(input_video, output_prefix)
