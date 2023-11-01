#import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from time import sleep

def x1func(t):
    x1f = 100
    return np.sin(x1f*2*np.pi*t)

def x2func(t):
    x2f = 1000
    return np.sin(x2f*2*np.pi*t)

# Time step delta t
dt = 0.000001
start_time = 0
stop_time = 0.01

# Generate a time vector 't' (seconds?)
t = np.arange(start_time, stop_time, dt) # (start, stop, increment)

###################################
# Generate signals with np.sin(t)
###################################

x1 = np.array([x1func(time) for time in t])
x2 = np.array([x2func(time) for time in t])

#1c
# Play the two signals x1(t) and x2(t)
#sd.play(x1, 1/dt, blocking=True)
#sleep(1)
#sd.play(x2, 1/dt, blocking=True)
#sleep(1)

# Create new figure
fig, ax = plt.subplots()
# Plot the curve of with x-values 't' and y values 'x' into 
# the figure 'ax' with the legend entry 'My signal'.
ax.plot(t, x1, label='My signal 1')
ax.plot(t, x2, label='My signal 2')

ax.set_xlabel('t [s]') 
ax.set_ylabel('x []') 
ax.legend()

plt.savefig("fig_1b")


#ax.set_xlim()
#ax.set_ylim()
#ax.grid()

################################ 2 ######################################################

# Time step delta t
dt = 0.00001 #0.01ms
start_time = 0
stop_time = 0.02

def h(t):
    alpha = 1000*np.pi
    u = 0 if t < 0 else 1
    return alpha**2*t*np.exp(-alpha*t)*u

def y(x, tstart, tstop, dt):
    h_arr = np.array([h(t) for t in np.arange(tstart, tstop, dt)])
    y = signal.convolve(x, h_arr, method = 'direct')*dt
    return y[0:x.shape[0]] 


# Generate a time vector 't' 
t2 = np.arange(start_time, stop_time, dt) # (start, stop, increment)

###################################
# Generate signals with np.sin(t)
###################################

x = np.array([h(time) for time in t2])

dirac_x = np.zeros(int((stop_time - start_time)/dt)+1)
dirac_x[0] = 1/dt

dirac_y = y(dirac_x, start_time, stop_time, dt)


# Create new figure
fig, ax = plt.subplots()

ax.set_xlim(right = 0.005)

# Plot the curve of with x-values 't' and y values 'x' into 
# the figure 'ax' with the legend entry 'My signal'.
ax.plot(t2, x, 'k', label='impulse response')
ax.plot(t2, dirac_y, "y--", label='Convulution with Dirac delta')

ax.set_xlabel('t [s]') 
ax.set_ylabel('x []') 
ax.legend()

plt.savefig("fig_2a")

## upg 2b

x1 = np.array([x1func(t) for t in np.arange(start_time, stop_time, dt)])
x2 = np.array([x2func(t) for t in np.arange(start_time, stop_time, dt)])

y1 = y(x1, start_time, stop_time, dt)
y2 = y(x2, start_time, stop_time, dt)

fig, ax = plt.subplots()

ax.plot(t2, y1, label='y1(t)')
ax.plot(t2, y2, label='y2(t)')
ax.plot(t2, x1, label='x1(t)')
ax.plot(t2, x2, label='x2(t)')

ax.set_xlabel("t [s]")
ax.set_ylabel("x []")
ax.legend()

plt.savefig("fig_2b")


### upg 2c

x3 = np.array([x1func(t) + x2func(t) for t in np.arange(start_time, stop_time, dt)])

y3 = y(x3, start_time, stop_time, dt)

fig, ax = plt.subplots()


ax.plot(t2, y3, 'k', label='y3(t)')
ax.plot(t2, y1+y2, "y--", label='y1(t) + y2(t)')

ax.set_xlabel("t [s]")
ax.set_ylabel("x []")
ax.legend()

plt.savefig("fig_2c")
