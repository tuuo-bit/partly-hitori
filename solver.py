import numpy as np
import math
import tkinter as tk
from tkinter import ttk
from tkinter import *
class hitori:
    g=[]
    st=[]
    d=1
    def __init__(s):
        s.color = [ "#26648E","#53D2DC", "#4F8FC0", "#FFBA69"]
        s.font = [ "Bahnschrift 18", "Bahnschrift 16", "Bahnschrift 14"]
        s.window = Tk()
        s.window.configure( background=s.color[0])
        s.window.title( "brute forced, turns out to be a np-complete, so its incomplete but not wrong")
        s.window.resizable( False, False)
        center_x = int( (s.window.winfo_screenwidth() - 720)/2)
        center_y = int( (s.window.winfo_screenheight() - 400)/2)
        s.window.geometry( f"720x400+{center_x}+{center_y}")
        s.label2Var = tk.StringVar(value="O:  X:  Percentage Solved:")
    def UI(s):
        # input frame
        s.frame1 = Frame( master=s.window, height=380, width=345, background=s.color[1])
        s.frame1.place( anchor="w", rely=0.5, relx=0.014)
        s.entry1 = Text( master=s.frame1, font=s.font[0], background=s.color[2], foreground=s.color[3], borderwidth=0, padx=5)
        s.entry1.place( anchor="sw", relx=0.03, rely=0.974, width=325, height=325)
        s.button = Button( master=s.frame1, text=">", font=s.font[1], borderwidth=0, background=s.color[3], command=s.fillGrid)
        s.button.place( anchor="ne", rely=0.03, relx=0.97, width=25, height=25)
        s.label1 = Label( master=s.frame1, background=s.color[0], text="Get Your Hitori Partly Solved!", font=s.font[2], foreground=s.color[3])
        s.label1.place( anchor="nw", relx=0.03, rely=0.03, height=25, width=290)
        # output frame
        s.frame2 = Frame( master=s.window, height=380, width=345, background=s.color[1])
        s.frame2.place( anchor="e", rely=0.5, relx=0.986)
        s.entry2 = Text( master=s.frame2, font=s.font[0], background=s.color[2], foreground=s.color[3], borderwidth=0, padx=5)
        s.entry2.place( anchor="sw", relx=0.03, rely=0.974, width=325, height=325)
        s.label2 = Label( master=s.frame2, background=s.color[0], text="",textvariable=s.label2Var, font=s.font[2], foreground=s.color[3])
        s.label2.place( anchor="nw", relx=0.03, rely=0.03, height=25, width=325)
        #
    def fillGrid( s):
        try:
            values = list(map(int,list("".join(s.entry1.get( "1.0","end").split()))))
            s.d=int(math.sqrt( len(values)))
            s.g=np.array( values, dtype='int').reshape(s.d,s.d)
            s.st=np.full([s.d,s.d],0,dtype='int')
            if not values:
                s.label2Var.set("O:  X:  Percentage Solved:")
                s.entry2.delete( 1.0, END)
                return
            s.solve()
            s.summarize()
            s.returnStatus()
        except:
            s.entry2.delete( 1.0, END)
            s.entry2.insert(END,"Error\nCheck Input")
        return
    def validateCoord( s, x):
        x = np.atleast_1d( x)
        return np.array( np.array(x>=0) & np.array(x<s.d)).all()
    def summarize( s):
        o = (s.st==2).sum()
        x = (s.st==1).sum()
        s.label2Var.set( f"O: { o}  X:  { x}  Percentage Solved: {int((o+x)*100/(s.d**2))}%")
        return
    def countX( s, x, y):
        ele = s.g[x,y]
        return (s.g[x,:] == ele).sum(),np.argwhere( s.g[x,:] == ele).flatten()
    def countY( s, x, y):
        ele = s.g[x,y]
        return (s.g[:,y] == ele).sum(),np.argwhere( s.g[:,y] == ele).flatten()
    def updateStatus( s, x, y, new):
        if s.validateCoord( [ x, y]) and s.st[x,y] == 0:
            s.st[x,y] = new
            if new == 1:
                s.updateSafe( x, y)
                return
            else:
                s.markDuplicateY( x, y)
                s.markDuplicateX( x, y)
                return
        return
    def updateSafe( s, x, y):
        s.updateStatus( x-1, y, 2)
        s.updateStatus( x+1, y, 2)
        s.updateStatus( x, y-1, 2)
        s.updateStatus( x, y+1, 2)
        return
    def markDuplicateX( s, x, y):
        x = np.atleast_1d(x)
        ele = s.g[x[0],y]
        for i in range(s.d):
            if s.g[i,y] == ele and i not in x:
                s.updateStatus( i, y, 1)
        return
    def markDuplicateY( s, x, y):
        y = np.atleast_1d(y)
        ele = s.g[x,y[0]]
        for i in range(s.d):
            if s.g[x,i] == ele and i not in y:
                s.updateStatus( x, i, 1)
        return
    def markTriple( s, x, y):
        mid = s.g[x,y]
        if s.validateCoord([x-1,x+1]) and (mid == s.g[x-1,y] and mid == s.g[x+1,y]):
            s.updateStatus( x, y, 2)
            s.updateStatus( x-1, y, 1)
            s.updateStatus( x+1, y, 1)
        if s.validateCoord([y-1,y+1]) and mid == s.g[x,y-1] and mid == s.g[x,y+1]:
            s.updateStatus( x, y, 2)
            s.updateStatus( x, y-1, 1)
            s.updateStatus( x, y+1, 1)
        return
    def markBetweenPair( s, x, y):
        mid = s.g[x,y]
        if s.validateCoord([x-1,x+1]) and s.g[x-1,y] == s.g[x+1,y] and mid != s.g[x-1,y]:
            s.updateStatus( x, y, 2)
        if s.validateCoord([y-1,y+1]) and s.g[x,y-1] == s.g[x,y+1] and mid != s.g[x,y-1]:
            s.updateStatus( x, y, 2)
        return
    def pairInduction( s, x, y):
        crr = s.g[x,y]
        if s.validateCoord( [ y-1, y+1]):
            if s.g[x,y-1] == crr and s.g[x,y+1] != crr:
                s.markDuplicateY(x,[y,y-1])
            if s.g[x,y-1] != crr and s.g[x,y+1] == crr:
                s.markDuplicateY(x,[y,y+1])
        if s.validateCoord( [ x-1, x+1]):
            if s.g[x-1,y] == crr and s.g[x+1,y] != crr:
                s.markDuplicateX([x,x-1],y)
            if s.g[x-1,y] != crr and s.g[x+1,y] == crr:
                s.markDuplicateX([x,x+1],y)
        return
    def markUnique( s, x, y):
        if s.countX( x, y)[0] + s.countY( x, y)[0] == 2:
            s.updateStatus( x, y, 2)
    def solve( s):
        for i in range(h.d):
            for j in range(h.d):
                s.markUnique( i, j)
                s.markTriple( i, j)
                s.markBetweenPair( i, j)
                s.pairInduction( i, j)
        return
    def returnStatus( s):
        x = np.full(shape=(s.d,s.d),fill_value="", dtype="U8")
        for i in range(s.d):
            for j in range(s.d):
                if s.st[i,j] == 2:
                    x[i,j]="O"
                elif s.st[i,j] == 1:
                    x[i,j]="X"
                else:
                    x[i,j]=str(s.g[i,j])
        s.entry2.delete( 1.0, END)
        for ele in x:
            s.entry2.insert(END," ".join(ele)+'\n')
        return
h=hitori()
h.UI()
h.window.mainloop()
#s="3322431525541222224325413"
#s="5143415452434153525514523"
#s="4153212355344513515452513"