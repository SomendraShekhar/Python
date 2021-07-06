from tkinter import *

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def mod(a,b):
    return a % b

def lcm(a,b):
    L = a if a>b else b
    while L<= a*b:
        if L%a==0 and L%b == 0:
            return L
        L = L + 1

def hcf(a,b):
    H = a if a<b else b
    while H>=1:
        if a%H==0 and b % H == 0:
            return H
        H = H - 1

def extract_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            float(t)
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys(): # addition
            try:
                l = extract_from_text(text)
                r = operations[word.upper()](l[0],l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END, 'something went wrong please enter again')
            finally:
                break

        else:
            list.delete(0, END)
            list.insert(END, 'something went wrong please enter again')

operations = { '+' :add , 'ADD':add , 'ADDITION':add, 'SUM':add, 'PLUS':add, '-':sub, 'SUB':sub,
                'DIFFERENCE':sub, 'MINUS':sub, 'SUBTRACT':sub, 'LCM':lcm, 'HCF':hcf, '*':mul,
               'PRODUCT':mul, 'MULTIPLICATION':mul, 'MULTIPLY':mul, '/':div, 'DIVISION':div,
               'DIV':div, 'DIVIDE':div, 'MOD':mod, '%':mod, 'REMAINDER':mod, 'MODULUS':mod}

win = Tk()
win.geometry('500x300')
win.title("Smart Calculator")
win.configure(background="skyblue")

l1 = Label(win,text="I am a Smart Calculator", font="Cambria 12 bold", width=25, padx=3)
l1.place(x=150,y=10)

l2 = Label(win,text="My name is PythonHub", font="Cambria 12 bold", padx=3)
l2.place(x=180,y=45)

l3 = Label(win,text="What can I help you?", font="Cambria 12 bold", padx=3)
l3.place(x=176,y=130)

textin = StringVar()
e1 = Entry(win, width=30, textvariable=textin)
e1.place(x=164, y=162)

b1 = Button(win, text="Get Result", font="Cambria 12 bold", command=calculate)
b1.place(x=210, y=200)

list = Listbox(win, width=35, height=2)
list.place(x=145, y=248)

win.mainloop()