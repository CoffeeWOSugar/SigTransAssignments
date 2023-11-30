import numpy as np
import soundfile as sf

def x(t):
    f = 15000
    return np.sin(f*2*np.pi*t)

sampling_frequency1 = 2000
sampling_period1 = 1/sampling_frequency1

k1 = np.arange(0, 5, sampling_period1)

xk1 = x(k1)

sampling_frequency2 = 300000
sampling_period2 = 1/sampling_frequency2

k2 = np.arange(0, 1, sampling_period2)

xk2 = x(k2)



# overlaps the tones
sf.write('tone1.wav', xk1, sampling_frequency1)
sf.write('tone2.wav', xk2, sampling_frequency2)