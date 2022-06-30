from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    print(f"Your password is: {password}")
    password_input.delete("0.1", END)
    password_input.insert("0.1", password)
    copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get("1.0", "end-1c")
    username = email_input.get("1.0", "end-1c")
    password = password_input.get("1.0", "end-1c")

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please don't leave an empty fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n"
                                                              f"Email: {username}\n"
                                                              f"Password: {password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            with open("passwords.txt", "a") as f:
                f.writelines(f"{website} | {username} | {password}\n")
            website_input.delete("0.1", END)
            password_input.delete("0.1", END)


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
password_button = Button(text="Generate Password", padx=0, command=generate_password)
password_button.grid(row=3, column=2)

# "Add" button - Row 4
# button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
# Mainloop
window.mainloop()
