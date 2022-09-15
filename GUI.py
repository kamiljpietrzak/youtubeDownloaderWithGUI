import tkinter
from tkinter import filedialog

import customtkinter
import ytDownload

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x400")
app.title("YouTube Downloader by Bubkovsky")


def button_clicked():
    print("Button click")
    ytDownload.download(link.get(), ask_directory())


def ask_directory():
    print("Button click folder")
    directoryPath = filedialog.askdirectory()
    print(directoryPath)
    return directoryPath

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT, text="Wprowadź dane i kliknij przycisk")
label_1.pack(pady=12, padx=10)

link = customtkinter.CTkEntry(master=frame_1, placeholder_text="Wklej link")
link.pack(pady=12, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=button_clicked, text="Pobierz Film")
button_1.pack(pady=12, padx=10)

app.mainloop()
