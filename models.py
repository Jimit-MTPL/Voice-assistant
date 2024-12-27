from gpt4all import GPT4All
import os
#from faster_whisper import WhisperModel
import whisper
import sys

model = GPT4All("C:/Users/jimit_moontechnolabs/AppData/Local/nomic.ai/GPT4All/Llama-3.2-1B-Instruct-Q4_0.gguf", allow_download=False)
model.chat_session(system_prompt="You are a restaurant Bot. you must act as restaurant receptionist. Help user by answering their questions, recommending dishes, and placing orders. Collect the customer’s address and order details, then confirm the order before processing. and don't chat with yourself!")

base_model_path = os.path.expanduser('~/.cache/whisper/base.pt')
base_model = whisper.load_model(base_model_path)

if sys.platform != 'darwin':
    import pyttsx3
    engine = pyttsx3.init() 
