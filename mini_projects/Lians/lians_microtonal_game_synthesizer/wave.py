from random import choice
import numpy as np
import sounddevice as sd


NOTES = ['C', 'C𝄲', 'C♯|D♭', 'D𝄳', 'D', 'D𝄲', 'D♯|E♭', 'E𝄳', 
         'E', 'E𝄲|F𝄳', 'F', 'F𝄲', 'F♯|G♭', 'G𝄳', 'G', 'G𝄲', 
         'G♯|A♭', 'A𝄳', 'A', 'A𝄲', 'A♯|B♭', 'B𝄳', 'B', 'B𝄲|C𝄳']
FREQ = {}
A = 440
FS = 44100

    
def set_frequencies(pitch, scale=NOTES, scale_dict=FREQ):
    for note, steps in zip(scale, range(-18, 6)):
        f = pitch * 2 ** (steps / 24)
        scale_dict[note] = f


def play_note(note, scale_dict=FREQ, octave_modifiers=[1, 2, 4]):
    sd.stop()
    t = np.linspace(0, 1, FS, False)
    freq = scale_dict[note] * choice(octave_modifiers)
    tone = np.sin(2 * np.pi * freq * t)
    sd.play(tone, FS) 


set_frequencies(A)

# play_note("A")
# play_note("C")
# play_note("E")