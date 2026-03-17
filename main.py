import keyboard
from playsound3 import playsound

from whisper import transcribe
from recorder import stop_recording_stream, start_recording_stream
from actions import handle_action
from cortex import process_text 
import time
import pyautogui
import pyperclip

is_recording = False
is_actions_mode = False
is_cortex_mode = False
stream = None




def get_selected_text():
   
    pyautogui.hotkey("ctrl", "c")

    for _ in range(5):
        time.sleep(0.1)
        selected_text = pyperclip.paste()
        if selected_text:
            break
    else:
        selected_text = "" 

    return selected_text






def start_recording(e):
    global is_recording, stream, is_actions_mode, is_cortex_mode

    if not is_recording:
        is_recording = True
        is_actions_mode = keyboard.is_pressed("shift")
        is_cortex_mode = keyboard.is_pressed("ctrl")

        playsound("siri.mp3", block=False)
        
        if is_actions_mode:
            mode_name = "Actions"
        elif is_cortex_mode:
            mode_name = "Cortex"
        else:
            mode_name = "Dictation"
            
        print(f"Recording: {mode_name}")
        
        stream = start_recording_stream()

def stop_recording(e):
    global is_recording, is_actions_mode, is_cortex_mode

    if is_recording:
        is_recording = False
        print("Recording stopped")

        audio_data = stop_recording_stream(stream)
        if audio_data is None:
            return

        text = transcribe(audio_data)
        print("Transcribed Text:", text)
        print()

        # Decide mode
        if is_actions_mode:
            print("Mode: Actions")
            handle_action(text)
        elif is_cortex_mode:
            print("Mode: Cortex")
            
            selected = get_selected_text()
            final_text = process_text(text, context=selected)
            print("Selected text", selected)
            print("Cortex Output:", final_text)
            pyperclip.copy(final_text + " ")
            pyautogui.hotkey("ctrl", "v")
        else:
            print("Mode: Dictation")
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
