#! python3
# bulletPointAdder.py adds wikipedia bullet points to the start of each line of text on the clipboard

import pyperclip

text = pyperclip.paste()

# separate lines and add stars

linesOfText = text.split('\n')

for lines in range(len(linesOfText)):
    linesOfText[lines] = '* ' + linesOfText[lines]

text = '\n'.join(linesOfText)

pyperclip.copy(text)

