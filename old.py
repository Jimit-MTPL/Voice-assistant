from os import system
import speech_recognition as sr
from gpt4all import GPT4All
import sys
import whisper
import warnings
import time
import pyautogui
import webbrowser
import os
import subprocess

model = GPT4All("C:/Users/jimit_moontechnolabs/AppData/Local/nomic.ai/GPT4All/Phi-3-mini-4k-instruct.Q4_0.gguf", allow_download=False)
#assistant_name = "hi"
#listening_for_trigger_word = True
should_run = True
source = sr.Microphone()
recognizer = sr.Recognizer()
base_model_path = os.path.expanduser('~/.cache/whisper/base.pt')
base_model = whisper.load_model(base_model_path)

if sys.platform != 'darwin':
    import pyttsx3
    engine = pyttsx3.init() 

tasks = []
listeningToTask = False
askingAQuestion = False

def check_ffmpeg():
    try:
        # Try to run ffmpeg
        subprocess.run(["ffmpeg", "-version"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False

def set_ffmpeg_path():
    ffmpeg_dir = 'C:\\ffmpeg'  # Default path to FFmpeg

    if check_ffmpeg():
        print("FFmpeg is already accessible in the system PATH.")
        return

    if not os.path.isdir(ffmpeg_dir):
        print("The provided path is not a valid directory.")
        return

    ffmpeg_path = os.path.join(ffmpeg_dir, "ffmpeg.exe")
    ffprobe_path = os.path.join(ffmpeg_dir, "ffprobe.exe")

    if not (os.path.isfile(ffmpeg_path) and os.path.isfile(ffprobe_path)):
        print("FFmpeg executables not found in the specified directory.")
        return

    # Add FFmpeg to system PATH for this session
    os.environ["PATH"] += os.pathsep + ffmpeg_dir
    print("FFmpeg path set successfully.")

def respond(text):
    if sys.platform == 'darwin':
        ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
        clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)
        system(f"say '{clean_text}'")
    else:
        engine.say(text)
        engine.runAndWait()

def listen_for_command():
    with source as s:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        with open("command.wav", "wb") as f:
            f.write(audio.get_wav_data())
        command = base_model.transcribe("command.wav")
        if command and command['text']:
            print("You said:", command['text'])
            return command['text'].lower()
        return None
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def perform_command(command):
    global tasks
    global listeningToTask
    global askingAQuestion
    global should_run
    #global listening_for_trigger_word
    
    if command:
        print("Command: ", command)
        """
        if listeningToTask:
            tasks.append(command)
            listeningToTask = False
            respond(f"Adding {command} to your task list. You have {len(tasks)} tasks in your list.")
        
        elif "add a task" in command:
            listeningToTask = True
            respond("Sure, what is the task?")
        
        elif "list tasks" in command:
            respond("Sure. Your tasks are:")
            for task in tasks:
                respond(task)  # Respond once per task
        
        elif "take a screenshot" in command:
            pyautogui.screenshot("screenshot.png")
            respond("I took a screenshot for you.")
        
        elif "open chrome" in command:
            respond("Opening Chrome.")
            webbrowser.open("http://www.youtube.com/@JakeEh")
        
        elif "ask a question" in command:
            askingAQuestion = True
            respond("What's your question?")
            return  # Exit to prevent further command processing
        
        elif askingAQuestion:
            askingAQuestion = False
        """
        respond("Thinking...")  # Notify the user you're processing the question
            
        print("User command: ", command)
        output = model.generate(command, max_tokens=200)
            
        if output:  # Check if the model produced output
            print("Output: ", output)
            respond(output)  # Respond with the generated output only once
        
        if "exit" in command:
            should_run = False
        
        #else:
        #   respond("Sorry, I'm not sure how to handle that command.")
    
    # Reset the listening state
    #listening_for_trigger_word = True
    
    # Add a short delay to prevent quick re-triggering of the same command
    time.sleep(1)  # You can adjust this based on your requirements


def main():
    set_ffmpeg_path()
    #global listening_for_trigger_word
    while should_run:
        command = listen_for_command()
        #if listening_for_trigger_word:
        #    listening_for_trigger_word = False
        #else:
        perform_command(command)
        time.sleep(1)
    respond("Goodbye.")

if __name__ == "__main__":
    main()