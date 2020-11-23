#############################
# rotating_rotator
#############################
import time
from csv import writer
from iterative_julius import *
from writer import *
from tkinter import filedialog
from tkinter import *
from cryptography.fernet import Fernet

# FUNCTIONS
# 
# 
# 
def key_generator():
	root = Tk()
	root.configure(bg="aqua")
	root.geometry("450x300")
	root.title("Key Generator")


	def saveKey():
		create_file = filedialog.asksaveasfile(mode='wb', defaultextension=".key")
		key = Fernet.generate_key()
		global active_fernet_key
		active_fernet_key = create_file.name
		create_file.write(key)
		create_file.close()

	def saveNumKey():
		create_file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
		global active_position_key
		active_position_key = create_file.name
		create_file.write('w')
		create_file.close()


	heading = Label(text="Generate a Fernet Key and a NumKey with the button below:", bg="aqua", fg="black", font="10", width="450", height="3").pack()
	button1 = Button(root, text="Generate Fernet Key", command=saveKey, width="30", height="3").pack(side=TOP, pady=8)
	button1 = Button(root, text="Generate Position Key", command=saveNumKey, width="30", height="3").pack(side=TOP, pady=8)
	button3 = Button(root, text="Select Keys", command=root.destroy, width="10", height="1").pack(side=RIGHT, padx=100)

	root.mainloop()


def open_fernet():
		open_file_select = filedialog.askopenfilename(filetypes=[("Key files", "*.key")])
		global active_fernet_key
		active_fernet_key = open_file_select

def open_position():
		open_file_select = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
		global active_position_key
		active_position_key = open_file_select


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


def ask_for_keys():
	root = Tk()
	root.configure(bg="aqua")
	root.geometry("450x250")
	root.title("Select Key")
	heading = Label(text="Do you need to generate keys?", bg="aqua", fg="black", font="10", width="450", height="3").pack()

	generate_keys = Button(root, text="Yes", command=lambda:[root.destroy(), key_generator()], width="30", height="3").pack(side=TOP, pady=8)
	select_keys = Button(root, text="No", command=lambda:[root.destroy(), choose_key()], width="30", height="3").pack(side=TOP, pady=8)

	root.mainloop()

def unlock_file():
	with open(active_fernet_key, 'rb') as mykey:
		key = mykey.read()

	f = Fernet(key)
	with open(active_position_key, 'rb') as encrypted_file:
		encrypted = encrypted_file.read()
		decrypted = f.decrypt(encrypted)
	with open(active_position_key, 'wb') as decrypted_file:
		decrypted_file.write(decrypted)

def lock_file():
	with open(active_fernet_key, 'rb') as mykey:
		key = mykey.read()

	f = Fernet(key)

	with open(active_position_key, 'rb') as original_file:
		original = original_file.read()

	encrypted = f.encrypt(original)

	with open (active_position_key, 'wb') as encrypted_file:
		encrypted_file.write(encrypted)


# define the cipher
#iterative_julius.py - but don't call it

# Ask if they have keys, open/generate

print("Initializing script")

ask_for_keys()

print("Keys loaded")
# try to decode position key

try:
	unlock_file()
	print("Unlocking Position Key")
except:
	pass

# open text editor and write text file
print("Text editor opened")
time.sleep(1)
create_document()


# append to position key
with open(active_position_key, 'a+') as write_obj:
	csv_writer = writer(write_obj)
	csv_writer.writerow(keystring)

print("Position Key Updated")


# encode position key

lock_file()
print("Key Locked")

# append to another document (optional)
