import speech_recognition as sr
import whisper
import numpy as np
import os

base_model_path = os.path.expanduser('~/.cache/whisper/base.pt')
base_model = whisper.load_model(base_model_path)


# Initialize recognizer
recognizer = sr.Recognizer()

# Capture audio from microphone
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)
    
    # Convert the captured audio to raw data
    audio_data = np.frombuffer(audio.get_raw_data(), np.int16)

    # Transcribe the audio using Whisper without saving it as a file
    result = base_model.transcribe(audio_data, fp16=False)
    print(result['text'])