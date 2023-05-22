import tkinter as tk
english_to_morsecode = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '-':'-....-','':'',
                    '(':'-.--.', ')':'-.--.-', ' ':'/'}

morsecode_to_english = {v:k for k,v in english_to_morsecode.items()}

def eng_to_m (message):
    translated = ''
    for i in message:
         translated += english_to_morsecode[i.upper()]
         translated += ' '
    print(translated)
    
def m_to_eng (message): 
    y = message.split(" ")
    translated = ''
    print(y)
    for i in y:
        translated += morsecode_to_english[i]
    print(translated)
    
root = tk.Tk()

head = tk.Label(text="English/Morse Translator").grid(column=0, row=0, columnspan=3)
etm = tk.Button(text="Translate English To Morse").grid(column=0, row=1)
mte = tk.Button(text="Translate Morse to English").grid(column=1, row=1)
root.mainloop()