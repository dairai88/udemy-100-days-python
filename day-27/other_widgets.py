"""day 27"""
from tkinter import Tk, Label, Button, Entry, END, Text, Spinbox, Scale, IntVar, Checkbutton, \
    Radiobutton, Listbox

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Label
my_label = Label(text="This is old text", font=("Arial", 24, "bold"))
my_label.config(text="This is new text")
my_label.pack()

# Button


def button_clicked():
    """button clicked"""
    print("I got clicked")
    new_text = textInput.get()
    my_label.config(text=new_text)


# calls action() when pressed
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
textInput = Entry(width=30)
# Add some text to begin with
textInput.insert(END, string="Some text to begin with.")
print(textInput.get())
textInput.pack()

# Text
textArea = Text(height=5, width=30)
# Puts cursor in textbox.
textArea.focus()
# Adds some text to begin with.
textArea.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(textArea.get("1.0", END))
textArea.pack()

# Spinbox


def spinbox_used():
    """spin box used"""
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.


def scale_used(value):
    """scale used"""
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton


def checkbutton_used():
    """Prints 1 if On button checked, Otherwise 0."""
    print(checked_state.get())


# variable to hold on to check state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton


def radio_used():
    """radio used"""
    print(radio_state.get())


# Variable to hold on to which radio button is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox


def listbox_used(event):
    """Gets current selection from listbox"""
    print(f"event: {event}", listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
