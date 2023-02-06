from .analysis import polyfit 
import matplotlib




def predict_water_level(dates, levels, days_future):
    num_dates = matplotlib.dates.date2num(dates)
    num_dates -= num_dates[0]
    poly = polyfit(num_dates,levels,4)[0]
    prediction = poly(num_dates[0]+days_future)
    return prediction