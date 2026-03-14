from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

def save():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_pass.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Oops", "Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered:\nemail:  {email}\nPassword:  {password}\n"
                                f">>> Is it OK to save? <<<")
        if is_ok:
            with open("password.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")

            entry_web.delete(0, END)
            entry_pass.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    entry_pass.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = (
        [choice(letters) for _ in range(randint(8,10))] +
        [choice(numbers) for _ in range(randint(2,4))] +
        [choice(symbols) for _ in range(randint(2,4))]
    )

    shuffle(password_list)
    password = "".join(password_list)
    entry_pass.insert(0, password)
    # save password to the clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

canvas = Canvas(window, width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
label_web = Label(text="Website:")
label_web.grid(column=0, row=1, padx=5, pady=5, sticky="e")

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2, padx=5, pady=5, sticky="e")

label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3, padx=5, pady=5, sticky="e")

#Entries
entry_web = Entry(width=35)
entry_web.grid(column=1, row=1, columnspan=2, padx=5, pady=5, sticky="we")
entry_web.focus()

entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2, padx=5, pady=5, sticky="we")
entry_email.insert(0, "sam@dalnorth.com")

entry_pass = Entry(width=21)
entry_pass.grid(column=1, row=3, padx=5, pady=5, sticky="we")

#Buttons
button_gen = Button(window, text="Generate Password", command=generate_password)
button_gen.grid(column=2, row=3)

button_add = Button(window, text="Add", width=43, command=save)
button_add.grid(column=1, row=4, columnspan=2)


# ---------------------------- MAIN LOOP ----------------------------------- #
window.mainloop()