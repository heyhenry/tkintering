# sourced example from chatgpt query * repurposed for own use

from PIL import Image, ImageTk
import tkinter as tk

def resize_image(image_path, new_size):
    # Open the image using PIL
    with Image.open(image_path) as img:
        # Resize the image using Image.LANCZOS for high-quality resizing
        resized_img = img.resize(new_size, Image.LANCZOS)
        return resized_img

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Image Resizing Example")

    # Path to your image file
    image_path = 'opened_eye.png'
    
    # Resize the image
    new_size = (15, 20)
    resized_img = resize_image(image_path, new_size)

    # Convert the resized image to a PhotoImage object
    photo_img = ImageTk.PhotoImage(resized_img)

    # Create a Label to display the image
    label = tk.Label(root, image=photo_img)
    label.pack()

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

