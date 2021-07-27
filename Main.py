"""
    Main
"""

import Sender
import pyaudio


p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)

s = Sender.SenderObj(stream)

s.send(msg='0100101')

stream.close()