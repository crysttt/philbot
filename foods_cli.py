from flask import Flask, request
import foods

app = Flask(__name__)

@app.route('/')
def hello_world():
    return ' Hello, World!'


@app.route('/safe_foods', methods = ['GET', 'POST'])
def safe_foods():
    state = 'NO_QUERY'
    context = {}

    output_string = ''
    output = foods.ON_ENTER_STATE[state](context)
    output_string += output
    
    
    line = request.values.get('text')
    ret = foods.ON_INPUT[state](line, context)
    state, context, optional_output = ret
    if optional_output:
        output_string += optional_output

    output_string += foods.ON_ENTER_STATE[state](context)
    return(output_string)