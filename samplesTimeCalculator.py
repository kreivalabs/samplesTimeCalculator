#!/usr/bin/env python

#Convert samples to time, based on sampling rate, number of samples and seconds

#import Future functions (www.python-future.org)
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import input

#import math functionality
import math

#prompt for user input
sample_rate = float(input("Enter sample rate in kHz, for example - 44.1, 48, 88.2, 96: "))
num_samples = int(input("Enter number of samples as integer: "))
num_seconds = float(input("Enter elapsed time in seconds: "))

#Elapsed time = samples/sample rate
#Samples over time = sample rate * time (seconds)
samples_seconds = num_samples / (sample_rate * 1000)
samples_milliseconds = (num_samples / (sample_rate * 1000)) * 1000
samples_time = (sample_rate * 1000) * num_seconds

#display results, prompt for user input to exit
print('Elapsed time in milliseconds: ', samples_milliseconds)
print('Elapsed time in seconds: ', samples_seconds)
print('Samples elapsed: ', samples_time)
print('Press the <Enter> key to exit.')
input()
