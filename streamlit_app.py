from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Defining Classes!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout out our [documentation](https://docs.streamlit.io) and
[community forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""

# ==========================================================================
# Defining equipment classes
class Boiler:
    def __init__(self, quantity, capacityMBH, turndown, efficiency):
        self.quantity = quantity
        self.capacityMBH = capacityMBH
        self.turndown = turndown  # number in percent. like 10
        self.efficiency = efficiency  # just the number like 81
        
class Chiller:
    def __init__(self, quantity, capacityMBH, turndown):
        self.quantity = quantity
        self.capacityMBH = capacityMBH
        self.turndown = turndown  # number in percent. like 10

class Pump:
    def __init__(self, quantity, HP, MaxGPM, turndown, efficiency):
        self.quantity = quantity
        self.HP = HP
        self.MaxGPM = MaxGPM
        self.turndown = turndown
        self.efficiency = efficiency
        
#Assigning values to each equipment, in reality we want to read this form the file.         
TestBoiler = Boiler(1, 7000, 10, 81)
CHWP1 = Pump(1, 10, 40, 10, 90)
TestChiller = Chiller(1, 150, 10)
tons = np.array([200, 180, 160, 140, 120, 100, 80, 60, 48])
kws = np.array([236.10, 191.70, 157.20, 131.20, 105.70, 80.02, 59.81, 47.39, 41.89])
n = 6

