# Python String Utilities

This repository contains small Python utilities for manipulating text and the clipboard.

## Contents

- **[bulletPointAdder](bulletPointAdder/bulletPointAdder.py)**  
  Adds Wikipedia-style bullet points to each line of text from the clipboard.

- **[mclip](mclip/mclip.py)**  
  A multi-clipboard tool for quickly copying preset phrases to the clipboard.

- **[pigLat](pigLat/pigLat.py)**  
  Converts English text to Pig Latin, preserving punctuation and capitalization.

- **[tablePrinter](tablePrinter/tablePrinter.py)**  
  Prints a list of lists in a well-formatted table with each column right-justified.

## Usage

Each tool can be run directly with Python or via the provided `.bat` files on Windows.

### Example: bulletPointAdder

1. Copy some lines of text to your clipboard.
2. Run:
   ```
   bulletPointAdder\bulletPointAdder.bat
   ```
3. The clipboard will now contain the same lines, each prefixed with `* `.

### Example: mclip

1. Run:
   ```
   mclip\mclip.bat agree
   ```
2. The phrase for "agree" will be copied to your clipboard.

### Example: pigLat

1. Run:
   ```
   pigLat\pigLat.bat
   ```
2. Enter a message when prompted. The Pig Latin translation will be displayed.

### Example: tablePrinter

1. Edit `tablePrinter/tablePrinter.py` to set your own table data or use the sample data.
2. Run:
   ```
   tablePrinter\tablePrinter.bat
   ```
3. The formatted table will be printed to the console.

## Requirements

- Python 3.x
- [pyperclip](https://pypi.org/project/pyperclip/) (install with `pip install pyperclip`) *(for clipboard utilities)*

---

These scripts are for learning and experimenting with string manipulation in Python.