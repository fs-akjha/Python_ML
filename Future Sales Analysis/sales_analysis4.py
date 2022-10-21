import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression

data = pd.read_csv("advertising.csv")

correlation = data.corr()
print(correlation["Sales"].sort_values(ascending=False))

#Refer:- https://thecleverprogrammer.com/2022/03/01/future-sales-prediction-with-machine-learning/