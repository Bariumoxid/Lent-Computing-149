import numpy as np

def polyfit(dates, levels, p):
    d0 = dates[0] 
    return np.poly1d(np.polyfit(dates, levels, p)), d0

