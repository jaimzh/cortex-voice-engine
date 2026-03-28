# Cortex: Context Aware Voice to Text Engine

Cortex is a context-aware, voice-driven workspace assistant. It is a headless text engine designed to understand both your voice commands and the context of your screen.

---

## Operational Modes

### Dictation (Caps Lock)
Standard high-accuracy transcription. Speak and release to have your speech transcribed and pasted at the cursor.

### Actions (Caps Lock + Shift)
Execute system-level commands with your voice. Open websites, search Google, or trigger custom macros defined in `actions.py`.

### Cortex (Caps Lock + Ctrl)
The core feature of the system. Highlight text on your screen and tell Cortex how to transform it. It uses an LLM to bridge the gap between your selection and your intent.

### Text Intelligence (Ctrl + Alt)
A shortcut for instant text processing without voice recording. Highlight any text and press Ctrl + Alt to have Cortex automatically answer a question, summarize content, or transform the selection based on its current state. It provides real-time feedback by showing a thinking placeholder before replacing the text with the AI result.

#### Example Command Patterns:
- **Transformation:** Highlight "hello world" and say "make this uppercase" -> **HELLO WORLD**
- **Grammar & Cleanup:** Highlight a rough draft and say "fix the grammar and make it formal" -> **A polished version.**
- **Phonetic Correction:** Say "My name is James J A I M Z" -> **My name is Jaimz** 
- **Format Conversion:** Say "Notion: make a list of apples and milk" -> A formatted checkbox list.
- **Direct Intel:** Say "Cortex: what is the boiling point of water?" -> **100°C**

---

## Example Interaction

**Voice Transformation:**
Imagine you have this highlighted:
> "the user is currently on the login page"

You hold **Caps Lock + Ctrl** and say: "make login page upper cake and wrap in brackets"

**Cortex Output:**
> "the user is currently on the [LOGIN PAGE]"

**Text Intelligence:**
Imagine you have this highlighted in your editor:
> "What is the Big O complexity of binary search?"

You press **Ctrl + Alt** (no voice needed).

**Cortex Output:**
> "O(log n)"

---

## Installation & Setup

### 1. Python Dependencies
Install the core libraries required for audio, hotkeys, and AI:
```bash
pip install -r requirements.txt
```

### 2. System Requirements
To make transcription and the AI engine work, you need these two dependencies installed on your system:

- **FFmpeg**: Required by Whisper to process audio.
  - Windows: `winget install FFmpeg` or `choco install ffmpeg`
- **Ollama**: Required for the Cortex transformation mode.
  - Download from [ollama.com](https://ollama.com) and ensure it is running.

### 3. Audio Feedback
Place a `siri.mp3` file in the `sounds/` directory to hear a chime when you start recording.

---

## Controls

| Shortcut | Mode | Action |
| :--- | :--- | :--- |
| Caps Lock (Hold) | Dictation | Transcribe speech to text |
| Caps Lock + Shift | Actions | Run voice commands |
| Caps Lock + Ctrl | Cortex | Process selected text with context |
| Ctrl + Alt | Text Intelligence | Instant AI answer or transformation |
| Esc | Exit | Stop the application |

---

## Project Structure

```text
cortex_voice_to_text_engine/
├── sounds/           # Audio feedback (siri.mp3)
├── main.py           # Core listener & hub
├── cortex.py         # AI transformation engine
├── whisper.py        # Local transcriber
├── recorder.py       # Audio capture
├── actions.py        # Voice-triggered commands
└── requirements.txt  # Python dependencies
```

---

## System Architecture

- `main.py`: The central hub and keyboard listener.
- `cortex.py`: LLM logic and system prompt for context-processing.
- `whisper.py`: Handles local transcription via Whisper.
- `actions.py`: Custom map of voice-triggered commands.
- `recorder.py` & `utils.py`: Audio handling and system helpers.
