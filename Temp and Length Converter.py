import sys
import tkinter as tk
from tkinter import *
import urllib.request
import webbrowser
from functools import partial
from tkinter import Tk, StringVar, ttk

root = Tk()
root.title('Unit Converter App')
root.geometry("450x400+100+200")
labelfont = ('ariel', 56, 'bold')
l = Label(root, text='Unit Converter App', font=("Arial", 20, "italic"), justify=CENTER)
l.place(x=80, y=20)

widget = Button(None, text="QUIT", bg="white", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="green",
                activeforeground="blue", command=root.destroy).place(x=350, y=350)

def WeightConverter():
    factors = {'kg': 1000, 'hg': 100, 'dg': 10, 'g': 1, 'deg': 0.1, 'cg': 0.01, 'mg': 0.001}
    ids = {"Kilogram": 'kg', "Hectagram": 'hg', "Decagram": 'dg', "Decigram": 'deg', "Kilogram": 'kg', "gram": 'g',
           "centigram": 'cg', "milligram": 'mg'}

    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Weight Converter")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label(mainframe, text="Weight Converter", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1,
                                                                                                            row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    in_select = OptionMenu(mainframe, in_unit, "Kilogram", "Hectagram", "Decagram", "gram", "Decigram", "Centigram",
                           "Milligram").grid(column=3, row=1, sticky=W)

    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Kilogram", "Hectagram", "Decagram", "gram", "Decigram", "Centigram",
                           "Milligram").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()



def LengthConverter():
    factors = {'nmi': 1852, 'mi': 1609.34, 'yd': 0.9144, 'ft': 0.3048, 'inch': 0.0254, 'km': 1000, 'm': 1, 'cm': 0.01,
               'mm': 0.001}
    ids = {"Nautical Miles": 'nmi', "Miles": 'mi', "Yards": 'yd', "Feet": 'ft', "Inches": 'inch', "Kilometers": 'km',
           "meters": 'm', "centimeters": 'cm', "millileters": 'mm'}

    def convert(amt, frm, to):
        if frm != 'm':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Length Converter")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label(mainframe, text="Length Converter", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1,
                                                                                                            row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    in_select = OptionMenu(mainframe, in_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers",
                           "meters", "centimeters", "millileters").grid(column=3, row=1, sticky=W)

    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers",
                           "meters", "centimeters", "millileters").grid(column=3, row=3, sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()


def TemperatureConverter():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()

        if celTempVar.get() != 0.0:
            celToFah = (celTemp * 9 / 5 + 32)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * (5 / 9))
            celTempVar.set(fahToCel)

    def reset():
        top = Toplevel(padx=50, pady=50)
        top.grid()
        message = Label(top, text="Reset Complete")
        button = Button(top, text="OK", command=top.destroy)

        message.grid(row=0, padx=5, pady=5)
        button.grid(row=1, ipadx=10, ipady=10, padx=5, pady=5)

        fahTempVar.set(int(0))
        celTempVar.set(int(0))

    top = Toplevel()
    top.title("Temperature Converter")

    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))
    titleLabel = Label(top, text="Temperature Converter", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1,
                                                                                                           row=1)

    celLabel = Label(top, text="Celcius: ", font=("Arial", 16), fg="red")
    celLabel.grid(row=2, column=1, pady=10, sticky=NW)

    fahLabel = Label(top, text="Fahrenheit: ", font=("Arial", 16), fg="blue")
    fahLabel.grid(row=3, column=1, pady=10, sticky=NW)

    celEntry = Entry(top, width=10, bd=5, textvariable=celTempVar)
    celEntry.grid(row=2, column=1, pady=10, sticky=NW, padx=125)

    fahEntry = Entry(top, width=10, bd=5, textvariable=fahTempVar)
    fahEntry.grid(row=3, column=1, pady=10, sticky=NW, padx=125)

    convertButton = Button(top, text="Convert", font=("Arial", 8, "bold"), relief=RAISED, bd=5, justify=CENTER,
                           highlightbackground="red", overrelief=GROOVE, activebackground="green",
                           activeforeground="blue", command=convert)
    convertButton.grid(row=4, column=1, ipady=8, ipadx=12, pady=5, sticky=NW, padx=55)

    resetButton = Button(top, text="Reset", font=("Arial", 8, "bold"), relief=RAISED, bd=5, justify=CENTER,
                         highlightbackground="red", overrelief=GROOVE, activebackground="green",
                         activeforeground="blue", command=reset)
    resetButton.grid(row=4, column=2, ipady=8, ipadx=12, pady=5, sticky=NW)


def color_config(widget, color, event):
    widget.configure(foreground=color)


widget = Button(root, text="Temperature converter", bg="white", fg="red", font=("Arial", 14, "bold"), relief=RAISED,
                bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="green",
                activeforeground="blue", command=TemperatureConverter).place(x=50, y=120)
widget = Button(root, text="Length Converter", bg="white", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="green",
                activeforeground="blue", command=LengthConverter).place(x=50, y=180)
widget = Button(root, text="Area Converter", bg="white", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="green",
                activeforeground="blue", command=AreaConverter).place(x=50, y=240)
widget = Button(root, text="Currency converter", bg="white", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="green",
                activeforeground="blue", command=CurrencyConverter).place(x=50, y=60)
widget = Button(root, text="Weight Converter", bg="white", fg="red", font=("Arial", 14, "bold"), relief=RAISED, bd=5,
                justify=CENTER, highlightbackground="red", overrelief=GROOVE, activebackground="green",
                activeforeground="blue", command=WeightConverter).place(x=50, y=300)

root.mainloop()
