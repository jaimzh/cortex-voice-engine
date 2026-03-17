import pyperclip
import pyautogui
import time

def get_selected_text():
    old_clipboard = pyperclip.paste()
    print(f"Old clipboard: {old_clipboard!r}")

    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.1)  # a little longer to make sure the clipboard updates

    selected_text = pyperclip.paste()
    print(f"Grabbed text: {selected_text!r}")

    pyperclip.copy(old_clipboard)
    return selected_text

from utils import get_selected_text

if __name__ == "__main__":
    input("Highlight some text in any app, then press Enter here...")
    text = get_selected_text()
    print("Grabbed text:", repr(text))
    
    
    
    
    