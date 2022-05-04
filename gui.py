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

def plot(label,eHR,eSV,eR,eC, root, adrenaline, adenosine, vasodilators):
    # the figure that will contain the plot

   #fig = Figure(figsize=(5, 5), dpi=100)

    # adding the subplot
   # plot1 = fig.add_subplot(111)



    # plotting the graph

    SV = float(eSV.get())
    HR = float(eHR.get())
    tsys = 0.33
    R1 = 0
    R2 = float(eR.get())
    C = float(eC.get())
    Pout = 35
    L = 0
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
    label.config(text = myString)

    # create a figure
    figure = Figure(figsize=(5, 5), dpi=100)

    # create FigureCanvasTkAgg object
    figure_canvas = FigureCanvasTkAgg(figure, root)
    # create the toolbar

    # create axes
    axes = figure.add_subplot()

    # create the barchart
    axes.plot(P)
    axes.set_title('Pressure')
    axes.grid()

    figure_canvas.get_tk_widget().grid(row=1, column=3)
    figure_canvas.draw()

def make_buttons(root):
    frame = ttk.Frame(root, name='foo')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)
    # HR label and entry
    ttk.Label(frame, text='HR (bpm)').grid(column=0, row=0, sticky=tk.W)
    e_hr = ttk.Entry(frame, width=30, name='hr')
    e_hr.grid(column=1, row=0, sticky=tk.W)

    # SV label and entry
    ttk.Label(frame, text='SV (ml)').grid(column=0, row=1, sticky=tk.W)
    v_hr = ttk.Entry(frame, width=30, name='sv')
    v_hr.grid(column=1, row=1, sticky=tk.W)

    # Add adrenaline button
    ttk.Button(frame, text='Add adrenaline').grid(column=0, row=2)

    # Remove adrenaline button
    ttk.Button(frame, text='Remove adrenaline').grid(column=1, row=2)

    # Add adenosine button
    ttk.Button(frame, text='Add adenosine').grid(column=0, row=3)

    # Remove adenosine button
    ttk.Button(frame, text='Remove adenosine').grid(column=1, row=3)

    # Add vaso button
    ttk.Button(frame, text='Add vaso').grid(column=0, row=4)

    # Remove vaso button
    ttk.Button(frame, text='Remove vaso').grid(column=1, row=4)


    ttk.Label(frame, text="Pressure: ", font="Arial 25").grid(column=2, row=0)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=3)

    return frame


"""
    # Replace with:
    ttk.Label(frame, text='Replace with:').grid(column=0, row=1, sticky=tk.W)
    replacement = ttk.Entry(frame, width=30)
    replacement.grid(column=1, row=1, sticky=tk.W)

    # Match Case checkbox
    match_case = tk.StringVar()
    match_case_check = ttk.Checkbutton(
        frame,
        text='Match case',
        variable=match_case,
        command=lambda: print(match_case.get()))
    match_case_check.grid(column=0, row=2, sticky=tk.W)

    # Wrap Around checkbox
    wrap_around = tk.StringVar()
    wrap_around_check = ttk.Checkbutton(
        frame,
        variable=wrap_around,
        text='Wrap around',
        command=lambda: print(wrap_around.get()))
    wrap_around_check.grid(column=0, row=3, sticky=tk.W)

    for widget in frame.winfo_children():
        widget.grid(padx=0, pady=5)

    return frame

    lHR = tk.Label(text="HR (bpm)", font="Arial 14")
    lSV = tk.Label(text="SV (ml)", font="Arial 14")
    lR = tk.Label(text="R", font="Arial 14")
    lC = tk.Label(text="C", font="Arial 14")

    lHR.place(x=10, y=20)
    lSV.place(x=10, y=50)
    lR.place(x=10, y=80)
    lC.place(x=10, y=110)

    eHR = tk.Entry(width=10)
    eHR.insert(0, "65")
    eSV = tk.Entry(width=10)
    eSV.insert(0, "70")
    eR = tk.Entry(width=10)
    eR.insert(0, "0.7")
    eC = tk.Entry(width=10)
    eC.insert(0, "2.196")
"""

def main():
    root = tk.Tk()
    root.title('Plotting the pressure')
    root.geometry("1000x500")


    fr = make_buttons(root)

    #root.columnconfigure(0, weight=4)
    fr.grid(column=0, row=0)


    adrenaline = False
    adenosine = False
    vasolidators = False
    root.mainloop()


"""
    eHR.place(x=120, y=25)
    eSV.place(x=120, y=55)
    eR.place(x=120, y=85)
    eC.place(x=120, y=115)
"""


"""
    plot_button = tk.Button(master=root,
                            command = lambda: plot(ansL,eHR,eSV,eR,eC, root, adrenaline, adenosine, vasolidators),
                            height=1, width=20,
                            text="Calc Pressure",
                            font="Arial 14")
    plot_button.place(x=10, y=150)
"""


if __name__ == '__main__':
    main()