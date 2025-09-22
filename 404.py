import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pydub import AudioSegment

def convert_wav_to_mp3(root_folder, bitrate="192k"):
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".wav"):
                wav_path = os.path.join(dirpath, filename)
                mp3_path = os.path.splitext(wav_path)[0] + ".mp3"

                if os.path.exists(mp3_path):
                    log(f"Skipping (already exists): {mp3_path}")
                    continue

                try:
                    log(f"Converting: {wav_path} -> {mp3_path}")
                    audio = AudioSegment.from_wav(wav_path)
                    audio.export(mp3_path, format="mp3", bitrate=bitrate)
                except Exception as e:
                    log(f"Failed to convert {wav_path}: {e}")

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        log(f"Selected folder: {folder}")
        convert_wav_to_mp3(folder)
        messagebox.showinfo("Done", "Conversion completed!")

def log(message):
    text_box.insert(tk.END, message + "\n")
    text_box.see(tk.END)

root = tk.Tk()
root.title("WAV to MP3 Converter")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

btn_choose = tk.Button(frame, text="Choose Folder", command=choose_folder)
btn_choose.pack(pady=5)

text_box = tk.Text(frame, height=20, width=80)
text_box.pack(pady=5)

root.mainloop()
