# Import necessary libraries
from tkinter import *  # For GUI components
import pyqrcode  # For generating QR codes
from PIL import ImageTk, Image  # For handling images in Tkinter

# Initialize the main window
root = Tk()
# Set the background color of the window
root.configure(bg='#87CEEB')  # Light sky blue background color

# Load an image to display at the top
try:
    logo_image = Image.open('logo.png')  # Path to your image file
    logo_image = logo_image.resize((400, 200))  # Resize the image if needed
    logo_photo = ImageTk.PhotoImage(logo_image)
except IOError:
    print("Image file not found. Ensure 'logo.png' is in the same directory as your script.")

def generate():
    # Retrieve the values entered by the user
    link_name = name_entry.get()  # Name for the QR code file
    link = link_entry.get()  # URL or link to encode in the QR code

    # Define the filename for the QR code image
    file_name = link_name + ".png"

    # Generate the QR code and save it as a PNG file
    url = pyqrcode.create(link)  # Create the QR code object
    url.png(file_name, scale=8)  # Save the QR code as a PNG file with a scale factor

    # Load the generated QR code image
    image = ImageTk.PhotoImage(Image.open(file_name))

    # Create a label widget to display the QR code image
    image_label = Label(image=image)
    image_label.image = image  # Keep a reference to avoid garbage collection

    # Display the QR code image on the canvas at specified coordinates
    canvas.create_window(200, 450, window=image_label)


# Create a canvas widget for drawing and organizing other widgets
canvas = Canvas(root, width=1200, height=600,bg="#87CEEB" ,bd=0, highlightthickness=0 )
#canvas.pack()
canvas.pack(pady=20)

# Create and place the image at the top of the canvas
if 'logo_photo' in locals():
    logo_label = Label(root, image=logo_photo, bg="#87CEEB")
    canvas.create_window(200, 20, window=logo_label)


# Create and place a label at the top of the canvas
app_label = Label(root, text="QR Code Generator", bg="#87CEEB", fg="blue", font=("Arial", 30))
canvas.create_window(200, 50, window=app_label)

# Create and place labels for user input fields
name_label = Label(root, text="URL Name", bg="#87CEEB")
link_label = Label(root, text="Your URL" ,bg="#87CEEB")

canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

# Create and place entry fields for user input
name_entry = Entry(root,bd=2 ,font=("Arial"))  # Entry for the link name
link_entry = Entry(root, bd=2,font=("Arial"))  # Entry for the link

canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

# Create and place a button that triggers QR code generation
button = Button(text="Generate QR Code", command=generate)
canvas.create_window(200, 230, window=button)

# Start the Tkinter event loop
root.mainloop()



