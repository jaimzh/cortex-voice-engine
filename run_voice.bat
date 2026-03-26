@echo off
REM Activate the virtual environment
call venv\Scripts\activate

REM Printing out a starter message
echo Setting up voice to text

REM Run the main script
python main.py

REM Keep the window open if the script finishes or crashes

pause

