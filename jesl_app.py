#! usr/bin/python3

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.title = 'JESL Calculator'

app.layout = html.Div(
    children=[
        html.Div(
            className='container-fluid',
            ),
        html.Div(
            className='app-header',
            children=[
                html.H1('Jessica\'s amazing percentage calculator app!', className='app-header--title')
            ]),
        html.Div(
            className='sub-text',
            children=[
                html.Div('This calculator will compute a student\'s percentage grade in a snap. Just try it and see...')
            ]),
        html.Div(
            className='total-points',
            children=[
                html.Div('Enter the total points here:')
            ]),
        html.Div(
            className='tp-input',
            children=[
        dcc.Input(id='total_points', value='', type='text')
            ]),
        html.Div(className='earned-points',
            children=[
                html.Div('Enter the earned points here:')
            ]),
        html.Div(
            className='ep-input',
            children=[
        dcc.Input(id='earned_points', value='', type='text')
            ]),
        html.Div(className='percentage',
            children=[
                html.Div('Ta da! You\'re grade is...')
            ]),
        html.Div(
            className='percent',
            children=[
        html.Div(id='percentage'),
            ]),
        html.Div(className='nonsense',
            children=[
                html.Div('I hope that you\'re happy with your grade because you earned it!')
            ]),
        ])

@app.callback(
    Output('percentage', 'children'),
    [Input('total_points', 'value'),
     Input('earned_points', 'value')])

def get_percentage(total_points, earned_points):

    float_total_points = float(total_points)

    while True:
        float_earned_points = float(earned_points)
        percent_grade = float_earned_points / float_total_points * 100

        return round(percent_grade, 0)

if __name__ == '__main__':
    app.run_server(debug=True)