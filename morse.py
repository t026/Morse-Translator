import tkinter as tk
from tkinter import messagebox
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
print(morsecode_to_english)

def eng_to_m():
    message = etm.get()
    translated = ''
    valid = True
    for i in message:
        if i.upper() not in english_to_morsecode:
            translated += i + ' '
        else:
            translated += english_to_morsecode[i.upper()] + ' '
    if valid and translated:
        messagebox.showinfo(title="English to Morse Translation", message=translated)
    elif valid and not translated:
        messagebox.showerror(title="ERROR", message="Your message was empty.")
    else:
        messagebox.showerror(title="ERROR", message="Your text includes 1 or more non English characters!")

        
def m_to_eng(): 
    message = mte.get()
    y = message.split(" ")
    translated = ''
    print(y)
    valid = True
    for i in y:
        if i not in morsecode_to_english.keys():
            valid = False
        else:
            translated += morsecode_to_english[i]
    if valid and translated:
        messagebox.showinfo(title="Morse to English Translation", message=translated)
    elif valid and not translated:
        messagebox.showerror(title="ERROR", message="Your message was empty.")
    else:
        messagebox.showerror(title="ERROR", message="Your text includes 1 or more non morse characters!")
        
def help():
    messagebox.showinfo(title="Help", message ="In Morse Code, different letters are separated by spaces\nDifferent words are separated by /")

root = tk.Tk()
tk.Label(text="English to Morse").grid(column=0,row=0)
tk.Label(text="Morse to English").grid(column=1,row=0)
etm = tk.Entry()
etm.grid(column=0, row=1)
mte = tk.Entry()
mte.grid(column=1, row=1)
tk.Button(text="Translate English To Morse", command=eng_to_m).grid(column=0, row=2)
tk.Button(text="Translate Morse to English", command=m_to_eng).grid(column=1, row=2)
tk.Button(text="HELP", command=help).grid(column=0, row=3, columnspan=2, sticky='nesw')
root.mainloop()


