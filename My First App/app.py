import webbrowser
import dash
import dash_bootstrap_components as dbc
from dash import dcc, html

from dash import dcc, html, Input, Output, State, callback
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

app.title = "My First Dash App"

app.layout = html.Div(
    [
        dbc.Card(
            [
                dbc.CardHeader("First Dash App"),
                dbc.CardBody(
                    [
                        html.Div(
                            [
                                dbc.Label("Number"),
                                dbc.Input(placeholder="Place a number here", type="text", id='num_input'),
                                dbc.FormText("Negative numbers are not allowed."),
                            ]
                        ), 
                        html.Div(
                            [
                                dbc.Label("Process"),
                                dbc.Select(
                                    id="process_select",
                                    options=[
                                        {"label": "Get Factorial", "value": 1},
                                        {"label": "Generate Fibonacci", "value": 2},
                                    ],
                                ),
                                dbc.FormText("Select an operation"),
                            ]
                        ), 
                        dbc.Button("Calculate!", id='btn_calculate', color='primary', n_clicks=0),
                        html.Div(id='output_area')
                    ]
                ),
            ],
            style={"width": "18rem"},
        )
    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "alignItems": "center",
        "height": "100vh",
    },
)

from utilities import generateFibonacci, getFactorial

@app.callback(
    [
        Output('output_area', 'children')
    ],
    [
        Input('btn_calculate', 'n_clicks')
    ], 
    [
        State('num_input', 'value'), 
        State('process_select', 'value')
    ]
)
def calculateResults(btncalculate_clicks, num_input, process_select):
    if btncalculate_clicks > 0:

        try:
            float_val = float(num_input)
        except (ValueError, TypeError):
            return ["Words are not allowed."]

        if not float_val.is_integer():
            return ["Integers only."]

        valid_num = int(float_val)

        if valid_num < 0:
            return ["No negative numbers."]

        process_select = int(process_select)

        if process_select == 1:
            factorial_value = getFactorial(valid_num)
            output_val = ("The factorial is "+ str(factorial_value) + ".")

        elif process_select == 2:
                fib_sequence = generateFibonacci(valid_num)
                fib_sequence_str = [str(i) for i in fib_sequence]
                output_seq = ", ".join(fib_sequence_str)
                output_val = ("We get the sequence "+ output_seq + ".")

        else:
            raise PreventUpdate

        return [output_val]

    else:
        raise PreventUpdate

if __name__ == '__main__':
    webbrowser.open('http://127.0.0.1:8050', autoraise=True)
    app.run()