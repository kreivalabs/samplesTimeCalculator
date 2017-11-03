#!/usr/bin/env python

# version 1.1.1 02-November-2017

# Convert samples to time, based on sampling rate, number of samples and seconds

# Import Future functions (www.python-future.org)
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import input

# Import math functionality
import math

title="Samples and Time Converter"
print(title)
print("=" * 80)

# Prompt for user input
sample_rate = float(input("Enter sample rate in kHz, for example - 44.1, 48, 88.2, 96: "))
num_samples = int(input("Enter number of samples as integer: "))
num_seconds = float(input("Enter elapsed time in seconds: "))

# Elapsed time = samples/sample rate
# Samples over time = sample rate * time (seconds)

samples_seconds = num_samples / (sample_rate * 1000)
samples_milliseconds = (num_samples / (sample_rate * 1000)) * 1000
samples_time = (sample_rate * 1000) * num_seconds

# return results, prompt for user input to exit
print("=" * 80)
print("Elapsed time in milliseconds: ", samples_milliseconds)
print()
print("Elapsed time in seconds: ", samples_seconds)
print()
print("Samples elapsed in", num_seconds, "seconds: ", samples_time)
print()
print("Press the <Enter> key to exit.")
input()
