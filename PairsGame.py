#2018128

# ABC PAIRS GAME

#Importing modules

import tkinter as tk
from tkinter import *
import random
import time
from tkinter import messagebox
import threading

# making local variables into global variables

global T
global count
global sc

#
# this is Level 2
#

def level2():
    window=tk.Tk()

    bgcolor='#e4f4fb'
    window.configure(bg=bgcolor)
    window.geometry("725x400")

    messagebox.showinfo("Pairs Game", "Match all tiles to win")
    
    Label(window, text="Pairs Game",bg=bgcolor, fg="#00b7f0", font="comicsans 18 bold") .grid(row=0,column=0,padx=0,sticky=W)
    Label(window, text="Match all the tiles to win\n",bg=bgcolor, fg="black", font="none 12 bold") .grid(row=1,column=0,padx=0,sticky=W)


    global T
    global count
    global sc
    sc=0
    count=67
    T=[]

# Play Again and Exit Buttons

    def close_window():
            window.destroy()

    def restart():
        close_window()
        main()

    def newwindow():
        window2=Toplevel()
        window2.configure(bg=bgcolor)
        Button(window2,text="Play Again",width=14,bg=bgcolor, fg="black", font="none 12 bold",command=restart) .grid(row=0, column=15, sticky=W)
        Button(window2,text="Exit",width=14,bg=bgcolor, fg="black", font="none 12 bold",command=close_window) .grid(row=1, column=15, sticky=W)

# List to help with tile click count

    def start_window():
        global T
        T=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#Function that adds and substracts the Score
        
    def score(f1,f2,r,c):
        global sc
        global T
        if f1==f2:
            sc= sc+20
        else:
            T[r][c]+=1
            sc=sc + (-5 * T[r][c])
           
        scorelabel= Label(window, text="Score:"+" "+str(sc), bg=bgcolor, fg="black", font="none 12 bold") .grid(row=12,column=9,sticky=W)
        levellabel= Label(window, text="Level:"+"2", bg=bgcolor, fg="black", font="none 12 bold") .grid(row=11,column=9,sticky=W)

# 60 Countdown timer
        
    def start_count():
        global count
        global totalscore
        for i in range(count):
            time.sleep(1)
            Label (window, text="Countdown :", bg=bgcolor,fg="black", font="none 12 bold") .grid(row=0,column=15,sticky=E)
            Label (window, text='00', bg=bgcolor, fg="black", font="none 12 bold") .grid(row=0,column=27,sticky=E)
            Label (window, text=str(count-i), bg=bgcolor, fg="black", font="none 12 bold") .grid(row=0,column=27,sticky=E)
        tk.messagebox.showinfo(title='Ended!', message='Game over! Score:'+' '+str(sc))
        newwindow()   
        
    class MemoryTile:
        def __init__(self, parent):
            self.parent = parent
            r=10
            c=0
        
            self.buttons = [[tk.Button(window,
                                       width=9,
                                       height=4,
                                       command=lambda row=row, column=column: self.choosetile(row, column)
                                       ) for column in range(4)] for row in range(3)]
            for row in range(3):
                r=r+1
                c=0
                for column in range(4):
                    c=c+1
                    self.buttons[row][column].grid(row=r, column=c)
            self.first = None
            self.drawboard()
            
#tiles will show for 8 seconds by using the following codes
            
            self.show_tiles()
            self.parent.after(8000, self.hide_alltiles)

        def show_tiles(self):
            for r in range(3):
                for c in range(4):
                    self.buttons[r][c].config(text=self.answer[r][c])

        def hide_alltiles(self):
            for r in range(3):
                for c in range(4):
                    self.buttons[r][c].config(text='')

#this will add values to the grid
                    
        def drawboard(self):
            self.answer = list('DDDDEEEEFFFF')
        
            random.shuffle(self.answer)
            self.answer = [self.answer[:4],
                           self.answer[4:8],
                           self.answer[8:12],
                           self.answer[12:]]
            for row in self.buttons:
                for button in row:
                    button.config(text='',bg='#33cfff', state=tk.NORMAL)
            self.start_time = time.monotonic()

#function to choose the tiles           

        def choosetile(self, row, column):
            global sc,totalscore, lvl, count
            self.buttons[row][column].config(text=self.answer[row][column])
            self.buttons[row][column].config(state=tk.DISABLED)
            
            
            if not self.first:
                self.first = (row, column)
            else:
                a,b = self.first
                v1=self.answer[row][column]
                v2=self.answer[a][b]
                     
                score(v1,v2,row,column)

                if self.answer[row][column] == self.answer[a][b]:
                    self.answer[row][column] = ''
                    self.answer[a][b] = ''
                    if not any(''.join(row) for row in self.answer):
                        duration = time.monotonic() - self.start_time
                        sc=sc+(count - int(duration))
                        messagebox.showinfo(title='Success!', message='Good job! Score:'+' '+str(sc)+'(Bonus:'+str(count - int(duration))+')')
                        tk.messagebox.showinfo(title='Ended!', message='Game over! Score:'+' '+str(sc))
                        newwindow()
                        self.parent.after(1000, self.drawboard)
                else:
                    self.parent.after(500, self.hidetiles, row, column, a, b)
                self.first = None

# function to hide the tiles

        def hidetiles(self, x1, y1, x2, y2):
                self.buttons[x1][y1].config(text='', state=tk.NORMAL)
                self.buttons[x2][y2].config(text='', state=tk.NORMAL)

# threading to allow multiple processes

    t = threading.Thread(target = start_count)
    t.daemon = True    #-----this is the one which says to run in back ground ---- so allow mutiple process.
    t.start()        #this wil start thread to run
    start_window()
    
    memory_tile = MemoryTile(window)

    window.mainloop()

