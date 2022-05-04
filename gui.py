import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import ttk
import wk_calc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

widget_labels={'HR':'.foo.hr',
               'SV':'.foo.sv',
               'Pressure':'.foo.pressure',
               'Plot':'.foo.plot'
               }


# plot function is created for
# plotting the graph in
# tkinter window

def plot(label,eHR,eSV, root):
    # the figure that will contain the plot

   #fig = Figure(figsize=(5, 5), dpi=100)

    # adding the subplot
   # plot1 = fig.add_subplot(111)



    # plotting the graph

    SV = float(eSV.get())
    HR = float(eHR.get())
    tsys = 0.33
    R1 = 0
    R2 = 1
    C = 1
    Pout = 35
    L = 0
    adrenaline=adenosine=vasodilators=False
    if adrenaline:
        P = wk_calc.calcPressure(SV, HR, tsys, R1, R2, C, Pout, L)
    elif adenosine:
        P = wk_calc.calcPressure(SV, HR, tsys, R1, R2, C, Pout, L)
    elif vasodilators:
        P = wk_calc.calcPressure(SV, HR, tsys, R1, R2, C, Pout, L)
    else:
        P = wk_calc.calcPressure(SV, HR, tsys, R1, R2, C, Pout, L)
    Psys = round(max(P))
    Pdia = round(min(P))

    myString = "Pressure: " + str(Psys)+"/"+str(Pdia) + " mmHg"
    label.config(text=myString)

    # create a figure
    figure = Figure(figsize=(5, 3))

    # create FigureCanvasTkAgg object
    figure_canvas = FigureCanvasTkAgg(figure, root)
    # create the toolbar

    # create axes
    axes = figure.add_subplot()

    # create the barchart
    axes.plot(P)
    axes.grid()

    figure_canvas.get_tk_widget().grid(row=1, column=2, rowspan=7, pady=5)
    figure_canvas.draw()

def make_buttons(root):
    width=20
    frame = ttk.Frame(root, name='foo')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)
    # HR label and entry
    ttk.Label(frame, text='HR (bpm)').grid(column=0, row=0, sticky=tk.W)
    e_hr = ttk.Entry(frame, width=width, name='hr')
    e_hr.grid(column=1, row=0, sticky=tk.W)

    # SV label and entry
    ttk.Label(frame, text='SV (ml)').grid(column=0, row=1, sticky=tk.W)
    e_sv = ttk.Entry(frame, width=width, name='sv')
    e_sv.grid(column=1, row=1, sticky=tk.W)

    # Psys label and entry
    ttk.Label(frame, text='Psys (mmHg)').grid(column=0, row=2, sticky=tk.W)
    psys = ttk.Entry(frame, width=width, name='psys')
    psys.grid(column=1, row=2, sticky=tk.W)

    # Pdys label and entry
    ttk.Label(frame, text='Pdys(mmHg)').grid(column=0, row=3, sticky=tk.W)
    p_dys = ttk.Entry(frame, width=width, name='pdys')
    p_dys.grid(column=1, row=3, sticky=tk.W)

    # Add adrenaline button
    ttk.Button(frame, text='Add adrenaline', width=width).grid(column=0, row=4)

    # Remove adrenaline button
    ttk.Button(frame, text='Remove adrenaline', width=width).grid(column=1, row=4)

    # Add adenosine button
    ttk.Button(frame, text='Add adenosine', width=width).grid(column=0, row=5)

    # Remove adenosine button
    ttk.Button(frame, text='Remove adenosine', width=width).grid(column=1, row=5)

    # Add vaso button
    ttk.Button(frame, text='Add vaso', width=width).grid(column=0, row=6)

    # Remove vaso button
    ttk.Button(frame, text='Remove vaso', width=width).grid(column=1, row=6)

    label = ttk.Label(frame, font="Arial 20")
    label.grid(column=2, row=0, rowspan=2, sticky=tk.N)

    ttk.Button(frame, command=lambda: plot(label, e_hr, e_sv, frame),
                            width=width*2+4,
                            text="Calc Pressure").grid(column=0, row=7, columnspan=2)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=10, ipadx=2, ipady=1)

    return frame

def main():
    root = tk.Tk()
    root.title('Plotting the pressure')
    root.geometry("800x370")

    fr = make_buttons(root)

    #root.columnconfigure(0, weight=4)
    fr.grid(column=0, row=0)


    adrenaline = False
    adenosine = False
    vasolidators = False
    root.mainloop()

if __name__ == '__main__':
    main()