import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.animation import FuncAnimation
import csv

fig, ax = plt.subplots()

minutes = 45

time_remaining = minutes*60
time_elapsed = 0
size=[time_remaining,time_elapsed]
labels=["remaining", "elapsed"]
colors=['g','w']
ax.pie(size, labels=labels, colors=colors)

def myupdate(i):
    global time_remaining
    global time_elapsed
    global colors

    if (time_remaining > 0):
        ax.clear()
        time_remaining -= 1
        time_elapsed += 1
        size=[time_remaining,time_elapsed]
        ax.pie(size, labels=labels, colors=colors)
    
myanimation=FuncAnimation(fig, myupdate, interval=1000)
plt.show()