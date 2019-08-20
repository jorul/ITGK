import pyaudio
import numpy as np
 
p = pyaudio.PyAudio()
  
CONCERT_PITCH = 440  # kammertonen
HALF_INTERVAL = 2**(1 / 12)
C_FREQUENCY = CONCERT_PITCH * HALF_INTERVAL**(-9)
 
 
def play_tone(frequency, duration, volume=0.3):
    """
    Kode funnet på SO: https://stackoverflow.com/questions/8299303/generating-sine-wave-sound-in-python
    Se også: http://en.wikipedia.org/wiki/Bit_rate#Audio
    """
    sampling_rate = 44100
    global stream
    # generate samples, note conversion to float32 array
    samples = (np.sin(2 * np.pi * np.arange(sampling_rate * duration) * frequency / sampling_rate)).astype(np.float32)
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=sampling_rate, output=True)
    # play. May repeat with different volume values (if done interactively)
    stream.write(volume * samples)
 
 
def close():
    global stream
    stream.stop_stream()
    stream.close()
    p.terminate()
 
play_tone(440, 4)
 
close()
 
 
 
 
 
 
 def get_scale_frequencies(scale, start_frequency):
