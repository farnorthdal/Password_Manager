from tkinter import *

def button_clicked():
    pass
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
button_gen = Button(window, text="Generate Password", command=button_clicked)
button_gen.grid(column=2, row=3)

button_add = Button(window, text="Add", width=30, command=button_clicked)
button_add.grid(column=1, row=4, columnspan=2)


# ---------------------------- MAIN LOOP ----------------------------------- #
window.mainloop()