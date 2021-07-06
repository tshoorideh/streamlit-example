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
class Boiler:
    def __init__(self, quantity, capacityMBH, turndown, efficiency):
        self.quantity = quantity
        self.capacityMBH = capacityMBH
        self.turndown = turndown  # number in percent. like 10
        self.efficiency = efficiency  # just the number like 81


TestBoiler = Boiler(1, 7000, 10, 81)

""" Test Boiler """
print(TestBoiler)
