# QuickFileSearch

## 📌 Overview

QuickFileSearch is a lightweight, portable Windows tool for fast file searching based on a pre-generated index.

It was designed as an alternative to slow native search solutions (e.g. Windows Search) in environments with large file collections, external drives, or network storage.

Instead of scanning the filesystem at runtime, QuickFileSearch uses a prebuilt JSON index for instant search performance.

## ✨ Features

### 📦 Indexing

- Recursive folder scan
- Collects file names and full file paths
- Generates a local `file_index.json`
- Fully offline process
- No admin rights required

### 🔎 Search Engine

- Fast lookup based on prebuilt index (no live filesystem scanning)
- Exact substring search
- Lightweight fuzzy search (character-based matching)
- Optional path-based search

### 🖥️ UI

- Simple desktop GUI (Tkinter)
- Two-column layout:
  - File name
  - Full file path

- Double-click to open files via default system application
- Initial display limit (1000 entries) for performance safety
- Live status indicator (displayed vs total indexed files)

## ⚙️ Workflow

1. Run `generate_index.exe`
2. Select target folder (local, external, or network drive)
3. Index is generated (`file_index.json`)
4. Run `file_viewer.exe`
5. Search and open files instantly

## 🚀 Characteristics

- Portable `.exe` builds available
- Fully offline capable
- No installation required
- No background services
- Works with:
  - External drives
  - Network shares
  - Large project directories
  - Archive folders

## 🧠 Concept

QuickFileSearch was created to explore how a pre-indexed search system can outperform traditional filesystem search in large-scale directories.

The core idea is to shift expensive filesystem traversal into a single indexing step, enabling near-instant search experiences afterwards.

## 🧱 Architecture

- `generate_index.pyw`
  → Builds file index from filesystem

- `file_viewer.pyw`
  → Loads index and provides search UI

- `file_index.json`
  → Lightweight search database

## 🛠️ Build

```bash
build.bat
```

Outputs:

- `generate_index.exe`
- `file_viewer.exe`

## 📌 Limitations

- No real-time filesystem updates
- Index must be regenerated after file changes
- Fuzzy search is lightweight (not semantic)
- Performance depends on initial indexing time

## 📦 Tech Stack

- Python
- Tkinter (UI)
- PyInstaller (packaging)
- JSON-based index storage

## 📌 Status

This project is no longer actively developed.

It is a prototype demonstrating indexed file search as an alternative to real-time filesystem scanning.

## 🤝 Notes

This project was created as an experimental solution for performance-focused file search in large or external storage environments.
