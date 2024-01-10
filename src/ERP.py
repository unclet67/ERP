#ERP Calculation

import tkinter as tk
from tkinter import *
import math

root=Tk()
root.title("Calculate ERP")
root.geometry("500x400")

def Calculation():
    power=int(radar_power_in_dBMentry.get())
    gain=int(antenna_Gain_in_dBmvalue.get())
    loss=int(antenna_Loss_in_dBmvalue.get())
    total=(power+gain-loss)
    Label(text=f"{total}", font="arial 15 bold").place(x=250,y=170)


#subject
sub1=Label(root,text="Radar Power in dBm", font="arial 10")
sub2=Label(root,text="Antenna Gain in dBm", font="arial 10")
sub3=Label(root,text="Antenna Loss in dBm", font="arial 10")
total=Label(root,text="ERP", font="arial 10")


sub1.place(x=50,y=20)
sub2.place(x=50,y=70)
sub3.place(x=50,y=120)
total.place(x=50,y=170)

radar_power_in_dBMvalue=StringVar()
antenna_Gain_in_dBmvalue=StringVar()
antenna_Loss_in_dBmvalue=StringVar()

radar_power_in_dBMentry=Entry(root,textvariable=radar_power_in_dBMvalue,font="arial 15", width=15)
antenna_Gain_in_dBmvalue=Entry(root,textvariable=antenna_Gain_in_dBmvalue,font="arial 15", width=15)
antenna_Loss_in_dBmvalue=Entry(root,textvariable=antenna_Loss_in_dBmvalue,font="arial 15", width=15)

radar_power_in_dBMentry.place(x=250,y=20)
antenna_Gain_in_dBmvalue.place(x=250,y=70)
antenna_Loss_in_dBmvalue.place(x=250,y=120)

Button(text="Calculate", font="arial 15", bg="white", bd=10,command=Calculation).place(x=50,y=300)
Button(text="Exit", font="arial 15", bg="white", bd=10,width=8,command=lambda:exit()).place(x=350,y=300)

def Calculation():
    target=int(target_radar_heightvalue.get())
    total=(round(math.sqrt(target) + math.sqrt(3.6) * 1.23))
    Label(text=f"{total}", font="arial 15 bold").place(x=250,y=170)


#subject
sub1=Label(root,text="Target Radar Height in ft", font="arial 10")
total=Label(root,text="Radar Horizon in NM", font="arial 10")
sub3=Label(root, text='Radar Horizon = Square Root of Target Height + Square Root of USV Height *1.23', font='arial 10')


sub1.place(x=50,y=20)
total.place(x=50,y=70)
sub3.place(x=50,y=120)

target_radar_heightvalue=StringVar()


target_radar_heightvalue=Entry(root,textvariable=target_radar_heightvalue,font="arial 15", width=15)


target_radar_heightvalue.place(x=250,y=20)


Button(text="Calculate", font="arial 15", bg="white", bd=10,command=Calculation).place(x=50,y=300)
Button(text="Exit", font="arial 15", bg="white", bd=10,width=8,command=lambda:exit()).place(x=350,y=300)

root.mainloop()