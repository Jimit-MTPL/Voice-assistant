import subprocess
import os

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