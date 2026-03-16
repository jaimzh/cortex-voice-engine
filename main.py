import keyboard
from playsound3 import playsound

from whisper import transcribe
from recorder import stop_recording_stream, start_recording_stream
from actions import handle_action

import time
import pyautogui
import pyperclip

is_recording = False
is_actions_mode = False
stream = None


def start_recording(e):
    global is_recording, stream, is_actions_mode

    if not is_recording:
        is_recording = True
        is_actions_mode = keyboard.is_pressed("shift")

        playsound("siri.mp3", block=False)
        print(f"Recording: {'actionss' if is_actions_mode else 'Dictation'}")

        stream = start_recording_stream()


def stop_recording(e):
    global is_recording, is_actions_mode

    if is_recording:
        is_recording = False

        print("Recording stopped")

        audio_data = stop_recording_stream(stream)

        if audio_data is None:
            return

        text = transcribe(audio_data)

        print("Transcribed Text:", text)

        if is_actions_mode == True:
            handle_action(text)
        else:
            pyperclip.copy(text + " ")
            pyautogui.hotkey("ctrl", "v")


if __name__ == "__main__":
    print("hey")
    print("Hold caps lock to record")
    print("Press ESC to quit")

    keyboard.on_press_key("caps lock", start_recording)
    keyboard.on_release_key("caps lock", stop_recording)

    while True:
        if keyboard.is_pressed("esc"):
            print("Exiting...")
            break

        time.sleep(0.1)
