import os
import magic
from PyPDF2 import PdfReader
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
from PIL import Image  # Using Pillow instead of imghdr

def is_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            header = f.read(4)
        return header.startswith(b"%PDF")
    except:
        return False

def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            img.verify()  # Verify if it's a valid image
        return True
    except:
        return False

def is_audio(file_path):
    try:
        audio = magic.Magic(mime=True).from_file(file_path)
        return "audio" in audio
    except:
        return False

def classify_file(file_path):
    if is_pdf(file_path):
        return "PDF Document"
    elif is_image(file_path):
        return "Image (JPG/PNG/etc.)"
    elif is_audio(file_path):
        return "Audio File"
    else:
        return "Unknown Format"

# Example Usage
directory = "document_classification"  # Change this to your directory path
for file_name in os.listdir(directory):
    file_path = os.path.join(directory, file_name)
    if os.path.isfile(file_path):
        print(f"{file_name}: {classify_file(file_path)}")