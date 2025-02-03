import whisper
import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from PIL import Image
import numpy as np

model = whisper.load_model("small")

video_path = "final_video.mp4"
video = VideoFileClip(video_path)

target_height = 1920
aspect_ratio = video.size[0] / video.size[1]
target_width = int(target_height * aspect_ratio)

video = video.fl_image(lambda image: np.array(Image.fromarray(image).resize((target_width, target_height), Image.Resampling.LANCZOS)))

audio_path = "temp_audio.wav"
video.audio.write_audiofile(audio_path)

result = model.transcribe(audio_path, word_timestamps=True)

subtitle_clips = []

grouped_words = {
    "drive-through": "drive-through",
    "late-night": "late-night",
}

for segment in result['segments']:
    for word_info in segment['words']:
        word = word_info['word']
        start = word_info['start']
        end = word_info['end']

        if word in grouped_words:
            word = grouped_words[word]

        text_clip = TextClip(
            word,
            fontsize=100,
            color='white',
            size=video.size,
            font='Arial-Black',
            stroke_color='black',
            stroke_width=4
        ).set_start(start).set_end(end).set_position('center')

        subtitle_clips.append(text_clip)

final_video = CompositeVideoClip([video] + subtitle_clips)

final_video_path = "final_video_with_subtitles.mp4"
final_video.write_videofile(final_video_path, codec='libx264', fps=video.fps)

os.remove(audio_path)
