"""
Day 3/75
Personal Search Engine
"""

import os
import json
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from PIL import Image, ImageTk


# -----------------------------
# Constants
# -----------------------------

INDEX = "index.json"
data = []


# -----------------------------
# Scan Files
# -----------------------------

def scan():
    global data

    folder = filedialog.askdirectory()

    if not folder:
        return

    status.set("Scanning...")
    app.update_idletasks()

    data = []

    for root, _, files in os.walk(folder):

        for filename in files:

            path = os.path.join(root, filename)

            try:
                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as file:

                    content = file.read().lower()

            except (PermissionError, OSError, UnicodeDecodeError):
                content = ""

            extension = os.path.splitext(filename)[1].lstrip(".").lower()

            data.append({
                "name": filename.lower(),
                "path": path,
                "type": extension,
                "content": content
            })

    try:
        with open(INDEX, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)

        status.set(f"{len(data)} files indexed")

    except OSError:
        status.set("Unable to save index")


# -----------------------------
# Load Existing Index
# -----------------------------

def load():
    global data

    try:

        with open(INDEX, "r", encoding="utf-8") as file:
            stored_data = json.load(file)

        data = [
            item
            for item in stored_data
            if os.path.exists(item["path"])
        ]

        status.set(f"{len(data)} files loaded")

        search()

    except (FileNotFoundError, json.JSONDecodeError, OSError):

        data = []
        status.set("No index found")


# -----------------------------
# Search
# -----------------------------

def search(event=None):

    query = search_var.get().strip().lower()
    file_type = filter_var.get().lower()

    listbox.delete(0, tk.END)

    result_count = 0

    for item in data:

        if not os.path.exists(item["path"]):
            continue

        name_match = query in item["name"]
        content_match = query in item["content"]

        if name_match or content_match:

            if file_type == "all" or item["type"] == file_type:

                listbox.insert(tk.END, item["path"])
                result_count += 1

    status.set(f"{result_count} results")


# -----------------------------
# Preview Selected File
# -----------------------------

def preview(event=None):

    preview_box.delete("1.0", tk.END)
    preview_box.image = None

    try:

        path = listbox.get(tk.ACTIVE)

        if not path or not os.path.exists(path):
            return

        extension = os.path.splitext(path)[1].lower()

        # Image preview
        if extension in [".jpg", ".jpeg", ".png"]:

            image = Image.open(path)

            image.thumbnail((500, 500))

            img = ImageTk.PhotoImage(image)

            preview_box.image_create(
                tk.END,
                image=img
            )

            preview_box.image = img

        # Text preview
        else:

            with open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as file:

                content = file.read()

            preview_box.insert(
                tk.END,
                content
            )

    except (OSError, PermissionError):

        preview_box.insert(
            tk.END,
            "Preview Not Available"
        )


# -----------------------------
# Open File
# -----------------------------

def open_file(event=None):

    try:

        path = listbox.get(tk.ACTIVE)

        if os.path.exists(path):
            os.startfile(path)

    except OSError:
        pass


# -----------------------------
# Main Window
# -----------------------------

app = ttk.Window(
    themename="darkly"
)

app.title("Smart Search")
app.geometry("1300x750")


# -----------------------------
# Variables
# -----------------------------

search_var = tk.StringVar()

filter_var = tk.StringVar(
    value="All"
)

status = tk.StringVar(
    value="Ready"
)


# -----------------------------
# Top Frame
# -----------------------------

top = ttk.Frame(app)

top.pack(
    fill="x",
    padx=10,
    pady=10
)


# -----------------------------
# Search Entry
# -----------------------------

search_entry = ttk.Entry(
    top,
    textvariable=search_var,
    font=("Arial", 13)
)

search_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
)

search_entry.bind(
    "<KeyRelease>",
    search
)


# -----------------------------
# Scan Button
# -----------------------------

ttk.Button(
    top,
    text="Scan",
    command=scan
).pack(
    side="left",
    padx=5
)


# -----------------------------
# Load Button
# -----------------------------

ttk.Button(
    top,
    text="Load",
    command=load
).pack(
    side="left",
    padx=5
)


# -----------------------------
# File Type Filter
# -----------------------------

combo_box = ttk.Combobox(
    top,
    textvariable=filter_var,
    values=[
        "All",
        "text",
        "png",
        "jpg",
        "jpeg",
        "pdf",
        "py",
        "txt",
        "json",
        "html",
        "css",
        "js"
    ],
    state="readonly"
)

combo_box.pack(
    side="right",
    padx=5
)

combo_box.bind(
    "<<ComboboxSelected>>",
    search
)


# -----------------------------
# Main Content Frame
# -----------------------------

main = ttk.Frame(app)

main.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=5
)


main.columnconfigure(
    0,
    weight=4
)

main.columnconfigure(
    2,
    weight=6
)

main.rowconfigure(
    0,
    weight=1
)


# -----------------------------
# Search Results Listbox
# -----------------------------

listbox = tk.Listbox(
    main,
    font=("Consolas", 11)
)

listbox.grid(
    row=0,
    column=0,
    sticky="nsew"
)


# -----------------------------
# Vertical Scrollbar - Listbox
# -----------------------------

list_scrollbar = ttk.Scrollbar(
    main,
    command=listbox.yview
)

list_scrollbar.grid(
    row=0,
    column=1,
    sticky="ns"
)

listbox.config(
    yscrollcommand=list_scrollbar.set
)


# -----------------------------
# Horizontal Scrollbar - Listbox
# -----------------------------

list_horizontal_scrollbar = ttk.Scrollbar(
    main,
    command=listbox.xview,
    orient="horizontal"
)

list_horizontal_scrollbar.grid(
    row=1,
    column=0,
    sticky="ew"
)

listbox.config(
    xscrollcommand=list_horizontal_scrollbar.set
)


# -----------------------------
# Preview Box
# -----------------------------

preview_box = tk.Text(
    main,
    wrap="none",
    font=("Consolas", 11)
)

preview_box.grid(
    row=0,
    column=2,
    sticky="nsew",
    padx=(10, 0)
)


# -----------------------------
# Vertical Scrollbar - Preview
# -----------------------------

preview_scrollbar = ttk.Scrollbar(
    main,
    command=preview_box.yview
)

preview_scrollbar.grid(
    row=0,
    column=3,
    sticky="ns"
)

preview_box.config(
    yscrollcommand=preview_scrollbar.set
)


# -----------------------------
# Horizontal Scrollbar - Preview
# -----------------------------

preview_horizontal_scrollbar = ttk.Scrollbar(
    main,
    command=preview_box.xview,
    orient="horizontal"
)

preview_horizontal_scrollbar.grid(
    row=1,
    column=2,
    sticky="ew"
)

preview_box.config(
    xscrollcommand=preview_horizontal_scrollbar.set
)


# -----------------------------
# Listbox Events
# -----------------------------

listbox.bind(
    "<ButtonRelease-1>",
    preview
)

listbox.bind(
    "<Double-Button-1>",
    open_file
)


# -----------------------------
# Status Bar
# -----------------------------

ttk.Label(
    app,
    textvariable=status
).pack(
    fill="x",
    padx=10,
    pady=5
)


# -----------------------------
# Start Application
# -----------------------------

app.mainloop()