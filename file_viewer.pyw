import json
import os
import sys
from tkinter import Tk, Entry, Button, Label, Checkbutton, BooleanVar, Scrollbar, RIGHT, Y, LEFT, BOTH, Frame, messagebox
from tkinter import ttk

MAX_INITIAL_DISPLAY = 1000  # Begrenzung beim Start

# JSON-Pfad im gleichen Ordner wie die .exe oder .py
if getattr(sys, "frozen", False):
    current_dir = os.path.dirname(sys.executable)
else:
    current_dir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(current_dir, "file_index.json")

if not os.path.exists(json_path):
    messagebox.showerror("Datei fehlt", f"{json_path} nicht gefunden.\nBitte zuerst generate_index.py ausführen.")
    exit()

with open(json_path, "r", encoding="utf-8") as f:
    files = json.load(f)

# GUI
root = Tk()
root.title("QuickFileSearch")
root.geometry("900x550")

Label(root, text="Suche:").pack()
search_entry = Entry(root, width=50)
search_entry.pack()

fuzzy_var = BooleanVar(value=False)
path_var = BooleanVar(value=False)

Checkbutton(root, text="Ungenaue Suche", variable=fuzzy_var).pack()
Checkbutton(root, text="Pfad auch durchsuchen", variable=path_var).pack()

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(frame, columns=("Name", "Pfad"), show="headings", yscrollcommand=scrollbar.set)
tree.heading("Name", text="Dateiname")
tree.heading("Pfad", text="Pfad")
tree.column("Name", width=300)
tree.column("Pfad", width=500)
tree.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=tree.yview)

status_label = Label(root)
status_label.pack(pady=5)

def update_status(displayed, total):
    status_label.config(text=f"Angezeigt: {displayed} / Gesamt: {total}")

def search_files():
    term = search_entry.get().lower()
    fuzzy = fuzzy_var.get()
    search_path = path_var.get()

    results = []
    for f in files:
        haystack = f["Name"].lower()
        if search_path:
            haystack += f" {f['FullName'].lower()}"

        if fuzzy:
            letters = list(term)
            if all(c in haystack for c in letters):
                results.append(f)
        else:
            if term in haystack:
                results.append(f)

    tree.delete(*tree.get_children())
    for f in results:
        tree.insert("", "end", values=(f["Name"], f["FullName"]))

    update_status(len(results), len(files))

def open_file(event=None):
    selected = tree.selection()
    if selected:
        item = tree.item(selected[0])
        file_path = item["values"][1]
        os.startfile(file_path)

tree.bind("<Double-1>", open_file)

Button(root, text="Suche starten", command=search_files).pack(pady=5)

# ---- Initialanzeige (max. 1000 Dateien) ----
initial_files = files[:MAX_INITIAL_DISPLAY]

for f in initial_files:
    tree.insert("", "end", values=(f["Name"], f["FullName"]))

update_status(len(initial_files), len(files))

root.mainloop()
