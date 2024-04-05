import soundfile as sf
import numpy as np
from scipy import signal

input_signal,fs = sf.read("sing_mono.wav")
 #sampling frequency of Input signal
sampl_freq=fs
 #order of the filter
order=4
 #cutoff frquency
cutoff_freq=1000.0
 #digital frequency
Wn=2*cutoff_freq/sampl_freq
 # b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order, Wn, 'low')
print(b)
print(a)
 #filter the input signal with butterworth filter
output_signal = signal.filtfilt(b, a,input_signal[0:],padlen=1)
 #output signal = signal.lfilter(b, a,input signal)
 #write the output signal into .wav file
sf.write("Sound_With_ReducedNoise.wav",output_signal, fs)
