import soundfile as sf
import numpy as np
import sounddevice as sd

data, samplerate = sf.read("Recording_1.wav")

newdata = data[::6]

sf.write("Recording2.wav", newdata, 8000)

data, samplerate = sf.read("Recording (2)_1.wav")

newdata = data[::6]

sf.write("Recording (2)2.wav", newdata, 8000)

print(samplerate)