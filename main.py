from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    characters_list=[random.choice(letters) for char in range(8, 10)]
    integers_list=[random.choice(numbers) for num in range(2, 4)]
    symbols_list=([random.choice(symbols) for symbol in range(2, 4)])

    password_list = characters_list + integers_list + symbols_list
    password_list.extend(characters_list)
    password_list.extend(integers_list)
    password_list.extend(symbols_list)
    random.shuffle(password_list)

    password = "".join(password_list)
    password_field.delete(0, 'end')
    password_field.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_field.get()
    email_username = email_username_field.get()
    password = password_field.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Missing info", message="Please don't leave any empty fields")
    else:
        confirm_save = messagebox.askokcancel(title=website, message=f'Data entered: \nEmail: {email_username}\nPassword: {password}\n Do you want to save the data?')
        if confirm_save:
            with open('data.txt', 'a') as file:
                file.write(f'{website} / {email_username} / {password}\n')
                website_field.delete(0, 'end')
                password_field.delete(0, 'end')
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image = img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
website_field = Entry(width=35)
website_field.grid(column=1, row=1, columnspan=2)
website_field.focus()

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)
email_username_field = Entry(width=35)
email_username_field.grid(column=1, row=2, columnspan=2)
email_username_field.insert(0, 'jvdpt0@gmail.com')

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)
password_field = Entry(width=30)
password_field.grid(column=1, row=3)

generator_button = Button(text='Generate Password', command=generate_password)
generator_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()