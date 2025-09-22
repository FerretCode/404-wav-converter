# 404-wav-converter
A simple Python tool for converting lots of sounds from wav -> mp3 for compatibility with the Roland SP404

## Directory Structure

- With this tool, you must select one root directory that contains all of your kits
  - The script will walk all other directories in the root directory, converting .wav -> .mp3
  - Directory folder structure is maintained

## Setup & Dependencies

- This tool depends on `ffmpeg` and `pydub`
- Ensure you have `ffmpeg` installed and in your system's path prior to installation
```sh
cd packs # enter the folder containing all of your kits
python -m venv .venv # create a new virtual environment to install dependencies

source .venv/bin/activate # on unix systems
source .venv\Scripts\Activate.ps1 # on windows systems

pip install pydub # install pydub for conversion

python 404.py # open the tool
```
