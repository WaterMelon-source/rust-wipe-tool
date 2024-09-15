import seed

from dependencies.config import *
from customtkinter import *
from PIL import ImageTk

# Setup
set_appearance_mode("System")  # Modes: system (default), light, dark

app = CTk()
app.geometry("600x350")
app.resizable(width=False, height=False)
app.title("Rust Wipe Tool")
app.iconbitmap('dependencies/rust.ico')

# Data
seed_value, size, level, pil_image = seed.get_map()

# Functions
def button_function():
    seed_value, size, level, pil_image = seed.get_map()
    if seed_value is not None:
        input_box.delete(0, END)
        input_box.insert(0, seed_value)

        if pil_image is not None:
            tk_image = ImageTk.PhotoImage(pil_image)
            map_label .configure(image=tk_image)
            map_label .image = tk_image

        # Update Map Info
        map_info_label.configure(text=f"{level}; Size: {size}")

def place_paragraph(text, rely):
    text = CTkLabel(master=app, text=text, font=text_font)
    text.place(relx=0.05, rely=rely, anchor='w')

# Input box
input_box = CTkEntry(master=app)
input_box.place(relx=0.05, rely=0.31, anchor='w')
input_box.insert(0, seed_value)

# Generate button
g_button = CTkButton(master=app,
                    text="Generate",
                    hover_color=SECOND_COLOR,
                    fg_color=MAIN_COLOR,
                    text_color="#FFF",
                    command=button_function)
g_button.place(relx=0.05, rely=0.41, anchor='w')

# Font setup
title_font = CTkFont(family=FONT, size=TITLE_TEXT_SIZE, weight="bold")
text_font = CTkFont(family=FONT, size=PARAGRAPHS_FONT_SIZE)

# Title
title_text = CTkLabel(master=app, text="Rust Wipe:", font=title_font)
title_text.place(relx=0.05, rely=0.1, anchor='w')

# Paragraphs
place_paragraph("1. Generate Seed", 0.2)
place_paragraph("2. Write in console quit", 0.53)
place_paragraph("3. Rewrite a new seed", 0.63)
place_paragraph("4. Delete player.blueprints.3.db", 0.73)
place_paragraph("5. Start server", 0.83)

# Map
tk_image = ImageTk.PhotoImage(pil_image) if pil_image else None
map_label = CTkLabel(master=app, image=tk_image, text='')
map_label.place(relx=0.7, rely=0.42, anchor=CENTER)

# Map Info
map_info_label = CTkLabel(master=app, text=f"{level}; Size: {size}", font=text_font)
map_info_label.place(relx=0.7, rely=0.83, anchor=CENTER)

# Footer
bottom_text = CTkLabel(master=app, text="Rust Wipe Tool - Your Ultimate Map Generator", text_color="#FFF", bg_color=MAIN_COLOR, font=CTkFont(size=12))
bottom_text.place(relx=0.5, rely=0.96, relwidth=1, anchor=CENTER)

app.mainloop()
