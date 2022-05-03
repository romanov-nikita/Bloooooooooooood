import matplotlib.pyplot as plt
import tkinter as tk

def draw_plot(array):
    plt.figure(figsize=(10,10))
    plt.plot(array)
    plt.title('Blood pressure')
    plt.xlabel('Time, ms')
    plt.ylabel('Pressure, mmHg')
    plt.show()

if __name__ == '__main__':
    pass