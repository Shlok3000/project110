import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

#fig = ff.create_distplot([data], ["reading_time"], show_hist=False)
#fig.show()

print("Population Mean: ", statistics.mean(data))

def rand_set_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = rand_set_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("Sample mean: ", statistics.mean(mean_list))

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

setup()