import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv

fig, ax = plt.subplots()

time_remaining = 40
time_elapsed = 5
size=[time_remaining,time_elapsed]
labels=["remaining", "elapsed"]
ax.pie(size, labels=labels)

def myupdate(i):
    if (time_remaining > 0):
        ax.clear()
        time_remaining -= 1
        time_elapsed += 1
        size=[time_remaining,time_elapsed]
        ax.pie(size, labels=labels)
    
myanimation=FuncAnimation(fig, myupdate, interval=1000)
plt.show()