# 🎤 Urban Dictionary GUI: "Live"
"Yo is Davis live? Is Davis live?"

A custom-built, interactive GUI mimicking the Urban Dictionary interface, created for the UTM MSA Brothers' PowerPoint Night.

This tool was built to settle a debate and formally define the slang term "live" once and for all. Instead of a static slide, I wrote a Python script to render a functional application during the presentation, complete with audio triggers featuring voiceovers from friends in the community.

# 📸 Preview
<img width="647" height="523" alt="Screenshot 2025-12-17 at 10 06 07 PM" src="https://github.com/user-attachments/assets/2358ef68-7e0b-4547-ad7a-d93635c1f149" />


💡 Context
During a social event (PowerPoint Night), I gave a presentation breaking down specific community slang. To make the presentation interactive and humorous, I built this script to:

Clone the UI: Replicates the Urban Dictionary "Dark Mode" aesthetic using Python's tkinter.

Audio Integration: triggers system-level audio commands (afplay) to play recordings of friends pronouncing the word and using it in (questionable) context.

Engagement: The tool was demoed live, resulting in a highly engaging and funny segment of the night.

🛠️ Built With
Python 3

Tkinter (Standard Python GUI library)

macOS afplay (Audio File Play) - Note: This script relies on the macOS native audio terminal command.

💻 Code Highlights
The script creates a custom tkinter window with hardcoded styling to match the Urban Dictionary brand colors (#1c2431 background, #5daeff accents).

Custom font mapping to match the Urban Dictionary aesthetic
title_font = font.Font(family="Helvetica", size=32, weight="bold")
link_font = font.Font(family="Helvetica", size=13, weight="bold", underline=True)
It also handles system calls for audio playback:

Python
def play_pronunciation():
    # Triggers the macOS audio player for the specific MP3 file
    os.system("afplay ~/Desktop/msa/powerpoint_night/live.mp3")
🚀 How to Run
Note: This script is designed for macOS due to the afplay dependency.

# How to Run
Clone the repository.

Ensure you have Python 3 installed.

Update the file paths in the script to point to your local .mp3 files:

Python
os.system("afplay /path/to/your/audio/file.mp3")
Run the script:

Bash
python3 live.py

