# Video_To_Text_Converter
A simple python project to extract text from a video file.

1]Import necessary libraries:
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio to extract audio from the video.
from pydub import AudioSegment to work with audio files.
import speech_recognition as sr for speech recognition.

2]Define input and output file paths:
video_file: Path to the input video file.
audio_file: Path to the output audio file where extracted audio will be saved.

3]Extract audio from the video:
Use ffmpeg_extract_audio(video_file, audio_file) to extract audio from the video file.

4]Load the extracted audio using PyDub:
Use AudioSegment.from_wav(audio_file) to load the extracted audio.

5]Initialize a speech recognizer:
recognizer = sr.Recognizer() initializes the speech recognizer from the speech_recognition library.

6]Transcribe the audio:
Open the audio file with sr.AudioFile(audio_file) as the source.
Record the audio using recognizer.record(source).
Attempt to transcribe the audio using Google Web Speech API (recognizer.recognize_google(audio_data)).
Handle possible exceptions like sr.UnknownValueError or sr.RequestError.

7]Save the transcription to a text file:

Open a text file in write mode ("transcription.txt").
Write the transcription (text) into the file.
