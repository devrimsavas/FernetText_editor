from tkinter import *
from cryptography.fernet import Fernet
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox


root=Tk()
root.geometry("800x500")
root.title("FERNET TEXT EDITOR")
root.config(bg="beige")

###ATTENTION LINES BELOW must be activate to create your own key. otherwise program will not start"
#key=Fernet.generate_key()
#with open("key.key","wb") as key_file:
    #key_file.write(key)

#key_file= open("key.key", "rb")
#key=key_file.read()
global key
global cripto_flag
cripto_flag=False #the text is plain or encrypted

def open_key_file():
    global key
    root.filename=filedialog.askopenfilename(initialdir="/python/kripto", title="Select a Key File", filetypes=(("key files", "*.key"),("all files", "*.")))
    key_file=open(root.filename, "rb")
    key=key_file.read()

def open_file_2():
    text_input_box.delete("1.0", END)
    root.filename=filedialog.askopenfilename(initialdir="/python/kripto", title="Select a Text File", filetypes=(("Text Files", "*.txt"),("all files", "*.")))
    my_file=open(root.filename, "r", encoding="UTF-8")
    text_input_box.insert("1.0", my_file.read())

def open_file():
    text_input_box.delete("1.0", END)
    root.filename = filedialog.askopenfilename(initialdir="/python/kripto", title="Select a Text File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if root.filename:
        with open(root.filename, "r", encoding="UTF-8") as file:
            file_content = file.read()
            text_input_box.insert("1.0", file_content)

def save_file():
    root.filename = filedialog.asksaveasfile(
        initialdir="/python/kripto",
        defaultextension=".txt",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if root.filename is not None:
        file_content = text_input_box.get("1.0", END)
        root.filename.write(file_content)
        root.filename.close()


def encrypted_file():
    global key
    try:
        f = Fernet(key)
        file_data = text_input_box.get("1.0", END)
        arr = file_data.encode("utf-8")  # Convert text to bytes
        encrypted_data = f.encrypt(arr)
        text_input_box.delete("1.0", END)
        text_input_box.insert("1.0", encrypted_data.decode("utf-8"))  # Convert bytes back to text
        cripto_flag=True
        if cripto_flag:
            
            cripto_flag_label.config(text="Text Encrypted",fg="red",bg="green")
        
    except Exception as e:
        messagebox.showwarning("KEY REQUIRED", str(e))

def decrypted_file():
    global key
    try: 
        f = Fernet(key)
        file_data = text_input_box.get("1.0", END)
        arr = file_data.encode("utf-8")  # Convert text to bytes
        decrypted_data = f.decrypt(arr)
        text_input_box.delete("1.0", END)
        text_input_box.insert("1.0", decrypted_data.decode("utf-8"))  # Convert bytes back to text
        cripto_flag=False
        if not cripto_flag:

            cripto_flag_label.config(text="Text Decrypted",fg="white",bg="blue")
    except Exception as e:
        messagebox.showwarning("Decryption Error", "No Valid Key or Already Decrypted")


text_input_box=Text(root, width=83, height=20, borderwidth=2, wrap=WORD, font=("Arial", 12))
text_input_box.place(x=20, y=30)


#BUTTON SAVE

save_button=Button(root, text="SAVE",width=16, command=save_file)
save_button.place(x=15,y=400)

#BUTTON ENCRYPTED

encrypted_button=Button(root, text="ENCRYPTED", width=16, command=encrypted_file)
encrypted_button.place(x=140,y=400)

#BUTTON DECRYPTED

decrypted_button=Button(root, text="DECRYPTED",width=16, command=decrypted_file)
decrypted_button.place(x=265,y=400)

#BUTTON OPEN FILE

open_file_button=Button(root, text="OPEN FILE",width=16, command=open_file)
open_file_button.place(x=390,y=400)

# PROVIDE A KEY

enter_key_button=Button(root, text="OPEN KEY FILE",width=16, command=open_key_file)
enter_key_button.place(x=515, y=400)

cripto_flag_label=Label(root,width=20,text="PLAIN TEXT",fg="white",bg="blue" ,font=("Arial",14),borderwidth=2)
cripto_flag_label.place(x=250,y=450)

root.mainloop()
