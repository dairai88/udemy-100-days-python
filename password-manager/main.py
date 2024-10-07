"""password manager"""
import tkinter
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """save website registration info"""

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open("data.txt", "a", encoding="utf-8") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
logo_image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = tkinter.Entry(width=35)
email_entry.insert(0, "sundalei1988@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tkinter.Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
