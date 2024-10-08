"""password manager"""
import tkinter
import tkinter.messagebox
import random
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """generate password"""

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', \
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', \
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', \
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    generated_password = "".join(password_list)

    password_entry.delete(0, tkinter.END)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """save website registration info"""

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        tkinter.messagebox.showinfo(title="Oops", message="Please make sure you haven't \
                                    left any fields empty.")
    else:
        is_ok = tkinter.messagebox.askokcancel(title=website,
                                            message=f"These are the details entered: \n \
                                    Email: {email} \nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r", encoding="utf-8") as data_file:
                    # Reading old data
                    data = json.load(data_file)     
            except FileNotFoundError:
                with open("data.json", "w", encoding="utf-8") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w", encoding="utf-8") as data_file:
                    # Saving update data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, tkinter.END)
                password_entry.delete(0, tkinter.END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    """Find password"""
    website = website_entry.get()
    try:
        with open("data.json", "r", encoding="utf-8") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        tkinter.messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            tkinter.messagebox.showinfo(title=website,
                                        message=f"Email: {email}\nPassword: {password}")
        else:
            tkinter.messagebox.showinfo(title="Error",
                                        message=f"No details for {website} exists.")

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
website_entry = tkinter.Entry(width=20)
website_entry.focus()
website_entry.grid(row=1, column=1)
email_entry = tkinter.Entry(width=37)
email_entry.insert(0, "sundalei1988@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = tkinter.Entry(width=20)
password_entry.grid(row=3, column=1)

# Buttons
search_button = tkinter.Button(text="Search", width=12, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = tkinter.Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
