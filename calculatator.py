from tkinter import * 
cal = Tk()    
cal.iconbitmap(r"index.ico")
x = 0
y=69
cal.title("Calculator")
cal.resizable(False, False)
cal.geometry('350x420')
Display = Entry(cal, width = 22,font=("Helvetica", 50))
def add_to_display(text):
    myel = Display.get()
    if(text != 'AC' and text != '=' and text != 'C'):
        Display.insert(INSERT,text)
    elif(text == "="):
        if('÷' in myel):
          myel= myel.replace("÷",'/')
        if('×' in myel):
            myel = myel.replace("×",'*')
        if('^' in myel):
            myel = myel.replace('^','**')
        if(myel[-1] == "+" or myel[-1] == "-"):
            myel = Display.get()[:-1]
            Display.delete(0, END)
            Display.insert(INSERT,myel)
        else:
            myel = eval(myel)
            Display.delete(0, END)
            Display.insert(INSERT,myel)
    elif(text == "AC"):
        Display.delete(0, END)
    elif(text == "C"):
       myel = Display.get()[:-1]
       Display.delete(0, END)
       Display.insert(INSERT,myel)

buttons = []
arr_of_text = ["1","2","3","4","5","6","7","8","9","0",".","+","-","×","÷","(",")","C","AC",'^',"="]

for text in arr_of_text:
    buttons.append(Button( text=text,activebackground = "grey",justify=CENTER,command=lambda m=text:add_to_display(m)))

for button in buttons:
    button.config(font=("Helvetica",30,"bold"))
    button.place(x=x, y=y,width = 120, height = 50)
    x+=120
    if x == 360:
        y+=50
        x = 0
Display.pack()
cal.mainloop()  
