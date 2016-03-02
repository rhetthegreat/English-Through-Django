import os
import curses
import sys
import time
from threading import Thread
now = time.time()
wordtime=[]
win = curses.initscr()
x=0
def playSound():
    time.sleep(1)
    os.system("afplay "+sys.argv[-1]+"")
Thread(target=playSound).start()
while x<5:
    win.getch()
    x=  time.time()-now
    print x
    wordtime.append(x)
print wordtime
curses.endwin()
