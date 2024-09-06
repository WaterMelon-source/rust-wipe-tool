import random
import tkinter
from tkinter import font
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("300x300")
app.resizable(width=False, height=False)
app.title("RMSG")

# Input
Input = customtkinter.CTkEntry(master=app, text="")
Input.place(relx=0.75, rely=0.09, anchor=tkinter.CENTER)


def button_function():
    Input.delete(0, tkinter.END)
    Input.insert(0, random.randint(100000, 999999))


# Generate button
gbutton = customtkinter.CTkButton(master=app,
                                  text="Generate",
                                  fg_color="#33FF00",
                                  text_color="#FFF",
                                  command=button_function)
gbutton.place(relx=0.75, rely=0.22, anchor=tkinter.CENTER)

# Name text
ntext = customtkinter.CTkLabel(master=app, text="Rust Wipe:")
size = font.Font(size=15)
ntext['font'] = size
ntext.place(relx=0.2, rely=0.1, anchor=tkinter.CENTER)

# Punkt Text 1
text1 = customtkinter.CTkLabel(master=app, text="1. Generate Seed")
size = font.Font(size=10)
text1['font'] = size
text1.place(relx=0.22, rely=0.22, anchor=tkinter.CENTER)

# Punkt Text 2
text2 = customtkinter.CTkLabel(master=app, text="2. Write in console restart")
size = font.Font(size=10)
text2['font'] = size
text2.place(relx=0.3, rely=0.32, anchor=tkinter.CENTER)

# Punkt Text 3
text3 = customtkinter.CTkLabel(master=app, text="3. Rewrite a new seed")
size = font.Font(size=10)
text3['font'] = size
text3.place(relx=0.26, rely=0.42, anchor=tkinter.CENTER)

# Punkt Text 4
text4 = customtkinter.CTkLabel(master=app, text="4. Delete player.blueprints.3.db")
size = font.Font(size=10)
text4['font'] = size
text4.place(relx=0.35, rely=0.52, anchor=tkinter.CENTER)

# Punkt Text 5
text5 = customtkinter.CTkLabel(master=app, text="5. Start server")
size = font.Font(size=10)
text5['font'] = size
text5.place(relx=0.19, rely=0.62, anchor=tkinter.CENTER)

# Down label
text3 = customtkinter.CTkLabel(master=app, text="By RustChecker.com", text_color="#FFF", bg_color="#33FF00")
size = font.Font(size=24)
text3['font'] = size
text3.place(relx=0.5, rely=0.935, anchor=tkinter.CENTER)

app.mainloop()
