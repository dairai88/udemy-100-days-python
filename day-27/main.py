"""day 27"""
from tkinter import Tk, Label, Button, Entry, END


def button_clicked():
    """button clicked"""
    print("I got clicked")
    new_text = textInput.get()
    my_label.config(text=new_text)


# Creating a new window and configurations
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=40, pady=40)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Button

# calls action() when pressed
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
textInput = Entry(width=30)
# Add some text to begin with
textInput.insert(END, string="Some text to begin with.")
print(textInput.get())
textInput.grid(column=3, row=2)

window.mainloop()
