from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle, random
import pyperclip

font_word = ("Arial", 14, "normal")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list.extend([choice(symbols) for char in range(randint(2, 4))])
    password_list.extend([choice(numbers) for char in range(randint(2, 4))])

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website_entry_data = website_entry.get()
    email_entry_data = email_entry.get()
    password_entry_data = password_entry.get()

    if len(website_entry_data) == 0 or len(password_entry_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_entry_data, message=f"These are the details entered: \nEmail: {email_entry_data} "
                            f"\nPassword: {password_entry_data} \nIs it ok to save?")
        
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_entry_data} | {email_entry_data} | {password_entry_data}\n")
            detele_data()

def detele_data():
    website_entry.delete(0, END)
    email_entry.delete(0, END)
    email_entry.insert(0, "random@gmail.com")
    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#canvas setup
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#website labels and entry
website_label = Label(text="Website:", font= font_word)
website_label.grid(row=1, column=0)

website_entry = Entry(width=35)
website_entry.grid(row= 1, column=1, columnspan=2)


#email labels and entry
email_label = Label(text="Email/Username:", font= font_word)
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row= 2, column=1, columnspan=2)
email_entry.insert(0, "random@gmail.com")
email_entry.focus()


#password labels and entry
password_label = Label(text="Password:", font= font_word)
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row= 3, column=1, columnspan=1)


#generate password button
generate_button = Button(text="Generate Password", width=10, command=generate_password)
generate_button.grid(row=3, column=2)  

#add button
add_button = Button(text="Add", width=33, command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()