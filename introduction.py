from tkinter import*
root = Tk()
root.title('Introduction')
#root.geometry('300x200')
#Creating the label widgets
myLabel = Label(root, text = 'Hello World')
#myLabel.grid(column = 4,row = 5)
#myLabel.pack(expand = True,fill = None,side='top')
myLabel.place(x=50,y=56)
myButton = Button(root,text='Stop',command = root.destroy,bg='Red')
#myButton.pack(side = 'top')
#myButton.grid(column = 100,row = 10,pady=50,rowspan=500)
myButton.place(x = 25,y=63)
myButton2 = Button(root,text='Stop',command = root.destroy,bg='Red')
#myButton2.grid(columnspan = 2,ipadx=50,ipady = 50)
myButton2.place(x = 36 , y = 85)
root.mainloop()