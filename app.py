import tkinter as tk
import requests
import time
from tkinter import messagebox

def get_joke(language):
    url = f"https://v2.jokeapi.dev/joke/Any?lang={language}"
    response = requests.get(url)
    joke_data = response.json()
    
    if joke_data["type"] == "single":
        joke = joke_data["joke"]
        messagebox.showinfo("Chiste", joke)
    else:
        setup = joke_data["setup"]
        delivery = joke_data["delivery"]
        messagebox.showinfo("Chiste", setup)
        time.sleep(1)
        messagebox.showinfo("Chiste", delivery)

def on_english():
    get_joke("en")

def on_spanish():
    get_joke("es")

# Interfaz gráfica
root = tk.Tk()
root.title("Chistes con JokeAPI")
root.geometry("300x150")

label = tk.Label(root, text="Elige el idioma del chiste:")
label.pack(pady=10)

btn_en = tk.Button(root, text="Inglés", command=on_english)
btn_en.pack(pady=5)

btn_es = tk.Button(root, text="Español", command=on_spanish)
btn_es.pack(pady=5)

root.mainloop()
