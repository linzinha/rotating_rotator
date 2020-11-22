#############################
# rotating_rotator
#############################
import time
from csv import writer
from keygen import *
from iterative_julius import *
from writer import *
from tkinter import filedialog
from tkinter import *
from cryptography.fernet import Fernet



# First define the cipher
#iterative_julius.py - but don't call it

# Second Ask if they have keys??
key_check = input("Do you have your keys? y/n \n")
if key_check == "n":
	time.sleep(1)
	key_generator()

else:
	pass

# Third Set Keys
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

print("Select your key set")
time.sleep(1)
choose_key()
# Fourth decode position key
def unlock_file():
	with open(active_fernet_key, 'rb') as mykey:
		key = mykey.read()

	f = Fernet(key)
	with open(active_position_key, 'rb') as encrypted_file:
		encrypted = encrypted_file.read()
		decrypted = f.decrypt(encrypted)
	with open(active_position_key, 'wb') as decrypted_file:
		decrypted_file.write(decrypted)

try:
	unlock_file()
except:
	pass
# Fifth open text editor and write text file

print("Write your text")
time.sleep(1)
create_document()

# Sixth append to position key

with open(active_position_key, 'a+') as write_obj:
	csv_writer = writer(write_obj)
	csv_writer.writerow(keystring)


# Seventh encode position key
def lock_file():
	with open(active_fernet_key, 'rb') as mykey:
		key = mykey.read()

	f = Fernet(key)

	with open(active_position_key, 'rb') as original_file:
		original = original_file.read()

	encrypted = f.encrypt(original)

	with open (active_position_key, 'wb') as encrypted_file:
		encrypted_file.write(encrypted)

    
lock_file()

# Eighth append to another document (optional)
