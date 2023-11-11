from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from console import function

root = Tk()
root.title("Таблица значений функции в диапазоне")

# Frames
image_button_frame = Frame(root)
image_button_frame.grid(row=0, column=0)

label_frame = Frame(root)
label_frame.grid(row=0, column=1)

input_frame = Frame(root)
input_frame.grid(row=0, column=2)

table_frame = Frame(root)
table_frame.grid(row=1, column=0)

chart_frame = Frame(root)
chart_frame.grid(row=1, column=1)

image = Image.open("formula.jpg")
image = image.resize((300, 100))
photo = ImageTk.PhotoImage(image)

# Image
image_label = Label(image_button_frame, image=photo)
image_label.grid(row=0, column=0)


def btnClickHandler():
    tree.delete(*tree.get_children())
    try:
        a = float(inputA.get())
    except:
        messagebox.showerror("Ошибка", " Переменная a должна быть числом")
        return
    try:
        b = float(inputB.get())
    except:
        messagebox.showerror("Ошибка", " Переменная a должна быть числом")
        return
    try:
        h = float(inputH.get())
    except:
        messagebox.showerror("Ошибка", " Переменная h должна быть числом")
        return
    x = a
    i = 1
    x_values = []
    y_values = []
    while x <= b:
        tree.insert("", "end", values=(i, x, function(x)))
        x_values += [float(x)]
        if function(x) != "Не существует":
            y_values += [float(function(x))]
        else:
            y_values += [0]
        i += 1
        x += h
    figure = Figure(figsize=(4, 3), dpi=100)
    plot = figure.add_subplot(1, 1, 1)
    plot.plot(x_values, y_values)

    canvas = FigureCanvasTkAgg(figure, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()


button = Button(image_button_frame, text="Вычислить", width=42, height=2, command=btnClickHandler)
button.grid(row=1, column=0)

# Labels
label1 = Label(label_frame, text="Параметры задачи")
label1.grid(row=0, column=1)
label2 = Label(label_frame, text="Начало диапазона (a)")
label2.grid(row=1, column=1)
label3 = Label(label_frame, text="Конец диапазона (b)")
label3.grid(row=2, column=1)
label4 = Label(label_frame, text="Шаг (h)")
label4.grid(row=3, column=1)
label5 = Label(label_frame, text="Текущая функция")
label5.grid(row=4, column=1)

# Input
input1 = Label(input_frame, text="")
input1.grid(row=0, column=2)
inputA = Entry(input_frame)
inputA.grid(row=1, column=2)
inputB = Entry(input_frame)
inputB.grid(row=2, column=2)
inputH = Entry(input_frame)
inputH.grid(row=3, column=2)
input5 = Label(input_frame, text="f(x) = ln(x)")
input5.grid(row=4, column=2)

# Table
tree = ttk.Treeview(table_frame, column=("iCounter", "functionArg", "functionVal"), show="headings")
tree.heading("iCounter", text="№")
tree.heading("functionArg", text="x")
tree.heading("functionVal", text="f(x)")
tree.grid(row=0, column=0)

root.mainloop()
