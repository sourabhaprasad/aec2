import plotly.express as px
df = px.data.iris()
fig = px.line(df, y="sepal_width",)
fig.show()

fig = px.line(df, y="sepal_width", line_group='species')
fig.show()

df = px.data.tips()
# Creating the bar chart
fig = px.bar(df, x='day', y="total_bill")
fig.show()


df = px.data.tips()
# plotting the histogram
fig = px.histogram(df, x="total_bill")
fig.show()


df = px.data.tips()
# plotting the histogram
fig = px.histogram(df, x="total_bill", color='sex', nbins=50, histnorm='percent',barmode='overlay')
fig.show()

df = px.data.tips()
fig = px.pie(df, values="total_bill", names="day")
fig.show()

df = px.data.tips()
fig = px.box(df, x="day", y="tip")
fig.show()

df = px.data.tips()
# plotting the violin plot
fig = px.violin(df, x="day", y="tip")
fig.show()


df = px.data.tips()
fig = px.scatter_3d(df, x="total_bill", y="sex", z="tip")
fig.show()