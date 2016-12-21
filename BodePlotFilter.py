
import visa
import time

from tkinter import *
from tkinter.messagebox import *
from matplotlib.backends.backend_tkagg import *
from matplotlib.figure import Figure

def get_values(*args):
    freq.get()
    unit.get()
    ampli.get()
    offset.get()
    type_sig.get()

def send_cmds():
    global a, i, tab_am, tab_frq, tab_ph
    a = 2
    frq = 1
    am = 1
    ph = 1
    get_values()
    instr = rm.open_resource('USB0::0x0400::0x09C4::DG1D172101858::INSTR')
    instr1 = rm.open_resource('GPIB0::7::INSTR')
    #print(r)	#Testing purposes
    while True:
        spAmpl.cla()
        spPhas.cla()
        if a > 1:
            cmds = "APPL:{0} {1:.2f}{2}, {3}VPP, {4}V".format(type_sig.get(), float(freq.get())+i, unit.get(), float(ampli.get()), float(offset.get()))
            instr.write(cmds)
            time.sleep(2)
            instr1.write(':AUToscale')
            ta = am
            am = float(instr1.query(':MEASure:VAMPLitude?'))
            if (ta + am) >= 50 or (ta + am) <= -50:
                am = ta 
            tf = frq
            frq = float(instr1.query(':MEASure:FREQuency?'))
            if frq >= 10e20:
                frq = tf
            ph = float(instr1.query(':MEASure:PHASe?'))
            tab_am.append(am)
            tab_frq.append(frq)
            tab_ph.append(ph)
            spAmpl.semilogx(tab_frq, tab_am, 'r')
            spPhas.semilogx(tab_frq, tab_ph, 'r')
            canvas.show()
            #print(cmds)	#Testing purposes
            #print(tab_frq, tab_ph, tab_am)	#Testing purposes
            a+= 1
            i = i*1.1
            root.update()
        if a == 1:
            spAmpl.cla()
            spAmpl.semilogx(am, frq, 'b')
            spPhas.cla()
            spPhas.semilogx(ph, frq, 'b')
            root.update()


def pause():
    global a
    a = 1

def close():
    if askyesno('Warning', 'If you continue every information will be descartes!'):
        root.quit()     
        root.destroy()
        

                ############################
				#Declaration/Initialisation#

rm = visa.ResourceManager()
list = rm.list_resources()

root = Tk()

root.wm_title("BodePlotFilter.py")

frame = Frame(root)

a = 1
i = 100
tab_am = []
tab_ph = []
tab_frq = []


                ####################
				#Window composition#
				
title = Label(frame, text="GBF Set-UP", font=("Helvetica", 22), fg="blue")
title_graph = Label(root, text = "Bode Representation\t\t\t", font=("Helvetica", 14), bg="#f0f0f0", fg="black")
title_frame = Label(frame, text = "Signal", font=("Helvetica", 14))
type_sig = StringVar()
type_sig.set("###")

				
				##############
				#GUI creation#

fgBode = Figure(figsize=(11,5), dpi=75)
fgBode.suptitle('Bode plot', fontsize=12)
fgBode.subplots_adjust(hspace=0.28)

spAmpl = fgBode.add_subplot(121)
spAmpl.set_title('Amplitude',fontdict={'fontsize':10})

spPhas = fgBode.add_subplot(122, axisbg='cyan')
spPhas.set_title('Phase',fontdict={'fontsize':10})

frPlt = Frame(root)

cvPlot = FigureCanvasTkAgg(fgBode, master=frPlt)
cvPlot.show()

tbPlot = NavigationToolbar2TkAgg(cvPlot, frPlt)
tbPlot.update()

canvas = FigureCanvasTkAgg(fgBode, master=root)
canvas.show()
fgBode.tight_layout()
canvas.get_tk_widget().grid(column=1, row=10)


				##########################
				#Window elements creation#

b1 = Radiobutton(frame, text="Sinusoid\t\t\t", variable=type_sig, value="SIN")
b2 = Radiobutton(frame, text="Triangle\t\t\t", variable=type_sig, value="RAMP")
b3 = Radiobutton(frame, text="Square\t\t\t", variable=type_sig, value="SQUARE")

freq = Spinbox(frame, from_=0, to=1000000000000, width=10)
freq_title = Label(frame, text = "Freq")

unit = Spinbox(frame, values=('HZ', 'KHZ', 'MHZ', 'GHZ'), width=5)

ampli = Spinbox(frame, from_=0, to=1000000000000, width=10)
ampli_title = Label(frame, text = "Amp")

offset = Spinbox(frame, from_=0, to=1000000000000, width=10)
offset_title = Label(frame, text = "Offset")

button_start = Button(frame, text="Start", command=send_cmds, width=10, font=("Helvetica", 14), bg="#00ff80", activebackground="#00ff80", relief=GROOVE)
button_pause = Button(frame, text="Pause / Reset", command=pause, width=12, font=("Helvetica", 9), relief=GROOVE)
button_close = Button(master=frame, text='Close', command=close, bg="#ff0000", activebackground="#ff0000",fg="white", relief=GROOVE)


                ##########################
				#Window elements location#

frame.grid(column=1, row=0)

title.grid(column=1, row=1, columnspan=3)
title_frame.grid(column=1, row=2, sticky='nsw')
title_graph.grid(column=1, row=9, columnspan=3, sticky='n')

b1.grid(column=1, row=3, sticky='nsw')
b2.grid(column=1, row=4, sticky='nsw')
b3.grid(column=1, row=5, sticky='nsw')

freq_title.grid(column=2, row=3, sticky='nsw')
freq.grid(column=3, row=3, columnspan=1, sticky='nse')

unit.grid(column=4, row=3, sticky='nsw')

ampli_title.grid(column=2, row=4, sticky='nsw')
ampli.grid(column=3, row=4, sticky='nse')

offset_title.grid(column=2, row=5, sticky='nsw')
offset.grid(column=3, row=5, sticky='nse')

empty = Label(frame, width=40).grid(row=0, column=5)

button_start.grid(column=5, row=8, sticky='nse')
button_pause.grid(column=6, row=8, sticky='nse')
button_close.grid(column=7, row=8, sticky='nsw')

frPlt.grid(column=1, row=11, columnspan=3, sticky='nsw')

root.mainloop()
