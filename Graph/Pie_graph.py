import plotly.graph_objects as go

colors = ['lightblue', 'lightgreen']
labels = ['Trabalhados','Agendados']
values = [2891, 395]

fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='value', textfont_size=50, marker=dict(colors=colors, line=dict(color='#000000', width=2)))])
fig.show()