#--------------------Level 2 Ends --------------------


#
# This is Level 1
#


def main():
    window=tk.Tk()

    bgcolor='#e4f4fb'
    window.configure(bg=bgcolor)
    window.geometry("725x400")

    messagebox.showinfo("Pairs Game", "Press Ok to Start the Game")
    
    Label(window, text="Pairs Game",bg=bgcolor, fg="#00b7f0", font="comicsans 18 bold") .grid(row=0,column=0,padx=0,sticky=W)
    Label(window, text="Match all the tiles to win\n",bg=bgcolor, fg="black", font="none 12 bold") .grid(row=1,column=0,padx=0,sticky=W)

    global T
    global count
    global sc
    sc=0
    count=60
    T=[]
    
    def close_window():
            window.destroy()

    def restart():
        close_window()
        main()

    def nextlevel():
        close_window()
        level2()
        
# play again and exit button

    def newwindow():
        window2=Toplevel()
        window2.configure(bg=bgcolor)
        Button(window2,text="Play Again",width=14,bg=bgcolor, fg="black", font="none 12 bold",command=restart) .grid(row=0, column=15, sticky=W)
        Button(window2,text="Exit",width=14,bg=bgcolor, fg="black", font="none 12 bold",command=close_window) .grid(row=1, column=15, sticky=W)

#next level and exit button

    def nextwindow():
        window3=Toplevel()
        window3.configure(bg=bgcolor)
        Button(window3,text="Next Level",width=14,bg=bgcolor, fg="black", font="none 12 bold",command=nextlevel) .grid(row=0, column=15, sticky=W)
        Button(window3,text="Exit Game",width=14,bg=bgcolor, fg="black", font="none 12 bold",command=close_window) .grid(row=1, column=15, sticky=W)


    def start_window():
        global T
        T=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        
#Score System

    def score(f1,f2,r,c):
        global sc
        global T
        if f1==f2:
            sc= sc+20
        else:
            T[r][c]+=1
            sc=sc + (-5 * T[r][c])
           
        scorelabel= Label(window, text="Score:"+" "+str(sc), bg=bgcolor, fg="black", font="none 12 bold") .grid(row=12,column=9,sticky=W)
        levellabel= Label(window, text="Level:"+"1", bg=bgcolor, fg="black", font="none 12 bold") .grid(row=11,column=9,sticky=W)

#Countdown
        
    def start_count():
        global count
        for i in range(count):
            time.sleep(1)
            Label (window, text="Countdown :", bg=bgcolor,fg="black", font="none 12 bold") .grid(row=0,column=15,sticky=E)
            Label (window, text='00', bg=bgcolor, fg="black", font="none 12 bold") .grid(row=0,column=27,sticky=E)
            Label (window, text=str(count-i), bg=bgcolor, fg="black", font="none 12 bold") .grid(row=0,column=27,sticky=E)

        tk.messagebox.showinfo(title='Ended!', message='Game over! Total Score:'+' '+str(sc))#+'(Bonus:'+(count)+')')
        newwindow()   

# Game

    class MemoryTile:
        def __init__(self, parent):
            self.parent = parent
            r=10
            c=0
        
            self.buttons = [[tk.Button(window,
                                       width=9,
                                       height=4,
                                       command=lambda row=row, column=column: self.choosetile(row, column)
                                       ) for column in range(4)] for row in range(3)]
            for row in range(3):
                r=r+1
                c=0
                for column in range(4):
                    c=c+1
                    self.buttons[row][column].grid(row=r, column=c)
            self.first = None
            self.drawboard()
            
#Adding the values to the grid
            
        def drawboard(self):
            self.answer = list('AAAABBBBCCCC')
            random.shuffle(self.answer)
            self.answer = [self.answer[:4],
                           self.answer[4:8],
                           self.answer[8:12],
                           self.answer[12:]]
            for row in self.buttons:
                for button in row:
                    button.config(text='',bg='#33cfff', state=tk.NORMAL)
            self.start_time = time.monotonic()
            
#function to choose tiles

        def choosetile(self, row, column):
            global sc, count
            self.buttons[row][column].config(text=self.answer[row][column])
            self.buttons[row][column].config(state=tk.DISABLED)
            
            
            if not self.first:
                self.first = (row, column)
            else:
                a,b = self.first
                v1=self.answer[row][column]
                v2=self.answer[a][b]
                     
                score(v1,v2,row,column)

                
                if self.answer[row][column] == self.answer[a][b]:
                    self.answer[row][column] = ''
                    self.answer[a][b] = ''
                    if not any(''.join(row) for row in self.answer):
                        duration = time.monotonic() - self.start_time
                        sc=sc+(count - int(duration))
                        messagebox.showinfo(title='Success!', message='Good job! Score:'+' '+str(sc)+' '+'(Bonus:'+" "+str(count - int(duration))+')')
                        nextwindow()
                        
                        self.parent.after(1000, self.drawboard)
                else:
                    self.parent.after(500, self.hidetiles, row, column, a, b)
                self.first = None
                
# func to Hide tiles

        def hidetiles(self, x1, y1, x2, y2):
                self.buttons[x1][y1].config(text='', state=tk.NORMAL)
                self.buttons[x2][y2].config(text='', state=tk.NORMAL)
                

# threading to allow multiple processes

    t = threading.Thread(target = start_count)
    t.daemon = True    #-----this is the one which says to run in back ground ---- so allow mutiple process.
    t.start()        #this wil start thread to run

    start_window()

    memory_tile = MemoryTile(window)

    window.mainloop()

main()
