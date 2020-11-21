from tkinter import *
from tkinter import filedialog
from cryptography.fernet import Fernet

root = Tk()
root.configure(bg="aqua")
root.geometry("450x300")
root.title("Key Generator")


def saveKey():
    f = filedialog.asksaveasfile(mode='wb', defaultextension=".key")
    key = Fernet.generate_key()
    f.write(key)
    f.close()

def saveNumKey():
    g = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    g.write()
    g.close()


heading = Label(text="Generate a Fernet Key and a NumKey with the button below:", bg="aqua", fg="black", font="10", width="450", height="3").pack()
button1 = Button(root, text="Generate Key", command=saveKey, width="30", height="3").pack(side=TOP, pady=8)
button1 = Button(root, text="Generate NumKey", command=saveNumKey, width="30", height="3").pack(side=TOP, pady=8)

button3 = Button(root, text="Exit", command=root.destroy, width="10", height="1").pack(side=RIGHT, padx=100)

root.mainloop()

