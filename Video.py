from moviepy.editor import AudioFileClip, VideoFileClip, CompositeAudioClip
import shutil
import os
import random
from gradio_client import Client, handle_file
from pydub import AudioSegment

client = Client("fishaudio/fish-speech-1")

def create_creepy_voice(story_file, reference_audio_path, output_audio):
    try:
        with open(story_file, 'r', encoding='utf-8') as file:
            story = file.read()

        tts_result = client.predict(
            text=story,
            reference_audio=handle_file(reference_audio_path),
            max_new_tokens=0,
            chunk_length=200,
            top_p=0.7,
            repetition_penalty=1.2,
            temperature=0.7,
            api_name="/inference_wrapper"
        )

        print("TTS Response:", tts_result)

        audio_path = tts_result[0]

        if os.path.exists(audio_path):
            if os.path.exists(output_audio):
                os.remove(output_audio)

            shutil.copy(audio_path, output_audio)
            print(f"Audio saved as {output_audio}")
        else:
            raise ValueError("No valid audio file found in TTS result.")
    except Exception as e:
        print(f"Error during TTS generation: {e}")
        raise

def speed_up_audio(input_audio_path, output_audio_path, speed_factor):
    try:
        audio = AudioSegment.from_wav(input_audio_path)
        speed_changed_audio = audio.speedup(playback_speed=speed_factor)
        speed_changed_audio.export(output_audio_path, format="wav")
        print(f"Audio speed changed and saved as {output_audio_path}")
    except Exception as e:
        print(f"Error during audio speed adjustment: {e}")
        raise

def create_video_with_audio(output_audio, background_video, background_music, output_video):
    try:
        video_clip = VideoFileClip(background_video).without_audio()
        voice_clip = AudioFileClip(output_audio)
        music_clip = AudioFileClip(background_music).subclip(0, voice_clip.duration)
        combined_audio = CompositeAudioClip([voice_clip.volumex(1.0), music_clip.volumex(0.3)])
        print(f"Audio duration: {combined_audio.duration} seconds")

        if video_clip.duration <= combined_audio.duration + 40:
            raise ValueError("The background video is too short to select a portion at least 40 seconds away from the end.")

        max_start_time = video_clip.duration - combined_audio.duration - 40
        start_time = random.uniform(0, max_start_time)
        print(f"Selected start time: {start_time} seconds")
        video_subclip = video_clip.subclip(start_time, start_time + combined_audio.duration)
        final_video = video_subclip.set_audio(combined_audio)
        print("Combined audio set to the final video.")
        final_video.write_videofile(output_video, codec='libx264', audio_codec='aac', fps=24, audio=True)
        print(f"Final video saved as {output_video}")
    except Exception as e:
        print(f"Error during video creation: {e}")
        raise

def main():
    story_file = 'story.txt'
    reference_audio_path = 'Audio/Reference.mp3'
    output_audio = 'creepy_voice.wav'
    background_video = 'Audio/background.mp4'
    background_music = 'Audio/Mystery.mp3'
    output_video = 'final_video.mp4'

    try:
        create_creepy_voice(story_file, reference_audio_path, output_audio)
        speed_up_audio(output_audio, 'sped_up_creepy_voice.wav', 1.2)
        create_video_with_audio('sped_up_creepy_voice.wav', background_video, background_music, output_video)
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
