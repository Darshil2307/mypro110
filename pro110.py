import plotly.figure_factory as ff
import statistics as st
import random as rd
import pandas as pd
from scipy.__config__ import show

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].to_list()

fig=ff.create_distplot([data],["reading Time"], show_hist=False)
fig.show()

population_mean=st.mean(data)
print("Mean of the population is", population_mean)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        rd_index=rd.randint(0, len(data))
        value=data[rd_index]
        dataset.append(value)

    mean=st.mean(dataset)
    return(mean)

def show_fig(meanlist):
    df = meanlist
    fig = ff.create_distplot([df], ['reading_time'], show_hist = False)
    fig.show()
    
def setup():
    meanlist = []
    for i in range(0,100):
        setofmeans = random_set_of_means(10)
        meanlist.append(setofmeans)
    show_fig(meanlist)
    print('Sampling mean is', st.mean(meanlist))

setup()