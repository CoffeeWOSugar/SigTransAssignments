import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from time import sleep

# Time step delta t
dt = 0.00001 #0.01ms
start_time = 0
stop_time = 1

# Generate a time vector 't' (seconds?)
t = np.arange(start_time, stop_time, dt) # (start, stop, increment)


alpha = 1000*np.pi


## 
i = 0
for time in t:
    
    i+=1

# Create new figure
fig, ax = plt.subplots()
# Plot the curve of with x-values 't' and y values 'x' into 
# the figure 'ax' with the legend entry 'My signal'.
ax.plot(t, x, label='My signal 1')

ax.set_xlabel('t') 
ax.set_ylabel('x') 
ax.legend()

plt.title('Uppgift 2a')

plt.show()


#ax.set_xlim()
#ax.set_ylim()
#ax.grid()

