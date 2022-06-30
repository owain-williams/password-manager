from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass
# ---------------------------- UI SETUP ------------------------------- #

# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# Logo
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image_padlock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_padlock)
canvas.grid(row=0, column=1)

# Website - Row 1
# label
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
# input
website_input = Text(height=1, width=35, bg="white")
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

# Email/Username - Row 2
# label
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
# input
email_input = Text(height=1, width=35, bg="white")
email_input.insert(END, "owain@andersdigital.com")
email_input.grid(row=2, column=1, columnspan=2)

# Password - Row 3
# label
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)
# input
password_input = Text(height=1, width=21, bg="white")
password_input.grid(row=3, column=1)
# button
password_button = Button(text="Generate Password", command=generate_password, padx=0)
password_button.grid(row=3, column=2)

# "Add" button - Row 4
# button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
# Mainloop
window.mainloop()