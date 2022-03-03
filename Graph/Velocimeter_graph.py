import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = 0,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Agendamentos", 'font': {'size': 24}},
    delta = {'reference': 14, 'increasing': {'color': "black"}},
    gauge = {
        'axis': {'range': [None, 15], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'borderwidth': 5,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 8], 'color': 'blue'}],
            #{'range': [0, 15], 'color': 'white'},
            #{'range': [5, 10], 'color': 'white'},
            #{'range': [10, 15], 'color': 'white'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 14}}))

fig.update_layout(paper_bgcolor = "lavender", font = {'color': "red", 'family': "Arial", 'size': 40})

fig.show()