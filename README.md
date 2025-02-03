# AI Storytime Maker

![AI Storytime Maker](https://via.placeholder.com/1200x400?text=AI+Storytime+Maker)

## Overview
AI Storytime Maker is an automated tool that generates eerie storytelling videos with:
- AI-generated speech (creepy voice transformation)
- Background music and visuals
- Automatic subtitle generation
- Video resizing for mobile-friendly viewing

This repository leverages **Fish Speech TTS, MoviePy, Whisper AI, and Pydub** to fully automate the storytelling process.

---

## Features
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

### 1️⃣ Place Your Story
- Write your story inside `story.txt`.
- Place a reference voice file in `Audio/Reference.mp3`.

### 2️⃣ Run the Script
```bash
python main.py
```

### 3️⃣ Generated Output
- **Final video**: `final_video.mp4`
- **Audio files**: Stored in the `Audio/` directory.
- **Subtitled video**: `final_video_with_subtitles.mp4`

---

## Configuration
Customize the settings by modifying `main.py`:

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
```

---

## Contributing
Feel free to use and contribute! Fork the repository and submit a pull request with your improvements.

---

## License
MIT License © 2025 TheSpectre

