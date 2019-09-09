import tkinter
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
mainWindow=tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry('640x480+400+8')
label=tkinter.Label(mainWindow,text="Hello Deutschland")
label.pack(side='top')
leftFrame=tkinter.Frame(mainWindow)
leftFrame.pack(side='left',anchor='n',fill=tkinter.Y,expand=False)
canvas=tkinter.Canvas(leftFrame,relief='raised',borderwidth=2)
#canvas.pack(side='top',fill=tkinter.BOTH,expand=True )# use optional expand to work in expanding in all directions
canvas.pack(side='left',anchor='n')
rightFrame=tkinter.Frame(mainWindow)
rightFrame.pack(side='right',anchor='n',expand=True)
button1=tkinter.Button(rightFrame,text="button1")
button2=tkinter.Button(rightFrame,text="button2")
button3=tkinter.Button(rightFrame,text="button3")
button1.pack(side="top")
button2.pack(side="top")
button3.pack(side="top")
#configure the columns


mainWindow.mainloop()

