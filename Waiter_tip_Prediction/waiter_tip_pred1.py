import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("tips.csv")

#color can be sex, time, etc
figure = px.scatter(data_frame = data, x="total_bill",
                    y="tip", size="size", color= "day", trendline="ols")
figure.show()

#Refer:- https://thecleverprogrammer.com/2022/02/01/waiter-tips-prediction-with-machine-learning/