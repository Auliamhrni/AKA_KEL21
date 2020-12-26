import os
from tkinter import *
from tkinter.ttk import Combobox
import time
import random
from bubbleSort import bubble_sort
from selectionSort import selection
from pre import pre
from pre import pre1
from pre import pre2
from pre import pre3
from pre import pre4
from pre import pre5

#algs
    #shell sort
    #radix sort

    #comb sort
    #heap sort

# start a tkinter window
root = Tk()
widthr = root.winfo_screenwidth()
heightr = root.winfo_screenheight()
root.maxsize(root.winfo_screenwidth(), root.winfo_screenheight())
root.minsize(root.winfo_screenwidth(), root.winfo_screenheight())
root.config(bg="black")
root.title("Sorting algorithms visualization")

# vars
selected_alg = StringVar()
dades_pre = StringVar()
data = []
pre = pre.pre
pre1 = pre1.pre1
pre2 = pre2.pre2
pre3 = pre3.pre3
pre4 = pre4.pre4
pre5 = pre5.pre5

# draw the rectangles
def drawdata(data, colorarray):

    canvas.delete("all")
    c_height = (heightr/4)*3
    c_width = widthr
    x_width = c_width / (len(data) + 1)
    offset = 0
    spacing = 0
    normalizeddata = [i / max(data) for i in data]

    for i, height in enumerate(normalizeddata):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * ((heightr/3)+(heightr/3))
        x1 = (i+1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorarray[i])

    root.update_idletasks() # update the triangles

# generate an array
def generate():
    global data, pre, pre1, pre2, pre3, pre4, pre5, size

    try:    # if the size is not valid, set a default
        size = int(sizeEntry.get())
    except ValueError:
        size = 0

    data = []

    # check if there's a default set selectet, if it is, append that data to the list
    pre_dict = {'Pre':pre, 'Pre1':pre1, 'Pre2':pre2, 'Pre3':pre3, 'Pre4':pre4, 'Pre5':pre5}

    if pre_det.get() != 'No':
        which_pre = pre_det.get()

        for u in pre_dict.get(which_pre):
            data.append(u)
    # if there's no defaul selected, create a random list with the size you selected
    else:
        for n in range(1, size + 1):
            data.append(n)
        random.shuffle(data)

    drawdata(data, ['black' for x in range(len(data)+1)]) # call the drawdata function and create the squares

def Start_alg():
    global data, size, crono

    if alg_menu.get() == "Bubble Sort": # if buble sort selected:
        start = time.perf_counter() # start a timer
        bubble_sort(data, drawdata, 0)  # call the sort function
        end = time.perf_counter()   # stop the timer when the function ends
        timetext = str(f'Bubble {size} en {round(end - start, 2)} \n')  # write the timing in the program
        crono.insert(0.0, str(timetext))    
        dbb_alg = "Bubble"  # create variables to insert them in the SQL table
        dbb_size = size
        dbb_sec = round(end - start, 2)
        sqlformula = "INSERT INTO sortdata (alg, size, sec) VALUES (%s, %s, %s)"
        dades = (dbb_alg, dbb_size, dbb_sec)
        # insert the data

    elif alg_menu.get() == "Selection Sort":
        start = time.perf_counter()
        selection(data, drawdata, 0)
        end = time.perf_counter()
        drawdata(data, ['green' for x in range(len(data))])
        timetext = str(f'Selection {size} en {round(end - start, 2)} \n')
        crono.insert(0.0, str(timetext))
        dbm_alg = "selection"
        dbm_size = size
        dbm_sec = round(end - start, 2)
        sqlformula = "INSERT INTO sortdata (alg, size, sec) VALUES (%s, %s, %s)"
        dades = (dbm_alg, dbm_size, dbm_sec)


# frames
ui_frame = Frame(root, width=widthr, height=heightr/4, bg="lightblue1")
ui_frame.grid(row=0, column=0, padx=0, pady=0)

canvas = Canvas(root, width=widthr, height=((heightr/4)*3), bg="white")
canvas.grid(row=2, column=0, padx=10, pady=2)

# ui
Label(ui_frame, text="Algs:", bg="lightblue1").grid(row=0, column=0, padx=0, pady=0)
alg_menu = Combobox(ui_frame, textvariable=selected_alg, values=['No' , 'Bubble Sort','Selection Sort'])
alg_menu.grid(row=0, column=1, padx=2, pady=2)
alg_menu.current([0])
Button(ui_frame, text='Create', font=("arial", 13), command=generate, bg='white').grid(row=0, column=2, padx=5, pady=5)

Label(ui_frame, text="Number of data ", bg='lightblue1').grid(row=2, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(ui_frame, width=15)
sizeEntry.grid(row=2, column=1, padx=2, pady=2, sticky=W)

pre_det = Combobox(ui_frame, textvariable=dades_pre, values=['No', 'Pre', 'Pre1', 'Pre2', 'Pre3', 'Pre4', 'Pre5'])
pre_det.grid(row=1, column=3, padx=2, pady=2)
pre_det.current([0])

crono = Text(ui_frame, width=35, height=6, state='normal')
crono.grid(row=0, column=3)

order = Button(ui_frame, text='Sort!', font=("arial", 18), command=Start_alg, bg='red')
order.grid(row=2, column=2, padx=2, pady=2)
root.mainloop()