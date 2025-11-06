from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

# ---------- Encode Function ----------
def encode_image():
    global selected_image_path
    try:
        secret_message = text_message.get("1.0", END).strip()
        if not selected_image_path:
            messagebox.showwarning("No Image", "Please select an image first.")
            return
        if not secret_message:
            messagebox.showwarning("Empty Message", "Please enter a secret message to hide.")
            return

        image = Image.open(selected_image_path)
        encoded = image.copy()
        width, height = image.size
        index = 0

        binary_message = ''.join(format(ord(i), '08b') for i in secret_message)
        binary_message += '1111111111111110'  # End delimiter

        for row in range(height):
            for col in range(width):
                if index < len(binary_message):
                    r, g, b = image.getpixel((col, row))
                    r = (r & ~1) | int(binary_message[index])
                    encoded.putpixel((col, row), (r, g, b))
                    index += 1

        encoded.save("encoded_image.png")
        messagebox.showinfo("Success", "Message successfully encoded into 'encoded_image.png'!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# ---------- Browse Image (for encoding) ----------
def browse_image():
    global selected_image_path
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        selected_image_path = file_path
        lbl_selected.config(text=f"Selected: {file_path.split('/')[-1]}")

# ---------- Browse Encoded Image (for decoding) ----------
def browse_encoded_image():
    global encoded_image_path
    file_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        encoded_image_path = file_path
        lbl_encoded.config(text=f"Selected: {file_path.split('/')[-1]}")

# ---------- Decode Function ----------
def decode_message():
    global encoded_image_path
    try:
        if not encoded_image_path:
            messagebox.showwarning("No Image", "Please select an encoded image first.")
            return

        image = Image.open(encoded_image_path)
        width, height = image.size
        binary_data = ""

        for row in range(height):
            for col in range(width):
                r, g, b = image.getpixel((col, row))
                binary_data += str(r & 1)

        # Split into 8-bit chunks
        all_bytes = [binary_data[i:i + 8] for i in range(0, len(binary_data), 8)]
        decoded_message = ""

        for byte in all_bytes:
            char = chr(int(byte, 2))
            decoded_message += char
            # Stop if we reach the binary end marker
            if decoded_message.endswith("ÿþ"):  # equivalent to 1111111111111110
                decoded_message = decoded_message[:-2]  # remove marker
                break

        text_decoded.delete("1.0", END)
        text_decoded.insert(END, decoded_message.strip())

        messagebox.showinfo("Decoded", "Message successfully decoded!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# ---------- Main Window ----------
root = Tk()
root.title("🕵️‍♂️ Steganography Tool - by Rahul Singh")
root.geometry("650x600")
root.resizable(False, False)

selected_image_path = ""
encoded_image_path = ""

# ---------- Header ----------
# ---------- Header ----------
title_label = Label(root, text="Steganography Tool", font=("Arial", 22, "bold"))
title_label.pack(pady=10)

subtitle_label = Label(root, text="Hide and Reveal Secret Messages in Images", font=("Arial", 11))
subtitle_label.pack(pady=5)

# ---------- Encode Section ----------
encode_frame = LabelFrame(root, text="Encode Message", padx=10, pady=10, font=("Arial", 10, "bold"))
encode_frame.pack(padx=15, pady=10, fill="both", expand=True)

Label(encode_frame, text="Select Image:").grid(row=0, column=0, sticky=W, pady=5)
Button(encode_frame, text="Browse Image", width=20, command=browse_image).grid(row=0, column=1, pady=5)
lbl_selected = Label(encode_frame, text="No file selected", fg="gray")
lbl_selected.grid(row=1, column=1, sticky=W)

Label(encode_frame, text="Enter Secret Message:").grid(row=2, column=0, sticky=W, pady=5)
text_message = Text(encode_frame, height=4, width=45)
text_message.grid(row=2, column=1, pady=5)

Button(encode_frame, text="Encode & Save Image", width=22, command=encode_image).grid(row=3, column=1, pady=10)

# ---------- Decode Section ----------
decode_frame = LabelFrame(root, text="Decode Message", padx=10, pady=10, font=("Arial", 10, "bold"))
decode_frame.pack(padx=15, pady=10, fill="both", expand=True)

Label(decode_frame, text="Select Encoded Image:").grid(row=0, column=0, sticky=W, pady=5)
Button(decode_frame, text="Browse Encoded Image", width=22, command=browse_encoded_image).grid(row=0, column=1, pady=5)
lbl_encoded = Label(decode_frame, text="No file selected", fg="gray")
lbl_encoded.grid(row=1, column=1, sticky=W)

Button(decode_frame, text="Decode Message", width=22, command=decode_message).grid(row=2, column=1, pady=10)

Label(decode_frame, text="Decoded Message:").grid(row=3, column=0, sticky=W, pady=5)
text_decoded = Text(decode_frame, height=4, width=45)
text_decoded.grid(row=3, column=1, pady=5)

# ---------- Footer ----------
Label(root, text="Created by Rahul Singh", font=("Arial", 9, "italic")).pack(side=BOTTOM, pady=5)

root.mainloop()
