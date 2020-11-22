from tkinter import filedialog
from tkinter import *
from cryptography.fernet import Fernet


# Opens a file and sets path for each key type. Redundancy issues 
def open_fernet():
		open_file_select = filedialog.askopenfilename()
		global active_fernet_key
		active_fernet_key = open_file_select

def open_position():
		open_file_select = filedialog.askopenfilename()
		global active_position_key
		active_position_key = open_file_select

# Opens the tkinter dialog gui
def choose_key():
	root = Tk()
	root.configure(bg="aqua")
	root.geometry("450x250")
	root.title("Select Key")

	heading = Label(text="Select which key set you'd like to use", bg="aqua", fg="black", font="10", width="450", height="3").pack()

	choose_fernet_key_button = Button(root, text="Define Fernet Key", command=open_fernet, width="30", height="3").pack(side=TOP, pady=8)

	choose_position_key_button = Button(root, text="Define Position Key", command=open_position, width="30", height="3").pack(side=TOP, pady=8)

	exit_button = Button(root, text="Define Keys", command=root.destroy, width="10", height="1").pack(side=RIGHT, padx=100)


	root.mainloop()