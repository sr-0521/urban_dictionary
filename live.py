import os
import tkinter as tk
from tkinter import font

def play_pronunciation():
    os.system("afplay ~/Desktop/msa/powerpoint_night/live.mp3")

def play_pronunciation_1():
    os.system("afplay ~/Desktop/msa/powerpoint_night/fahad.mp3")

def play_pronunciation_2():
    os.system("afplay ~/Desktop/msa/powerpoint_night/suleman.mp3")

# Create main window
root = tk.Tk()
root.title("live - Urban Dictionary")
root.configure(bg="#1c2431")

# Use consistent font styles
title_font = font.Font(family="Helvetica", size=32, weight="bold")
text_font = font.Font(family="Helvetica", size=13)
link_font = font.Font(family="Helvetica", size=13, weight="bold", underline=True)
italic_font = font.Font(family="Helvetica", size=13, slant="italic")
bold_font = font.Font(family="Helvetica", size=11, weight="bold")

# Main container
frame = tk.Frame(root, bg="#1c2431", padx=30, pady=30)
frame.pack(expand=True)

# Title
title_label = tk.Label(frame, text="live", font=title_font, fg="#5daeff", bg="#1c2431")
title_label.pack(anchor="w", pady=(0, 15))

# Pronunciation frame
pronounce_frame = tk.Frame(frame, bg="#1c2431")
pronounce_frame.pack(anchor="w", pady=(0, 15))

pronounce_label = tk.Label(pronounce_frame, text="Pronounced: 'lyv'", font=text_font, fg="#e5e7eb", bg="#1c2431")
pronounce_label.pack(side="left")

speaker_button = tk.Button(pronounce_frame, text="🔊", font=bold_font, fg="white",
                           bg="#1c2431", activebackground="#5daeff", activeforeground="black",
                           borderwidth=1, relief="flat", padx=10, pady=5,
                           command=play_pronunciation)
speaker_button.pack(side="left", padx=(10, 0))

# Definition text
definition_text = (
    "Used to describe something or someone thats active, happening,"
    " or full of energy. When something is live, its got the vibe — "
    "people are there, the mood is up, and its worth being part of. "
    "Can refer to a person, a room thats popping off, or the MSA weekly brothers event."
)
definition_label = tk.Label(frame, text=definition_text, font=text_font, fg="#e5e7eb",
                            bg="#1c2431", wraplength=600, justify="left")
definition_label.pack(anchor="w", pady=(0, 20))

# Example 1
example_text1 = "Yo is Davis live? Is Davis live?"
example_frame1 = tk.Frame(frame, bg="#1c2431")
example_frame1.pack(anchor="w", pady=(0, 20))

example_label1 = tk.Label(example_frame1, text=example_text1, font=italic_font, fg="#8dcaff",
                          bg="#1c2431", wraplength=550, justify="left")
example_label1.pack(side="left")

speaker_button1 = tk.Button(example_frame1, text="🔊", font=bold_font, fg="white",
                            bg="#1c2431", activebackground="#5daeff", activeforeground="black",
                            borderwidth=1, relief="flat", padx=5, pady=2,
                            command=play_pronunciation_1)
speaker_button1.pack(side="left", padx=(10, 0))

# Example 2
example_text2 = "Yo cubicles is live cuh, stahp tryna tell me its not vro 💔🥀"
example_frame2 = tk.Frame(frame, bg="#1c2431")
example_frame2.pack(anchor="w", pady=(0, 20))

example_label2 = tk.Label(example_frame2, text=example_text2, font=italic_font, fg="#8dcaff",
                          bg="#1c2431", wraplength=550, justify="left")
example_label2.pack(side="left")

speaker_button2 = tk.Button(example_frame2, text="🔊", font=bold_font, fg="white",
                            bg="#1c2431", activebackground="#5daeff", activeforeground="black",
                            borderwidth=1, relief="flat", padx=5, pady=2,
                            command=play_pronunciation_2)
speaker_button2.pack(side="left", padx=(10, 0))

# Contributor
contrib_label = tk.Label(frame, text="by r0adman_fxhxd - Sep 14, 2025",
                         font=bold_font, fg="#5daeff", bg="#1c2431")
contrib_label.pack(anchor="w", pady=(0, 25))

# --- Buttons section ---
buttons_frame = tk.Frame(frame, bg="#1c2431", highlightbackground="#5daeff",
                         highlightcolor="#5daeff", highlightthickness=1, bd=0)
buttons_frame.pack(pady=10)

# Button styles
def make_button(text, emoji=None):
    label = f"{emoji} {text}" if emoji else text
    return tk.Button(buttons_frame, text=label, font=bold_font, fg="white",
                     bg="#1c2431", activebackground="#5daeff", activeforeground="black",
                     borderwidth=1, relief="flat", padx=25, pady=10)

like_btn = make_button("", "👍")
dislike_btn = make_button("", "👎")
flag_btn = make_button("", "🚩")

like_btn.grid(row=0, column=0, sticky="ew")
dislike_btn.grid(row=0, column=1, sticky="ew")
flag_btn.grid(row=0, column=2, sticky="ew")

for i in range(3):
    buttons_frame.columnconfigure(i, weight=1, uniform="equal")

# Run window
root.mainloop()