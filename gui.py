import tkinter as tk
import matplotlib.pyplot as plt
import wk_calc


# plot function is created for
# plotting the graph in
# tkinter window
def plot(label,eHR,eSV,eR,eC):
    # the figure that will contain the plot

   #fig = Figure(figsize=(5, 5), dpi=100)

    # adding the subplot
   # plot1 = fig.add_subplot(111)



    # plotting the graph

    SV = float(eSV.get())
    HR = float(eHR.get())
    tsys = 0.33
    R = float(eR.get())
    C = float(eC.get())
    Pout = 35
    P = wk_calc.calcPressure(SV, HR, tsys, R, C, Pout)

    Psys = round(max(P))
    Pdia = round(min(P))

    myString = "Pressure: " + str(Psys)+"/"+str(Pdia) + " mmHg";
    label.config(text = myString)

    plt.plot(P)
    plt.show()

def main():
    root = tk.Tk()
    root.title('Plotting the pressure')
    root.geometry("700x200")

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

    eHR.place(x=120, y=25)
    eSV.place(x=120, y=55)
    eR.place(x=120, y=85)
    eC.place(x=120, y=115)

    ansL = tk.Label(text="Pressure: ", font="Arial 25")
    ansL.place(x=320, y=50)

    plot_button = tk.Button(master=root,
                            command = lambda: plot(ansL,eHR,eSV,eR,eC),
                            height=1, width=20,
                            text="Calc Pressure",
                            font="Arial 14")
    plot_button.place(x=10, y=150)

    root.mainloop()

if __name__ == '__main__':
    main()