import matplotlib.pyplot as plt
import datetime
from .datafetcher import fetch_measure_levels

def plot_water_levels(station, dates, levels):
    dt=dates
    time=fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt)) 
    plt.plot(time[0],levels) #time to water levels 

    #labelling
    plt.xlabel(station.name)
    plt.ylabel("Water level")
    plt.title("Task 2E")
    plt.tight_layout()
    plt.axhline(y=station.typical_range[0]) #typical value
    plt.axhline(y=station.typical_range[1]) #typical value
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