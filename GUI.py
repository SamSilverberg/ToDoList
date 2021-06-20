from ToDo import ToDo
from Colors import Colors
import tkinter as tk
from tkinter import *

# TODO - inserting larger dates gives cur.pos on line 43 in ToDo as NoneType?


Memory = []
#want to have multiple ToDo objects, label different colors, display chronologically
def new_list():
    for i in Memory: # tried to make duplicate list
        if listentry.get() == i[0]:
            raise ValueError

    List = listentry.get()
    List = ToDo()
    Memory.append([listentry.get(), List])
    print(Memory)
    alllists.delete('1.0', END)
    for i in range(len(Memory)):
        alllists.insert('1.0',f"{Memory[i][0]}"+"\n")

def printlistentriesbutton():
    listdisplay.delete('1.0', END)
    for i in range(len(Memory)):
        listdisplay.insert('1.0',f"{Memory[i][0]}: {Memory[i][1]}"+"\n")
    listdisplay.pack()


def give():
    inp = thingentry.get()
    inpclean = inp.split(':')
    list_to_add_to = inpclean[0]
    task = inpclean[1]
    date = inpclean[2]
    k = 0
    for i in Memory:
        if list_to_add_to == i[0]:
            i[1].add(task, date)
            print(i[1])
            break
        k += 1
        if k == len(Memory): # list not found
            raise ValueError


# GUI ====================================================================================
window = tk.Tk()

topFrame = tk.Frame(window, width=50, height=100)
listFrame = tk.Frame(window, width=50, height=100)

topFrame.pack(side=LEFT)
listFrame.pack(side=RIGHT)
listdisplay = tk.Text(listFrame, width = 50, height = 30)
listdisplay.insert('1.0',"")
listdisplay.pack(side=TOP)

addbutton = tk.Button(listFrame, text=f"Print All Items", command=printlistentriesbutton)
addbutton.pack(side=TOP)


label = tk.Label(
    topFrame,
    text="Current Lists: ",
    fg="black",
    width=30,
    height=1
)
label.pack(side=TOP)
alllists = tk.Text(topFrame, width = 30, height = 5)
alllists.insert('1.0',"")
alllists.pack(side=TOP)


#Add new list ====================================================================================
listentry = tk.Entry(topFrame, fg="black", bg="white", width=30)
listentry.pack(side=TOP)
addlist = tk.Button(topFrame, text='Make New List', command=new_list)
addlist.pack(side=TOP)

#Add new items ====================================================================================
inputlabel = tk.Label(topFrame, text="Input: list:task:month day year")
thingentry = tk.Entry(topFrame, fg="black", bg="white", width=30)
inputlabel.pack(side=TOP)
thingentry.pack(side=TOP)
addbutton = tk.Button(topFrame, text='Add', command=give)
addbutton.pack(side=TOP)

#COMMANDS ============================================================================================


window.mainloop()