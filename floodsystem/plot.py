import matplotlib.pyplot as plt
import datetime
from .datafetcher import fetch_measure_levels
import matplotlib
from .analysis import polyfit 

def plot_water_levels(station, dates, levels):
    plt.plot(dates,levels,'b-') #time to water levels 

    #labelling
    plt.xlabel(station.name)
    plt.ylabel("Water level")
    plt.title("Task 2E")
    plt.tight_layout()
    plt.axhline(y=station.typical_range[0],color ="red") #typical value
    plt.axhline(y=station.typical_range[1],color ="green") #typical value
    plt.show()

    #useless code
    #length=[0]
    #i=1
    #while i<=dates:
        #dt=i
        #outcome=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        #length.append(len(outcome[0]))
        #print(i)
        #i+=1
    #dt=dates
    #t=[]
    #level=[]
    #j=0
    #time,water_levels=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    #for j in range (dates):
        #t.append(time[int((length[j+1]-length[j])/2+length[j])])
        #level.append(water_levels[int((length[j+1]-length[j])/2+length[j])])
        #j+=1


def plot_water_level_with_fit(station, dates, levels, p):
    num_dates = matplotlib.dates.date2num(dates)
    num_dates -= num_dates[0]
    poly = polyfit(num_dates,levels,p)[0]

    plt.plot(dates, levels,label='actual')
    plt.plot(dates, poly(num_dates),'r--',label='best_fit')
    plt.xlabel("date")
    plt.ylabel("Water level")
    plt.legend(loc="upper left")
    plt.title(station.name)
    plt.show()

