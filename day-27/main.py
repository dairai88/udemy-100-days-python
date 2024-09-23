"""day 27"""
from tkinter import Tk, Label, Button, Entry, END

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

window.mainloop()
