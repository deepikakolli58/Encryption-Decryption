from tkinter import *
from tkinter import messagebox
import base64


def decrypt():
    password = code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END).strip()
        if message:
            try:
                decode_message = message.encode("ascii")
                base64_bytes = base64.b64decode(decode_message)
                decrypted_message = base64_bytes.decode("ascii")

                Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
                text2 = Text(screen2, font="Roboto 10", bg="White", relief=GROOVE, wrap=WORD, bd=0)
                text2.place(x=10, y=40, width=380, height=150)

                text2.insert(END, decrypted_message)
            except Exception as e:
                messagebox.showerror("Decryption", f"An error occurred: {str(e)}")
        else:
            messagebox.showerror("Decryption", "No message to decrypt")
    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    else:
        messagebox.showerror("Decryption", "Invalid Password")


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0, END).strip()
        if message:
            encode_message = message.encode("ascii")
            base64_bytes = base64.b64encode(encode_message)
            encrypted_message = base64_bytes.decode("ascii")

            Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
            text2 = Text(screen1, font="Roboto 10", bg="White", relief=GROOVE, wrap=WORD, bd=0)
            text2.place(x=10, y=40, width=380, height=150)

            text2.insert(END, encrypted_message)
        else:
            messagebox.showerror("Encryption", "No message to encrypt")
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    else:
        messagebox.showerror("Encryption", "Invalid Password")


def main_screen():
    global screen
    global code
    global text1

    screen = Tk()
    screen.geometry("375x398")
    screen.title("PctApp")

    def reset():
        code.set("")
        text1.delete(1.0, END)

    Label(text="Enter text for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=10)
    text1 = Text(font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    Label(text="Enter Secret key for encryption and decryption", fg="black", font=("Calibri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("Arial", 25), show="*").place(x=10, y=200)

    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)

    screen.mainloop()


main_screen()
