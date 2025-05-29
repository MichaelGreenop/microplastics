
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pybaselines
import sklearn
import seaborn
import scipy


# The aim of this script is to A) Format a dataset from Omnic data, but importantly
# B) To provide a standardised formatting of ATR data from CSV files (naming, data types, etc.)



# Function 1: Extracts, checks, and combines the spectra from CSV files into a formatted dataframe

# Formatting check:
# Have all the spectra in the files the same spectral range
# Are the spectra named using a consistent naming style?
# Is all the data the same data type (or can it be standardised?)
# Are there any non-values?


# Function 2: Data seperation
# Needs to separate the dataset into wavenumber, sample name, class labels, and spectral dataset


# Function 3: Preprocessing
# Baseline correction, scaling, etc. for the data matrix

# recombine the dataset as required


