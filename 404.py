#!/usr/bin/env python3
import os
import argparse
from pydub import AudioSegment

def convert_wav_to_mp3(root_folder, bitrate="192k"):
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".wav"):
                wav_path = os.path.join(dirpath, filename)
                mp3_path = os.path.splitext(wav_path)[0] + ".mp3"

                if os.path.exists(mp3_path):
                    print(f"Skipping (already exists): {mp3_path}")
                    continue

                try:
                    print(f"Converting: {wav_path} -> {mp3_path}")
                    audio = AudioSegment.from_wav(wav_path)
                    audio.export(mp3_path, format="mp3", bitrate=bitrate)
                except Exception as e:
                    print(f"Failed to convert {wav_path}: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Batch convert WAV files to MP3."
    )
    parser.add_argument(
        "folder", 
        type=str, 
        help="Path to the folder containing WAV files."
    )
    parser.add_argument(
        "--bitrate", 
        type=str, 
        default="192k", 
        help="Bitrate for the MP3 files (default: 192k)."
    )

    args = parser.parse_args()
    folder = os.path.abspath(args.folder)

    if not os.path.isdir(folder):
        print(f"Error: {folder} is not a valid directory.")
        return

    convert_wav_to_mp3(folder, bitrate=args.bitrate)
    print("Conversion completed!")

if __name__ == "__main__":
    main()
