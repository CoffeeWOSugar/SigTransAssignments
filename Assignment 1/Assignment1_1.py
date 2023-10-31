import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from time import sleep

# Time step delta t
dt = 0.0005
start_time = 0
stop_time = 1

# Generate a time vector 't' (seconds?)
t = np.arange(start_time, stop_time, dt) # (start, stop, increment)

###################################
# Generate signals with np.sin(t)
###################################

x1 = np.zeros(int((stop_time - start_time)/dt))
x2 = np.zeros(int((stop_time - start_time)/dt))
x1f = 100
x2f = 1000

def x1func(x):
    return np.sin(x1f*x)

def x2func(x):
    return np.sin(x2f*x)


## 
i = 0
for time in t:
    x1[i] = 5 * x1func(time)
    x2[i] = 5 * x2func(time)
    i+=1

# Play the two signals x1(t) and x2(t)
sd.play(x1, 1/dt, blocking=True)
sleep(1)
sd.play(x2, 1/dt, blocking=True)
sleep(1)

# Create new figure
fig, ax = plt.subplots()
# Plot the curve of with x-values 't' and y values 'x' into 
# the figure 'ax' with the legend entry 'My signal'.
ax.plot(t, x1, label='My signal 1')
ax.plot(t, x2, label='My signal 2')

ax.set_xlabel('t') 
ax.set_ylabel('x') 
ax.legend()

plt.title('Uppgift 1b')

plt.show()


#ax.set_xlim()
#ax.set_ylim()
#ax.grid()

