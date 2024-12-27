from faster_whisper import WhisperModel
import asyncio

model_directory = "faster_whisper_model"

model_size = 'medium'
model = WhisperModel(model_size, device='auto', download_root=model_directory)

segments, _ = model.transcribe(r'C:\Users\jimit_moontechnolabs\Desktop\Voice_assistant\temp_audio.wav', language="en")
transcription = " ".join(segment.text for segment in segments)
print(f"Transcription without async: {transcription}")


async def tts_func(num):
    asy_segments, _ = model.transcribe(r'C:\Users\jimit_moontechnolabs\Desktop\Voice_assistant\temp_audio.wav', language="en")
    asy_transcription = " ".join(asy_segment.text for asy_segment in asy_segments)
    print(f"Transcription {num}: {asy_transcription}")


async def call_func():
    for i in range(10):
        await tts_func(i)


if __name__ == "__main__":
    asyncio.run(call_func())