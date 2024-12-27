from faster_whisper import WhisperModel
import os

# Specify the directory where you want to download the model
model_directory = "faster_whisper_model"

# Make sure the directory exists
os.makedirs(model_directory, exist_ok=True)

# Load the Whisper model and specify the custom directory
faster_base_model = WhisperModel("medium", download_root=model_directory)

print(f"Model has been downloaded and loaded from: {model_directory}")
