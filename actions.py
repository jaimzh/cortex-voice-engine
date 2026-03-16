import webbrowser
import pyautogui
import time
import os
import subprocess


def open_youtube():
    webbrowser.open("https://youtube.com")
    
    
def open_site(site=""):
    if site: 
        webbrowser.open(f"https://{site}")

def open_google(query=""):
    if query:
        webbrowser.open(f"https://google.com/search?q={query.replace(' ', '+')}")


def type_hello():
    pyautogui.write("Hello! This action was triggered by your voice. ", interval=0.05)
    
def type_this(query):
    if query: 
        pyautogui.write("query ", interval=0.05)
        


TRIGGER_MAP = {
    "open youtube": open_youtube,
    "google": open_google,
    "type hello": type_hello,
    "type this": type_this, 
    "chrome": open_site,
    
}

def handle_action(text):
    if not text:
        return False

    clean_text = text.lower().strip()
    print(f"\n[Action Handler] Analyzing: \"{clean_text}\"")

    for trigger, action in TRIGGER_MAP.items():
        if trigger in clean_text:
            print(f" Trigger matched: '{trigger}'")
            
            if trigger == "google":
                query = clean_text.replace("google", "").strip().strip(",.?! ")
                action(query)
            elif trigger == "chrome":
                site = clean_text.replace("chrome", "").strip().strip(",.?! ")
                action(site)
            elif trigger == "type this": 
                query = clean_text.replace("type this", "").strip().strip(",.?! ")
                action(query)
                
            else:
                action()
            return True

    print("∅ No trigger matched.")
    return False

if __name__ == "__main__":
    pass