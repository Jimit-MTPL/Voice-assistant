#import warnings
import time
#import pyautogui
#import webbrowser
from model_response import respond
from ffmpeg_setup import set_ffmpeg_path
from voice_recognition import listen_for_command
from input_to_llm import perform_command
from variable_initialize import should_run

def main():
    set_ffmpeg_path()
    while should_run:
        command = listen_for_command()
        perform_command(command)
        time.sleep(1)
    respond("Goodbye.")

if __name__ == "__main__":
    main()