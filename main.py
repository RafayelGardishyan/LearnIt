from tkinter import *
import add
import learn

root = Tk()
def addf(event):
    add.main()
def learnf(event):
    learn.main()

lab = Label(root, text="Welkom bij LearnIt overhoorprogramma", font="'Helvetica', 20")
lab.grid(row=0, column=0, columnspan=2, padx="20", pady="10")
lab1 = Label(root, text="Klik op '+' om nieuwe lijsten toe te voegen of klik op 'Overhoren' om bestaande lijsten te overhoren", font="'Times', 10")
lab1.grid(row=1, column=0, columnspan=2, padx="20", pady="10")
but = Button(root, text="+", font="'Times', 15", width="5", bd="10", fg="green")
but.grid(row=2, column=0, padx="10", pady="5")
but1 = Button(root, text="Overhoren", font="'Times', 15", width="20", bd="10", fg="blue")
but1.grid(row=2, column=1, padx="10", pady="5")

but1.bind("<Button-1>", learnf)
but.bind("<Button-1>", addf)

root.title("LearnIt")
root.mainloop()