import ai_easy
from tkinter import *

ttt_list = [" "," "," "," "," "," "," "," "," ","O","X"]

window= Tk()

class but:

    def bt(self):
        self.btn["text"] = "O"
        ttt_list[self.idx]='O'
        location=ai_easy.ai(ttt_list)
        ttt_list[location]='X'
        b[location].btn["text"]="X"
        if ttt_list[0] == "X" and ttt_list[0] == ttt_list[4] and ttt_list[4] == ttt_list[8] or ttt_list[0] == "X" and ttt_list[0] == ttt_list[1] and ttt_list[1] == ttt_list[2] or ttt_list[3] == "X" and ttt_list[3] == ttt_list[4] and ttt_list[4] == ttt_list[5] or ttt_list[6] == "X" and ttt_list[6] == ttt_list[7] and ttt_list[7] == ttt_list[8] or  ttt_list[2] == "X" and ttt_list[2] == ttt_list[4] and ttt_list[2] == ttt_list[6] or ttt_list[0] == "X" and ttt_list[0] == ttt_list[3] and ttt_list[3] == ttt_list[6] or ttt_list[1] == "X" and ttt_list[1] == ttt_list[4] and ttt_list[4] == ttt_list[7] or ttt_list[2] == "X" and ttt_list[2] == ttt_list[5] and ttt_list[5] == ttt_list[8]:
            print("\nPlayer {} Win!\n".format("X"))
            exit()
            

    def __init__(self,x,y,idx):
        self.btn = Button(window, text=' ',command=self.bt)
        self.btn.place(x=x,y=y)
        self.idx=idx

b=but(30,30,0),but(60,30,1),but(90,30,2),but(30,60,3),but(60,60,4),but(90,60,5),but(30,90,6),but(60,90,7),but(90,90,8)


window.mainloop()


