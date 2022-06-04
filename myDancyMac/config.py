"""Settings for audio reactive LED strip"""
from __future__ import print_function
from __future__ import division
import os

N_PIXELS = 300
"""This is just for the filters to work (not using LEDs atm)"""

USE_GUI = True
"""Whether or not to display a PyQtGraph GUI plot of visualization"""

DISPLAY_FPS = False
"""Whether to display the FPS when running (can reduce performance)"""

GAMMA_TABLE_PATH = os.path.join(os.path.dirname(__file__), 'gamma_table.npy')
"""Location of the gamma correction table"""

MIC_RATE = 48000
"""Sampling frequency of the microphone in Hz"""

FPS = 50
"""Desired refresh rate of the visualization (frames per second)"""

MIN_FREQUENCY = 200
"""Frequencies below this value will be removed during audio processing"""

MAX_FREQUENCY = 6000
"""Frequencies above this value will be removed during audio processing"""

N_FFT_BINS = 24
"""Number of frequency bins to use when transforming audio to frequency domain

Fast Fourier transforms are used to transform time-domain audio data to the
frequency domain. The frequencies present in the audio signal are assigned
to their respective frequency bins. This value indicates the number of
frequency bins to use.

A small number of bins reduces the frequency resolution of the visualization
but improves amplitude resolution. The opposite is true when using a large
number of bins. More bins is not always better!

There is no point using more bins than there are pixels on the LED strip.
"""

N_ROLLING_HISTORY = 2
"""Number of past audio frames to include in the rolling window"""

MIN_VOLUME_THRESHOLD = 1e-7
"""No music visualization displayed if recorded audio volume below threshold"""
