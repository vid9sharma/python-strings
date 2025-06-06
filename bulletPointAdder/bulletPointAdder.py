#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()


listItems = text.split('\n')
for i in range(len(listItems)):
    item = listItems[i].strip()
    if item != '':
        listItems[i] = '* ' + item

text = '\n'.join(listItems)

pyperclip.copy(text)