import plotly.express as px
import plotly.graph_objs as go

# df_us = px.data.gapminder().query("country == 'United States'")
# img_1 = px.bar(df_us,x='country',y='pop')
# print("Graph is ready")
# img_1.show()

# df_tips = px.data.tips()
# img_2 = px.bar(df_tips, x='day', y='tip', color='sex', title='Tips by each gender',
#                labels={'tip': "tip Amount",
#                        'day': "day of the week"
#                        },
#                barmode='group'
#                )
# print("Graph is ready")
# img_2.show()


# plotly bar using figure

df_europe = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
# print(df_europe.columns)
# ['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap','iso_alpha', 'iso_num']
text = df_europe['pop'].to_numpy()
fig = go.Figure()
fig.add_trace(go.Bar(x=df_europe.country,
                     y=text,
                     text=text,
                     marker_color='blue'))
print("Graph is ready")
fig.show()
