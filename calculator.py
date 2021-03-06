from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "error"
                
        scvalue.set(value)
        screen.update  
        
        
    elif text == "c":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()
    

root = Tk()
root.geometry("400x700")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root,textvar=scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)
root.title("Calculator")

f = Frame(root, bg="grey")

b = Button(f, text= '9',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '8',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '7',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)

f.pack()

f = Frame(root, bg="white")

b = Button(f, text= '6',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '5',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '4',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)

f.pack()
f = Frame(root, bg="grey")

b = Button(f, text= '3',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '2',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '1',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)

f.pack()

f = Frame(root, bg="white")

b = Button(f, text= '0',padx=12,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '+',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '-',padx=9,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= '*',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '/',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= '%',padx=11,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)

f.pack()
f = Frame(root, bg="white")

b = Button(f, text= '=',padx=8,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= 'c',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)
b = Button(f, text= ':)',padx=10,pady=10,font ="lucida 15 bold" )
b.bind("<Button-1>",click)
b.pack(side=LEFT,padx=15,pady=15)

f.pack()




root.mainloop()
