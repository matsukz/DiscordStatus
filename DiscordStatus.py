import tkinter

texttitle = str(input("タイトルを入力："))

tki = tkinter.Tk()
tki.title(texttitle)
tki.geometry("250x100")

def fac():
    tki.destroy()

calc_button = tkinter.Button(text="EXIT！",command=fac,width=16,height=3)
calc_button.place(x=60,y=35)

tki.mainloop()