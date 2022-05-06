import tkinter as tk
from personalize import calcParameters
import matplotlib.pyplot as plt
from tkinter import ttk
import wk_calc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

"""
Dictionary representing medicine that can be added to calculations
and flag for removing existing calculations from plot
"""
medicine = {'Adrenaline': False,
            'Adenosine': False,
            'Caffeine': False,
            'Remove': False
            }

"""
Global variable for figure canvas to be drawn in GUI
"""
figure_canvas = None

"""
Function checking what medicine is added for calculations.
Sets True for chosen medicine and False for the rest objects in medicine dictionary
Gets name of medicine to be added
"""
def add_check(med):
    global medicine
    for key in medicine.keys():
        medicine[key] = False
    medicine[med] = True

"""
Function checking whether remove was chosen.
Sets False to all the values in medicine dictionary and clears plot output
Gets label from GUI where pressure should be shown
"""
def remove(label):
    global medicine
    global figure_canvas
    plt.cla()
    label.config(text=' ')
    for key in medicine.keys():
        medicine[key]=False
    figure_canvas.draw()

"""
Function that calculates the pressure and draws plot
"""
def plot(label, eHR, eSV, p_sys, p_dys, root, adrenaline, adenosine,
         caffeine, figure, axes):
    global figure_canvas
    # plotting the graph
    SV = float(eSV.get())
    HR = float(eHR.get())
    tsys = 0.33
    p_Sys = float(p_sys.get())
    p_Dys = float(p_dys.get())
    Pout = 35
    L = 0.00
    print(medicine)
    # Parameters adjusting
    R1, R2, C = calcParameters(SV, HR, tsys, p_Sys, p_Dys, Pout)
    if adrenaline:
        P = wk_calc.calcPressure(SV, 1.1 * HR, tsys, R1, 0.8 * R2, 0.6 * C, Pout, L)
        name ='Adrenaline'
    elif adenosine:
        P = wk_calc.calcPressure(SV, HR, tsys, R1, R2, C, Pout, L)
        name = 'Adenosine'
    elif caffeine:
        P = wk_calc.calcPressure(SV, HR, tsys, R1, R2, C, Pout, L)
        name = 'Caffeine'
    else:
        P = wk_calc.calcPressure(SV, HR, tsys, R1, R2, C, Pout, L)
        name = 'Normal'
    Psys = round(max(P))
    Pdia = round(min(P))

    myString = "Pressure: " + str(Psys) + "/" + str(Pdia) + " mmHg"
    label.config(text=myString)

    # create a figure
    # create FigureCanvasTkAgg object

    # create the toolbar


    # create axes
    # create the barchart
    axes.plot(P, label=name)
    axes.legend(fontsize=14)
    axes.set_title('Pressure', fontsize=14)
    axes.set_ylabel('Pressure, mmHg', fontsize=14)
    axes.set_xlabel('time, ms', fontsize=14)

    if figure_canvas == None:
        figure_canvas = FigureCanvasTkAgg(figure, root)
        figure_canvas.get_tk_widget().grid(row=1, column=2, rowspan=8)
    figure_canvas.draw()



def make_buttons(root):
    width = 20
    figure, axes = plt.subplots(figsize=(8, 6))
    frame = ttk.Frame(root, name='foo')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(0, weight=3)
    # HR label and entry
    ttk.Label(frame, text='HR (bpm)', font=("Arial",14)).grid(column=0, row=0, sticky=tk.W)
    e_hr = ttk.Entry(frame, width=width, name='hr', font=("Arial",14))
    e_hr.grid(column=1, row=0, sticky=tk.W)

    # SV label and entry
    ttk.Label(frame, text='SV (ml)', font=("Arial", 14)).grid(column=0, row=1, sticky=tk.W)
    e_sv = ttk.Entry(frame, width=width, name='sv', font=("Arial", 14))
    e_sv.grid(column=1, row=1, sticky=tk.W)

    # Psys label and entry
    ttk.Label(frame, text='Psys (mmHg)', font=("Arial", 14)).grid(column=0, row=2, sticky=tk.W)
    p_sys = ttk.Entry(frame, width=width, name='psys', font=("Arial", 14))
    p_sys.grid(column=1, row=2, sticky=tk.W)

    # Pdys label and entry
    ttk.Label(frame, text='Pdias(mmHg)', font=("Arial", 14)).grid(column=0, row=3, sticky=tk.W)
    p_dys = ttk.Entry(frame, width=width, name='pdys', font=("Arial" ,14))
    p_dys.grid(column=1, row=3, sticky=tk.W)

    # Add adrenaline button
    # HR + 10%
    # R2 - 20%
    # C - 40%
    ttk.Button(frame, text='Add adrenaline', width=width*2+4,
               command=lambda: add_check('Adrenaline')) \
        .grid(column=0, row=4, columnspan=2)


    # Add adenosine button
    ttk.Button(frame, text='Add adenosine', width=width*2+4,
               command=lambda: add_check('Adenosine'))\
        .grid(column=0, row=5, columnspan=2)


    # Add caffeine button
    ttk.Button(frame, text='Add caffeine', width=width*2+4,
               command=lambda: add_check('Caffeine'))\
        .grid(column=0, row=6, columnspan=2)



    label = ttk.Label(frame, font=("Arial" ,20))
    label.grid(column=2, row=0, rowspan=2, sticky=tk.N)

    # Remove
    ttk.Button(frame, text='Remove', width=width * 2 + 4,
               command=lambda: remove(label)) \
        .grid(column=0, row=7, columnspan=2)

    ttk.Button(frame, command=lambda: plot(label, e_hr, e_sv, p_sys, p_dys, frame,
                                           medicine['Adrenaline'],
                                           medicine['Adenosine'],
                                           medicine['Caffeine'],
                                           figure, axes),
               width=width * 2 + 4,
               text="Calc Pressure").grid(column=0, row=8, columnspan=2)

    for widget in frame.winfo_children():
        widget.grid(padx=5, pady=12, ipadx=2, ipady=12)

    return frame


def main():
    root = tk.Tk()
    root.title('Plotting the pressure')
    root.geometry("1300x724")
    root.resizable(0, 0)

    style = ttk.Style()
    style.theme_use('alt')
    style.configure('TButton', font=('American typewriter', 16), background='#222222', foreground='white')
    style.map('TButton', background=[('active', '#4287f5'), ('disabled', '#00f0f0')])

    style.configure('TButton_pressed', font=('American typewriter', 16), background='#222222', foreground='white')
    style.map('TButton_pressed', background=[('disabled', '#4287f5')])

    fr = make_buttons(root)

    # root.columnconfigure(0, weight=4)
    fr.grid(column=0, row=0)

    root.mainloop()


if __name__ == '__main__':
    main()
