from tkinter import *
from tkinter.scrolledtext import *


class DeliveryChargeCalculator:

    """
    tkinter GUI that calculates delivery charges
    Accepts inputs of the length, width, height and weight of a package.
    Delivery charges are then calculated based on the inputs.
    Charges are displayed in the GUI output textbox.
    """

    def __init__(self):

        """Initialises the GUI and all of it's labels, entries, buttons, scrolled text
           and radio buttons"""

        self._tk = Tk()  # creates a GUI window
        self._tk.title('Delivery Charges Calculator')  # change the title of GUI window
        self._tk.geometry('700x330')  # set window size to 700*330

        # ===================================Top Frame==================================
        top_frame = Frame(self._tk)  # add top frame to GUI window
        self._length_label = Label(top_frame, text='Length:')
        self._length_label.grid(row=0, column=0, sticky=E, padx=24)
        self._length_entry = Entry(top_frame, width=20)
        self._length_entry.grid(row=0, column=1, sticky=W)
        self._width_label = Label(top_frame, text='Width:')
        self._width_label.grid(row=1, column=0, sticky=E, padx=32)
        self._width_entry = Entry(top_frame, width=20)
        self._width_entry.grid(row=1, column=1, sticky=W)
        self._height_label = Label(top_frame, text='Height:')
        self._height_label.grid(row=2, column=0, sticky=E, padx=28)
        self._height_entry = Entry(top_frame, width=20)
        self._height_entry.grid(row=2, column=1, sticky=W)

        # ==================================Unit Frame==================================
        unit_frame = Frame(top_frame)
        self._unit_radio = IntVar()
        self._unit_radio.set(0)
        self._cm_radio = Radiobutton(unit_frame, text='cm', value=0, variable=self._unit_radio)
        self._cm_radio.grid(row=0, column=0)
        self._inch_radio = Radiobutton(unit_frame, text='inch', value=1, variable=self._unit_radio)
        self._inch_radio.grid(row=0, column=1)
        unit_frame.grid(row=3, column=1, sticky=W)

        # ==============================Top Frame Continue==============================
        self._space_label = Label(top_frame, text='')  # empty label for spacing
        self._space_label.grid(row=4, column=1)

        # weight label and entry
        self._weight_label = Label(top_frame, text='Weight(kg):')
        self._weight_label.grid(row=5, column=0, sticky=E)
        self._weight_entry = Entry(top_frame, width=20)
        self._weight_entry.grid(row=5, column=1, sticky=W)

        # ===============================Button Frame===================================
        button_frame = Frame(top_frame)
        self._cal_button = Button(button_frame, text='Calculate Charge', command=self.calculate)
        self._cal_button.grid(row=0, column=0)
        self._clear_button = Button(button_frame, text='Clear', width=10, command=self.clear)
        self._clear_button.grid(row=0, column=1)
        button_frame.grid(row=6, column=1, sticky=EW)

        # ================================Scroll Text===================================
        self._output = ScrolledText(top_frame, width=95, height=10, state=DISABLED)
        self._output.grid(row=7, column=0, columnspan=2)

        top_frame.pack()

        self._tk.mainloop()  # execute main loop

    def calculate(self):
        """Calculates volumetric weight. Volumetric weight is compared with the actual weight
           Delivery charge is calculated based on the higher of the actual and volumetric weight"""

        actual_weight = float(self._weight_entry.get())
        leng = float(self._length_entry.get())
        wid = float(self._width_entry.get())
        ht = float(self._height_entry.get())
        vol = leng * wid * ht

        # Append outputs
        self._output.configure(state=NORMAL)
        self._output.insert(END, 'Next Parcel\n')
        # check which unit is used
        if self._unit_radio.get() == 0:  # cm is the chosen unit
            vol_weight = vol / 6000
            self._output.insert(END, f'{leng}cm x {wid}cm x {ht}cm = {vol}cm^3 or {vol_weight:.2f}kg\n')
        else:  # inch is the chosen unit
            vol_weight = vol / 366
            self._output.insert(END, f'{leng}inch x {wid}inch x {ht}inch = {vol}inch^3 or {vol_weight:.2f}kg\n')
        # check which is the higher weight
        if vol_weight > actual_weight:  # vol_w is larger
            used = vol_weight
        else:
            used = actual_weight
        self._output.insert(END, f'Charges based on the higher of ({vol_weight:.2f}, {actual_weight}) = {used:.2f}kg\n')

        # Calculate delivery charges
        base_rate = 3
        charge = 0
        if used < 3:
            charge = 3 + base_rate
        elif used == 3 or used < 5:
            charge = 7 + base_rate
        elif used == 5 or used < 10:
            charge = 12 + base_rate
        elif used >= 10:
            charge = 30 + base_rate
        self._output.insert(END, f'Delivery Charge = ${charge:.2f}\n')
        self._output.configure(state=DISABLED)

    def clear(self):
        """
        To clear input fields after calculation.
        """
        self._length_entry.delete(0, END)
        self._width_entry.delete(0, END)
        self._height_entry.delete(0, END)
        self._weight_entry.delete(0, END)
        self._output.configure(state=NORMAL)
        self._output.delete(1.0, END)
        self._output.configure(state=DISABLED)
        self._unit_radio.set(0)


DeliveryChargeCalculator()
