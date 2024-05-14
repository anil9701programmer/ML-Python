import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

df_stocks = px.data.stocks()

# print(df_stocks.columns)  # ['date', 'GOOG', 'AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT']
# print(df_stocks['AAPL'].shape[0])
# print(df_stocks['GOOG'].shape[0])
# print(df_stocks['date'].shape[0])
# img = px.line(df_stocks, x='date', y='GOOG', labels={
#     'x': 'Date',
#     'y': 'Price'
# })
#
img = px.line(df_stocks, x='date', y=['GOOG', 'AAPL'], labels={
    'x': 'date',
    'y': 'prices'
}, title='Google Vs. Apple',hover_name='GOOG')
print("Graph is ready")
img.show()
