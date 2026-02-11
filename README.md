# QuickFileSearch

QuickFileSearch is a portable Windows tool for fast file searching based on a previously generated index.
It serves as a high-performance and lightweight alternative to Windows Search, especially for large file collections or network drives.

## Features

### 1. Index Creation

- Recursively scans a selected folder
- Collects:
  - File name
  - Full file path

- Stores the index as `file_index.json` in the same directory as the application
- No internet access required
- No administrator rights required

### 2. Search

All searches are performed exclusively on the generated index (no live filesystem scanning).

Supported options:

- **Exact Search**
  Substring search within the file name

- **Fuzzy Search**
  All entered characters must be present (order does not matter)

- **Include Path in Search**
  Also considers the full file path in the search

### 3. Display

- Two columns:
  - File name
  - Full file path

- On startup, a maximum of **1000 entries** is displayed (performance safeguard)
- Status bar showing:
  - Number of displayed files
  - Total number of indexed files

### 4. Open Files

- Double-click opens the file directly with its associated default application

## Characteristics

- Portable `.exe` possible
- No installation required
- No server dependency
- No background service
- Fully offline capable
- Suitable for:
  - External drives
  - Network drives
  - Project folders
  - Document archives

## Typical Workflow

1. Run `generate_index.exe`
2. Select the target folder
3. The index is created (`file_index.json`)
4. Run `file_viewer.exe`
5. Search and open files
