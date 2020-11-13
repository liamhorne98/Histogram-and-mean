from tkinter import *
window=Tk()

window.geometry("400x300")

import numpy as np
import matplotlib.pyplot as plt




lb=Label(window,text="(Output) " ,width=50)
lb.grid(row=1,column=1)

def get():

    num=np.arange(21)
    my_mean=np.mean(num)
    my_std=np.std(num)
    my_variance=np.var(num)
    lb.config(text=str(num)+ '\n'"Mean:"+ str(my_mean) +'\n' + "Standard Deviation:"+ str(my_std)+'\n'+"Varience:"+str(my_variance))

b_analyse=Button(window,text="Analyse", command=get)
b_analyse.grid(row=5,column=1)
def exit():
    window.destroy()

b_exit=Button(window,text="Exit",command=exit)
b_exit.grid(row=9,column=1)


def hist():
    nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
    bins = np.array([0, 1, 2, 3])
    '''print("nums: ",nums)
    print("bins: ",bins)
    print("Result:", np.histogram(nums, bins))'''
    plt.hist(nums, bins=bins)
    plt.xlabel("Nums")
    plt.ylabel("Bins")
    plt.show()

histbtn=Button(window,text="Challenge 2",command=hist)
histbtn.grid(row=10,column=1)



window.mainloop()