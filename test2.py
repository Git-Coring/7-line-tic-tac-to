import ai_easy
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from copy import deepcopy
import functools as fc
from tkinter import messagebox as msg

ttt_list = [" "," "," "," "," "," "," "," "," ","O","X"]

class Board:
    def __init__(self,other=None):
        self.player = 'X'
        self.opponent = 'O'
        self.empty = ' '
        self.size = 3
        self.fields = {}
        for y in range(self.size):
            for x in range(self.size):
                self.fields[x,y] = self.empty
        if other:
            self.__dict__ = deepcopy(other.__dict__)
    
class Start:
    def __init__(self):
        self.root = Tk()
        self.root.title('Tic - Tac - Toe Game')
        self.root.geometry("606x770+600+130")
        self.root.config(bg='white')
        self.root.resizable(False,False)
        self.l1 = Label(self.root,text="Tic - Tac - Toe",font='Times 65 bold',bg='white', fg='black')
        self.l2 = Label(self.root,text="Name :",font='Times 36 bold',bg='white', fg='black')
        self.b1 = Button(self.root,text='Start', font='Times 20 bold', bg='gray', fg='white', command=self.start)
        ## ID #####
        self.id = Text(self.root,font='Times 35 bold',bg='gray')
        self.id.place(x=245,y=480, width=300,height=60)
        ###########
        self.l1.place(x=30,y=180)
        self.l2.place(x=67,y=475)
        self.b1.place(x=245,y=580, width=130,height=60)
    def mainloop(self):
        self.root.mainloop()  
    def start(self):
        self.root.destroy()
        Level().mainloop()

class Level:
    def __init__(self):
        self.root = Tk()
        self.root.title('Tic - Tac - Toe Game')
        self.root.geometry("606x770+600+130")
        self.root.config(bg='white')
        self.root.resizable(False,False)
        self.l1 = Label(self.root,text="Level",font='Times 65 bold',bg='white', fg='black')
        self.b1 = Button(self.root,text='Beginner', font='Times 25 bold', bg='gray', fg='white' , command=self.beginner)
        self.b2 = Button(self.root,text='Advanced', font='Times 25 bold', bg='gray', fg='white', command=self.advance)
        self.l1.place(x=200,y=170)
        self.b1.place(x=210,y=430,height=100,width=200)
        self.b2.place(x=210,y=580,height=100,width=200)
    def mainloop(self):
        self.root.mainloop()
    def beginner(self):
        self.root.destroy()
        Beginner().mainloop()
    def advance(self):
        self.root.destroy()
        Advance().mainloop()

class Beginner:
    def loc(self,x,y):
        self.buttons[x,y]['text']="O"
        ttt_list[y*3+x]='O'
        k=ai_easy.easy(ttt_list)
        ttt_list[k]='X'
        self.buttons[k%3,int(k/3)]['text']='X'

    def __init__(self):
        self.frame = Tk()
        self.frame.title('TicTacToe')
        self.frame.geometry("950x547+500+270")
        self.frame.config(bg='white')
        self.frame.resizable(width=False, height=False)
        self.buttons = {}
        self.board = Board()
        for x,y in self.board.fields:
            button = Button(self.frame, command=fc.partial(self.loc,x,y), font='Times 20 bold', bg='gray', fg='white',width=8, height=4, bd=4,text=' ')
            button.grid(row=y, column=x)
            self.buttons[x,y] = button
        exitBrt = Button(self.frame, text='exit', font='Times 16 bold', bg='white', fg='black', height=1, width=8, bd=4, command=lambda: self.exit())
        exitBrt.grid(row=self.board.size+2, column=0, columnspan=self.board.size, sticky=E+W)

    def mainloop(self):
        self.frame.mainloop()
    def exit(self):
        self.frame.destroy()
        Level().mainloop()

class Advance:
    def loc(self,x,y):
        self.buttons[x,y]['text']="O"
        ttt_list[y*3+x]='O'
        k=ai_easy.ai(ttt_list)
        ttt_list[k]='X'
        self.buttons[k%3,int(k/3)]['text']='X'

    def __init__(self):
        self.frame = Tk()
        self.frame.title('TicTacToe')
        self.frame.geometry("950x547+500+270")
        self.frame.config(bg='white')
        self.frame.resizable(width=False, height=False)
        self.buttons = {}
        self.board = Board()
        for x,y in self.board.fields:
            button = Button(self.frame, command=fc.partial(self.loc,x,y), font='Times 20 bold', bg='gray', fg='white', width=8, height=4, bd=4,text=' ')
            button.grid(row=y, column=x)
            self.buttons[x,y] = button
        exitBrt = Button(self.frame, text='exit', font='Times 16 bold', bg='white', fg='black', height=1, width=8, bd=4, command=lambda: self.exit())
        exitBrt.grid(row=self.board.size+2, column=0, columnspan=self.board.size, sticky=E+W)

    def mainloop(self):
        self.frame.mainloop()
    def exit(self):
        self.frame.destroy()
        Level().mainloop()

if __name__ == '__main__':
  Start().mainloop()
