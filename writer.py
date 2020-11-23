from tkinter import filedialog
from tkinter import *
from iterative_julius import *

def create_document():
	root = Tk()
	root.configure(bg="aqua")
	root.geometry("450x700")
	root.title("Write Text")
	my_text = Text(root, width=40, height=10, font=("Helvetica", 16))
	my_text.pack(pady=10)
	encrypted_text = Text(root, width=40, height=10, font=("Helvetica", 16))
	encrypted_text.pack(pady=10)


	def encryptDoc():
		content = my_text.get(1.0, END)
		content = encryption(content)
		encrypted_text.insert(END, content)

	def saveDoc():
		write_file = filedialog.asksaveasfilename(initialdir="~", title="Save Document", defaultextension=".txt")
		write_file = open(write_file, 'w')
		write_file.write(encrypted_text.get(1.0, END))

	heading = Label(text="Create or Open File:", bg="aqua", fg="black", font="10", width="450", height="1").pack()
	encrypt_button = Button(root, text="Encrypt Text", command=encryptDoc, width="30", height="3")
	encrypt_button.pack(pady=10)
	save_button = Button(root, text="Save File", command=lambda:[saveDoc(), root.destroy()], width="30", height="3")
	save_button.pack(side=TOP, pady=4)

	def open_file():
		append_to = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

	def forget():
		if chkValue == False:
			open_button.pack_forget()
			save_button.pack()
		else:
			open_button.pack()
			save_button.pack_forget()


	chkValue = BooleanVar() 
	chkValue.set(False)

	chkExample = Checkbutton(root, text='Append to existing file?', var=chkValue, command=forget) 
	chkExample.pack(pady=2)
	# chkExample.toggle()

	open_button = Button(root, text="Open", command=open_file, width="30", height="3")
	open_button.pack(side=TOP, pady=10)
	open_button.pack_forget()


	root.mainloop()

create_document()