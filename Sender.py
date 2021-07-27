"""
    Sender
"""
import numpy as np


class SenderObj:
    def __init__(self, stream):
        self.sampling_freq = 44100
        self.stream = stream

    def send(self, msg):
        amp = 0.3
        t = np.arange(0, 0.3, 1/self.sampling_freq)
        ssBit = amp*np.sin(2*np.pi*(2100)*t)
        on = amp*np.sin(2*np.pi*(880)*t)
        off = amp*np.sin(2*np.pi*(650)*t)
        start = ssBit
        for each in msg:
            if each == '1':
                start = np.concatenate((start, on))
            else:
                start = np.concatenate((start, off))
        start = np.concatenate((start, ssBit))
        self.data = start
        self.transmit()
        return

    def transmit(self):                    #np.float32
        self.stream.write(self.data.astype(np.float32).tobytes())
