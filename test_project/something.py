__author__ = 'Mattia'

from matplotlib import pyplot as plt

#import matplotlib as mpl
#mpl.use('Qt4Agg')

import sys
import os
import json

#my_file = open("4f144ff15ccb6e3b0b00000e.json")

for all_file in os.listdir(os.getcwd()):
    if all_file.endswith(".json"):
        my_file = open(all_file)

        i            = 0
        dates        = {}
        time_windows = {}
        interArrival_times = {}

        # time_window in seconds
        time_window_length = 100

        index_baseline     = 1
        #time_window_counts = 0
        time_window_index  = 1

        for line in my_file:
            i += 1
            dates[i] = json.loads(line).get("created_at").get("$date")/1000

            interArrival_times[i] = dates.get(i-1, dates.get(i)) - dates.get(i)

            if dates[index_baseline] - dates[i] > time_window_length:
                time_window_index += 1
                index_baseline     = i

            time_windows[time_window_index] = time_windows.get(time_window_index, 0) + 1


        print(len(time_windows.values()))
        print(time_window_index)

        fig, ax = plt.subplots()
        ax.hist(dates.values(), 100, histtype='stepfilled')
        plt.show()

        #x = range(1, time_window_index)
        #plt.plot(x, time_windows.values())




        print("end")

print("end_end")