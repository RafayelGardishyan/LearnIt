import checker
from tkinter import *

x = 1


def main():
    global x
    addwindow = Tk()
    lab = Label(addwindow, text="Voer de naam van de lijst in:", font=20)
    lab.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    ent = Entry(addwindow, font=20, width=20, bd=5)
    ent.grid(row=0, column=2, columnspan=2, padx=10, pady=10)

    lab1 = Label(addwindow, text="Vraag:", font=20)
    lab1.grid(row=1, column=0, padx=10, pady=10)

    ent1 = Entry(addwindow, font=20, width=10, bd=5)
    ent1.grid(row=1, column=1, padx=10, pady=10)

    lab2 = Label(addwindow, text="Antwoord:", font=20)
    lab2.grid(row=1, column=2, padx=10, pady=10)

    ent2 = Entry(addwindow, font=20, width=10, bd=5)
    ent2.grid(row=1, column=3, padx=10, pady=10)

    but = Button(addwindow, font=20, text="Annuleren", width=20, bd=5, fg="red")
    but.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    but1 = Button(addwindow, font=20, text="Toevoegen", width=20, bd=5, fg="green")
    but1.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

    lab3 = Label(addwindow, text=" ", font=20)
    lab3.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

    def addtolib(event):
        global x
        word = ent1.get()
        answer = ent2.get()
        title = ent.get()
        if len(title) > 0:
            if len(word) > 0:
                if len(answer) > 0:
                    else:
                    lab3.configure(text=" ", fg="blue")
                    checker.foldercheck(title, lab3)
                    ent1.delete(0, END)
                    ent2.delete(0, END)
                    with open("lib/" + title + "/" + str(x), "w") as out_word:
                        char = "1"
                        for i in range(len(char)):
                            out_string = str(word)
                            out_word.write(out_string)
                    with open("lib/" + title + "/" + str(x) + "a", "w") as out_answer:
                        char = "1"
                        for i in range(len(char)):
                            out_string = str(answer)
                            out_answer.write(out_string)

                    x = x + 1
                else:
                    lab3.configure(text="Vul de antwoord in", fg="red")
            else:
                lab3.configure(text="Vul de vraag in", fg="red")
        else:
            lab3.configure(text="Vul de titel in", fg="red")

    but.bind("<Button-1>", quit)
    but1.bind("<Button-1>", addtolib)
    addwindow.bind("<Return>", addtolib)

    addwindow.title("Voeg nieuwe lijst toe")
    addwindow.mainloop()
