from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
from pydub import AudioSegment

# Input video file (using double backslashes)
video_file = video_file = "Video3.mp4"

# Output audio file
audio_file = "output_audio.wav"

# Extract audio from the video
ffmpeg_extract_audio(video_file, audio_file)

# Load the audio using pydub
audio = AudioSegment.from_wav(audio_file)

import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Transcribe the audio
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)  # Record the audio
    try:
        text = recognizer.recognize_google(audio_data)  # Use Google Web Speech API
        print("Transcription: " + text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

# Save the transcription to a text file
with open("transcription.txt", "w") as file:
    file.write(text)
