# First of all, what we are going to do is to import every library that would
# be needed in a future. Often the code will be upload to github by a windows
# OS, but this code is going to be developed to work in a raspberri pi board
# so sometimes will not work in your OS, but that is ok.

import numpy as np
import pandas as pd
# These two are for speed data processing, we are going to need them to
# arrange it correctly.

import matplotlib.pyplot as plt
# We import the module pyplot of that library because it will make figures with
# the data we will collect

import threading as thr
# This library allows us to run different loops at the same time se we can
# collect the data, process and plot it at the same time. Also we will use it
# to make fly the scout

##import RPi.GPIO as gpio
# The library that allows us to use the pins of the raspberry pi, the main
# library that will not work on common OS

# Then, what we want to do is to create an object, this object is our scout.
# Since this is going to be an embeded sistem, the hardware will work whit
# the code that we are going to write below. We have to understand the class
# as a subdivision of the main drone. The next functions we are going to write
# need to achieve all the goals that we have planted
class scout():
    def __init__(self, name, boss):
        self.name = name
        self.boss = boss