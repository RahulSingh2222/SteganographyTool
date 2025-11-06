🕵️ Steganography Tool (Python GUI)

A simple yet powerful Steganography Tool built with Python and Tkinter that allows users to hide secret text messages inside image files (encoding) and extract them back (decoding).
This project demonstrates how data can be concealed within images using the Least Significant Bit (LSB) method — a common concept in cybersecurity and digital forensics.

🚀 Features

🧩 Encode any secret message inside a PNG/JPG image.

🔍 Decode and extract the hidden message from an encoded image.

💻 User-friendly GUI made using Tkinter.

💾 Automatically saves the encoded image as encoded_image.png.

⚡ Lightweight and works completely offline.

🧠 How It Works

The tool modifies the least significant bits (LSB) of pixel values in an image to store binary data of your message.
Visually, the image remains unchanged — but the hidden text can later be retrieved by decoding the pixel data.

🛠️ Installation

Clone this repository

git clone https://github.com/RahulSingh2222/SteganographyTool.git


Navigate into the project folder

cd SteganographyTool


Install required dependencies

pip install pillow


Run the application

python steganography_tool.py

🧰 Requirements

Python 3.7 or above

Pillow (Python Imaging Library)

Tkinter (usually included with Python)

🖼️ GUI Overview

Encode Message Section:

Browse an image and enter a secret message.

Click “Encode & Save Image” to generate a new encoded image.

Decode Message Section:

Browse the encoded image.

Click “Decode Message” to reveal the hidden text.

🌐 Try It Out

👉 Click here to view this project on GitHub
