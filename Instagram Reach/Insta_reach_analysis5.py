import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import PassiveAggressiveRegressor


data = pd.read_csv("Instagram.csv", encoding = 'latin1')
data = data.dropna()
data.info()

#x can be Impressions, From Home, From Explore, From Other, Saves, Comments, Likes etc columns
#y can be Impressions, From Home, From Explore, From Other, Saves, Comments, Likes etc columns
figure = px.scatter(data_frame = data, x="From Hashtags",
                    y="Likes", size="Likes", trendline="ols", 
                    title = "Relationship Between Likes and Impressions")
figure.show()


#Refer:- https://thecleverprogrammer.com/2022/03/22/instagram-reach-analysis-using-python/