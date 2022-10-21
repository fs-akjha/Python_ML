import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("tips.csv")

#names cab be sex, smoker, time, etc
figure = px.pie(data, 
             values='tip', 
             names='day',hole = 0.5)
figure.show()

#Refer:- https://thecleverprogrammer.com/2022/02/01/waiter-tips-prediction-with-machine-learning/