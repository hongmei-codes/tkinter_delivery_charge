# Tkinter GUI 

Just a simple tkinter GUI that can calculate delivery charges 📦 based on predetermined formula.

# Demo
![tkinter gui demo](https://github.com/hongmei-codes/tkinter_delivery_charge/blob/master/demo/gui.png)

### Elements
* entry fields
* buttons
* radio buttons
* scroll text fields

  
# Tkinter for Beginners
Tkinter comes with python, so there is no need to install anything before using it.

To use tkinter, first import the package
```python
from tkinter import *
```

Next, create a GUI window and give a name and set the dimensions
```python
gui = Tk()
gui.title('Delivery Charges Calculator')
gui.geometry('100x100')
```

Now you can add elements to it like entry fields, buttons and radio buttons. After add all the elements, remember to pack the frames like this 👉🏼  `top_frame.pack()`. Otherwise you will not see the elements you put added to the window.

One last thing to do is to start the loop that listens for user input.
```python
gui.mainloop()  # excutes main loop
```

# Tkinter bugs 🐞
For mac users, if you turn on dark mode, your buttons may be displayed as white and without text. Turning off dark mode should solve the problem. But if that doesn't work, check out other solutions [here](https://github.com/PySimpleGUI/PySimpleGUI/issues/1124).
