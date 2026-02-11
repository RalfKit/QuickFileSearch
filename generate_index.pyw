import os
import sys
import json
from tkinter import filedialog, Tk, messagebox

# Tkinter-Hauptfenster verstecken
root = Tk()
root.withdraw()

# Ordner auswählen, der gescannt werden soll
folder = filedialog.askdirectory(title="Ordner zum Scannen auswählen")
if not folder:
    messagebox.showinfo("Abbruch", "Kein Ordner ausgewählt")
    exit()

files_list = []
for root_dir, dirs, files in os.walk(folder):
    for file in files:
        full_path = os.path.join(root_dir, file)
        files_list.append({
            "Name": file,
            "FullName": full_path
        })

# JSON immer im gleichen Ordner wie die .exe speichern
if getattr(sys, "frozen", False):
    # Wird ausgeführt als PyInstaller .exe
    current_dir = os.path.dirname(sys.executable)
else:
    # Wird als normales .py Script ausgeführt
    current_dir = os.path.dirname(os.path.abspath(__file__))

json_path = os.path.join(current_dir, "file_index.json")

# JSON schreiben
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(files_list, f, ensure_ascii=False, indent=2)

messagebox.showinfo("Fertig", f"{len(files_list)} Dateien indexiert.\nIndex gespeichert unter:\n{json_path}")
