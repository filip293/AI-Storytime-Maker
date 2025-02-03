# AI Storytime Maker For Tiktok, Youtube and Instagram

### Important:
Please place the video in the `Audio` folder and name it `Background.mp4`.

You can access the video I use [here](#).

## Overview
AI Storytime Maker is an automated tool that generates eerie storytelling videos with:
- AI-generated story creation to ensure unique and engaging narratives
- AI-generated speech (creepy voice transformation)
- Background music and visuals
- Automatic subtitle generation
- Video resizing for mobile-friendly viewing

This repository leverages **Gemma2, Fish Speech TTS, MoviePy, Whisper AI, and Pydub** to fully automate the storytelling process.

---

## Structure

### 1️⃣ **Story Generation - `Story.py`**
- Uses **Gemma2** to generate unique stories.
- Saves generated stories to prevent repetition.
- Summarizes stories for reference.

### 2️⃣ **Video Creation - `Video.py`**
- Uses **Fish Speech TTS** to convert stories into creepy AI-generated voice.
- Speeds up narration for pacing.
- Combines voice, background music, and visuals to generate the final video.

### 3️⃣ **Subtitle Generation - `AutoCAPS.py`**
- Uses **Whisper AI** for transcribing the generated video.
- Creates automatic captions and overlays them onto the video.
- Resizes video for mobile-friendly viewing.

---

## Features
✅ **AI-Powered Storytelling** - Unique stories are generated for every run.  
✅ **Text-to-Speech (TTS)** - Converts written stories into a creepy AI-generated voice.  
✅ **Background Audio & Video** - Automatically merges generated audio with selected visuals.  
✅ **Whisper AI Transcription** - Adds auto-generated subtitles to the final video.  
✅ **Video Resizing** - Optimizes videos for mobile screens.  
✅ **Speed Adjustment** - Tweaks narration speed for better pacing.  
✅ **Customizable** - Modify video size, audio processing, and subtitle styling easily.  

---

## Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/AI-Storytime-Maker.git
cd AI-Storytime-Maker
```

### 2️⃣ Install Dependencies
All required dependencies are listed in `requirements.txt`. Install them using:
```bash
pip install -r requirements.txt
```

---

### Usage

#### 1️⃣ Run the Story Generation Script
```bash
python Story.py
```
- Generates and saves a unique AI-generated story.

#### 2️⃣ Create the Video with Audio
```bash
python Video.py
```
- Converts the story into creepy AI voice.
- Combines voice, background music, and visuals.

#### 3️⃣ Add Auto-Generated Captions
```bash
python AutoCAPS.py
```
- Transcribes the video and overlays subtitles.

### 4️⃣ Generated Output
- **Final video**: `final_video.mp4`
- **Audio files**: Stored in the `Audio/` directory.
- **Subtitled video**: `final_video_with_subtitles.mp4`

---

## Configuration
Customize the settings by modifying `Video.py` and `AutoCAPS.py`:

| Setting | Description | Default Value |
|---------|-------------|---------------|
| `background_video` | Path to the background video file | `Audio/background.mp4` |
| `background_music` | Path to the background music file | `Audio/Mystery.mp3` |
| `speed_factor` | Speed multiplier for voice audio | `1.2` |
| `target_height` | Video height for mobile resizing | `1920` |
| `font` | Font style for subtitles | `Arial-Black` |

---

## Dependencies

📦 The following models and libraries are used:
- **Gemma2** (https://ollama.com)
- **Fish Speech TTS** (https://huggingface.co/fishaudio/fish-speech-1)
- **Whisper AI** (https://github.com/openai/whisper)
- **MoviePy** (https://zulko.github.io/moviepy/)
- **Pydub** (https://pydub.com/)

To use Whisper AI, ensure you download the required model before running the script.

---

## Example Output
![Example Output](https://via.placeholder.com/800x400?text=Final+Generated+Video)

---

## Requirements.txt
```
moviepy
pydub
gradio_client
whisper
numpy
pillow
ollama
```

---

## Contributing
Feel free to use and contribute! Fork the repository and submit a pull request with your improvements.

---

## License
MIT License © 2025 TheSpectre

