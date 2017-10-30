This utility prompts for three user inputs: sampling rate (44.1 kHz, 48 kHz, 88.2 kHz, or, 96 kHz), number of samples completed, 
and unit time in seconds. It returns:

1. The elapsed time in milliseconds necessary for the given number of samples to pass at the given sample rate,
2. The elapsed time in seconds necessary for the given number of samples to pass at the given sample rate, and,
3. The number of samples completed for the given sample rate and unit time (in seconds).

This Python script utilizes the Future additions from http://www.python-future.org
