from tkinter import * 
from tkinter import messagebox
import base64
import os

def decrypt():
    print("")

def encrypt():
    password=code.get()

    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("encrytion")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message=text1.get(1.0, END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")


        Label(screen2,text="ENCRYPT", font=("arial", 20), fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption", "Input password")
    elif password != "1234":
        messagebox.showerror("encryption", "Invalid password")

def main_secreen():

    global screen
    global code
    global text1
    
    screen=Tk()
    screen.geometry("375x398")

    #icon
    image_icon=PhotoImage(file="keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    

    Label(text="Enter text for encryption and decryption", fg="black", font=("calbri",13)).place(x=10, y=170)
    text1=Text(font=("roboto",20), bg="white", relief=GROOVE, wrap=WORD, bd=0)

    Label(text="Enter secret key encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)

    code=StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25)).place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0).place(x=10, y=250)
    Button(text="RESET", height="2", width=23, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)


    screen.title("PctApp")

    screen.mainloop()

main_secreen()