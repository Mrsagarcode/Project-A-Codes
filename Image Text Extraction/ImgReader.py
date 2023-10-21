import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pytesseract

def extract_text_from_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)

        text_display.config(state=tk.NORMAL)
        text_display.delete(1.0, tk.END)
        text_display.insert(tk.END, text)
        text_display.config(state=tk.DISABLED)

        image.thumbnail((250, 250))
        img_tk = ImageTk.PhotoImage(image)
        image_label.config(image=img_tk)
        image_label.image = img_tk

def save_text_to_file():
    text_to_save = text_display.get(1.0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_to_save)

# Create the main window
root = tk.Tk()
root.title("Text Recognition App")

# Create the widgets
upload_button = tk.Button(root, text="Upload Image", command=extract_text_from_image)
image_label = tk.Label(root)
text_display = tk.Text(root, wrap=tk.WORD, font=("Arial", 12), state=tk.DISABLED)
save_button = tk.Button(root, text="Save Text", command=save_text_to_file)

# Layout the widgets
upload_button.pack(pady=10)
image_label.pack(pady=10)
text_display.pack(pady=10)
save_button.pack(pady=5)

# Run the main loop
root.mainloop()
